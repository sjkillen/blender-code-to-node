#!/usr/bin/env -S blender -b -P

import bpy
from bpy.types import ShaderNodeTree, Context, Text
from node_code_ast import *


def reduce_vars(program: Program, symbols: SymbolTable) -> Program:
    def replace_var_with_value(var: VarExpr):
        if symbols.is_input(var.id):
            return var
        if (v := symbols[var.id]) is None:
            raise Exception("Variable", var.id, "Used before assignment")
        return v

    def update_values(assignment: Assignment):
        assignment = assignment.transform_type(replace_var_with_value, VarExpr)
        symbols[assignment.id] = assignment.expr
        return assignment

    return program.transform_type(update_values, Assignment)


def create_tree(name: str, text: str):
    symbols, program = parse(text)
    program = reduce_vars(program, symbols)
    tree = bpy.data.node_groups.new(name, "ShaderNodeTree")
    input_node = tree.nodes.new("NodeGroupInput")
    output_node = tree.nodes.new("NodeGroupOutput")
    value_numbering = dict()

    for expr in program.walk_all():
        if expr in value_numbering:
            continue
        edge = None
        if isinstance(expr, Program):
            continue
        elif isinstance(expr, Assignment):
            if expr.qualifier is Qualifier.OUT and expr.id not in output_node.inputs:
                tree.outputs.new(type="NodeSocketFloat", name=expr.id)
                edge = (output_node.inputs[expr.id], None)
            continue
        elif isinstance(expr, Number):
            node = tree.nodes.new("ShaderNodeValue")
            node.outputs[0].default_value = float(expr.value)
            edge = (None, node.outputs[0])
        elif isinstance(expr, UnaryExpr):
            node = tree.nodes.new("ShaderNodeMath")
            if expr.op == "-":
                node.operation = "SUBTRACT"
                node.inputs[0].default_value = 0.0
                edge = (node.inputs[1], node.outputs[0])
            elif expr.op == "!":
                node.operation = "COMPARE"
                node.inputs[1].default_value = 0
                node.inputs[2].default_value = 0
                aux = tree.nodes.new("ShaderNodeMath")
                aux.operation = "LESS_THAN"
                aux.inputs[1].default_value = 1
                aux.inputs[2].default_value = 0
                tree.links.new(node.outputs[0], aux.inputs[0])
                edge = (node.inputs[0], aux.outputs[0])
            else:
                raise Exception("unknown unary op")
        elif isinstance(expr, VarExpr):
            if symbols.is_input(expr.id):
                tree.inputs.new(type="NodeSocketFloat", name=expr.id)
                edge = (None, input_node.outputs[expr.id])
            elif symbols.is_output(expr.id):
                continue
            else:
                raise Exception("Bare variable found when not expected")
        elif isinstance(expr, BinaryExpr):
            node = tree.nodes.new("ShaderNodeMath")
            basic_ops = {
                "<": "LESS_THAN",
                ">": "GREATER_THAN",
                "**": "POWER",
                "+": "ADD",
                "-": "SUBTRACT",
                "*": "MULTIPLY",
                "/": "DIVIDE",
                "%": "MODULO",
            }
            if expr.op in basic_ops:
                node.operation = basic_ops[expr.op]
                edge = ((node.inputs[0], node.inputs[1]), node.outputs[0])
            else:
                raise Exception("Binary operation", expr.op, "not yet supported")
        else:
            raise Exception("Unknown Expr", expr)
        if edge is not None:
            value_numbering[expr] = edge

    for expr in program.walk_all():
        if isinstance(expr, Assignment) and expr.qualifier is Qualifier.OUT:
            _, o = value_numbering[expr.expr]
            tree.links.new(o, output_node.inputs[expr.id])
            continue
        edge = value_numbering.get(expr, None)
        if edge is None:
            continue
        if isinstance(expr, UnaryExpr):
            _, o = value_numbering[expr.expr]
            i, _ = edge
            tree.links.new(o, i)
        if isinstance(expr, BinaryExpr):
            subA, subB = value_numbering[expr.left], value_numbering[expr.right]
            _, o1 = subA
            _, o2 = subB
            (i1, i2), _ = edge
            tree.links.new(o1, i1)
            tree.links.new(o2, i2)


class CodeToNodeGroupOperator(bpy.types.Operator):
    bl_idname = "text.codetonodegroup"
    bl_label = "Code To Node Group"

    @classmethod
    def poll(cls, context: Context):
        return hasattr(context, "edit_text")

    def execute(self, context):
        text: Text = context.edit_text
        create_tree(text.name, text.as_string())
        return {"FINISHED"}


def menu(self, _context):
    self.layout.operator(CodeToNodeGroupOperator.bl_idname)


def register():
    bpy.types.TEXT_MT_format.append(menu)


def unregister():
    bpy.types.TEXT_MT_format.remove(menu)


def test():
    example = """
    input h
    x = 1 * h
    y = 2 * h
    z = x + y * h
    y = 1 * h
    x = 30 * h
    z = y ** x * h
    """

    result = """
    x = (1 * h)
    y = (2 * h)
    z = ((1 * h) + ((2 * h) * h))
    y = (1 * h)
    x = (30 * h)
    z = (((1 * h) ** (30 * h)) * h)
    """

    symbols, program = parse(example)
    reduced = reduce_vars(program, symbols)
    assert reduced == parse(result)[1]

    example2 = """
    input a
    output y = a * 42 + 10
    """

    create_tree("test", example2)


import sys

if __name__ == "__main__" and not sys.flags.interactive:
    test()
    print("Tests passed :)")

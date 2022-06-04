# Generated from NodeCode.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,74,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,1,1,1,1,2,3,2,18,8,2,1,2,1,2,1,2,3,2,23,8,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,41,8,3,
        10,3,12,3,44,9,3,3,3,46,8,3,1,3,3,3,49,8,3,1,3,3,3,52,8,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,69,8,3,
        10,3,12,3,72,9,3,1,3,0,1,6,4,0,2,4,6,0,5,1,0,1,2,1,0,9,10,1,0,12,
        14,2,0,7,7,15,15,1,0,16,19,85,0,11,1,0,0,0,2,14,1,0,0,0,4,17,1,0,
        0,0,6,51,1,0,0,0,8,10,3,4,2,0,9,8,1,0,0,0,10,13,1,0,0,0,11,9,1,0,
        0,0,11,12,1,0,0,0,12,1,1,0,0,0,13,11,1,0,0,0,14,15,7,0,0,0,15,3,
        1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,17,18,1,0,0,0,18,19,1,0,0,0,
        19,22,5,21,0,0,20,21,5,3,0,0,21,23,3,6,3,0,22,20,1,0,0,0,22,23,1,
        0,0,0,23,5,1,0,0,0,24,25,6,3,-1,0,25,52,5,21,0,0,26,52,5,22,0,0,
        27,28,5,4,0,0,28,29,3,6,3,0,29,30,5,5,0,0,30,52,1,0,0,0,31,32,5,
        6,0,0,32,52,3,6,3,8,33,34,5,7,0,0,34,52,3,6,3,7,35,36,5,21,0,0,36,
        45,5,4,0,0,37,42,3,6,3,0,38,39,5,8,0,0,39,41,3,6,3,0,40,38,1,0,0,
        0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,46,1,0,0,0,44,42,
        1,0,0,0,45,37,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,47,49,5,8,0,0,
        48,47,1,0,0,0,48,49,1,0,0,0,49,50,1,0,0,0,50,52,5,5,0,0,51,24,1,
        0,0,0,51,26,1,0,0,0,51,27,1,0,0,0,51,31,1,0,0,0,51,33,1,0,0,0,51,
        35,1,0,0,0,52,70,1,0,0,0,53,54,10,5,0,0,54,55,7,1,0,0,55,69,3,6,
        3,5,56,57,10,4,0,0,57,58,5,11,0,0,58,69,3,6,3,4,59,60,10,3,0,0,60,
        61,7,2,0,0,61,69,3,6,3,4,62,63,10,2,0,0,63,64,7,3,0,0,64,69,3,6,
        3,3,65,66,10,1,0,0,66,67,7,4,0,0,67,69,3,6,3,2,68,53,1,0,0,0,68,
        56,1,0,0,0,68,59,1,0,0,0,68,62,1,0,0,0,68,65,1,0,0,0,69,72,1,0,0,
        0,70,68,1,0,0,0,70,71,1,0,0,0,71,7,1,0,0,0,72,70,1,0,0,0,9,11,17,
        22,42,45,48,51,68,70
    ]

class NodeCodeParser ( Parser ):

    grammarFileName = "NodeCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'input'", "'output'", "'='", "'('", "')'", 
                     "'!'", "'-'", "','", "'=='", "'!='", "'**'", "'*'", 
                     "'/'", "'%'", "'+'", "'<'", "'>'", "'<='", "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WS", "IDENTIFIER", "NUMBER" ]

    RULE_program = 0
    RULE_qualifier = 1
    RULE_assignment = 2
    RULE_expr = 3

    ruleNames =  [ "program", "qualifier", "assignment", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    WS=20
    IDENTIFIER=21
    NUMBER=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NodeCodeParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(NodeCodeParser.AssignmentContext,i)


        def getRuleIndex(self):
            return NodeCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = NodeCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NodeCodeParser.T__0) | (1 << NodeCodeParser.T__1) | (1 << NodeCodeParser.IDENTIFIER))) != 0):
                self.state = 8
                self.assignment()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return NodeCodeParser.RULE_qualifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQualifier" ):
                return visitor.visitQualifier(self)
            else:
                return visitor.visitChildren(self)




    def qualifier(self):

        localctx = NodeCodeParser.QualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_qualifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            _la = self._input.LA(1)
            if not(_la==NodeCodeParser.T__0 or _la==NodeCodeParser.T__1):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(NodeCodeParser.IDENTIFIER, 0)

        def qualifier(self):
            return self.getTypedRuleContext(NodeCodeParser.QualifierContext,0)


        def expr(self):
            return self.getTypedRuleContext(NodeCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return NodeCodeParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = NodeCodeParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==NodeCodeParser.T__0 or _la==NodeCodeParser.T__1:
                self.state = 16
                self.qualifier()


            self.state = 19
            self.match(NodeCodeParser.IDENTIFIER)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==NodeCodeParser.T__2:
                self.state = 20
                self.match(NodeCodeParser.T__2)
                self.state = 21
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return NodeCodeParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NegContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NodeCodeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(NodeCodeParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeg" ):
                return visitor.visitNeg(self)
            else:
                return visitor.visitChildren(self)


    class FuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NodeCodeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(NodeCodeParser.IDENTIFIER, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NodeCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(NodeCodeParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)


    class LnotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NodeCodeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(NodeCodeParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLnot" ):
                return visitor.visitLnot(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NodeCodeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(NodeCodeParser.IDENTIFIER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NodeCodeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(NodeCodeParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class ParenthContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NodeCodeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(NodeCodeParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenth" ):
                return visitor.visitParenth(self)
            else:
                return visitor.visitChildren(self)


    class Lt_gt_le_geContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NodeCodeParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NodeCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(NodeCodeParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLt_gt_le_ge" ):
                return visitor.visitLt_gt_le_ge(self)
            else:
                return visitor.visitChildren(self)


    class PowContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NodeCodeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NodeCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(NodeCodeParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPow" ):
                return visitor.visitPow(self)
            else:
                return visitor.visitChildren(self)


    class Add_subContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NodeCodeParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NodeCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(NodeCodeParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_sub" ):
                return visitor.visitAdd_sub(self)
            else:
                return visitor.visitChildren(self)


    class Eq_neContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NodeCodeParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NodeCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(NodeCodeParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq_ne" ):
                return visitor.visitEq_ne(self)
            else:
                return visitor.visitChildren(self)


    class Mul_div_modContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NodeCodeParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NodeCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(NodeCodeParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_div_mod" ):
                return visitor.visitMul_div_mod(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = NodeCodeParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = NodeCodeParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 25
                self.match(NodeCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                localctx = NodeCodeParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(NodeCodeParser.NUMBER)
                pass

            elif la_ == 3:
                localctx = NodeCodeParser.ParenthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 27
                self.match(NodeCodeParser.T__3)
                self.state = 28
                self.expr(0)
                self.state = 29
                self.match(NodeCodeParser.T__4)
                pass

            elif la_ == 4:
                localctx = NodeCodeParser.LnotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.match(NodeCodeParser.T__5)
                self.state = 32
                self.expr(8)
                pass

            elif la_ == 5:
                localctx = NodeCodeParser.NegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 33
                self.match(NodeCodeParser.T__6)
                self.state = 34
                self.expr(7)
                pass

            elif la_ == 6:
                localctx = NodeCodeParser.FuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 35
                self.match(NodeCodeParser.IDENTIFIER)
                self.state = 36
                self.match(NodeCodeParser.T__3)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NodeCodeParser.T__3) | (1 << NodeCodeParser.T__5) | (1 << NodeCodeParser.T__6) | (1 << NodeCodeParser.IDENTIFIER) | (1 << NodeCodeParser.NUMBER))) != 0):
                    self.state = 37
                    self.expr(0)
                    self.state = 42
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 38
                            self.match(NodeCodeParser.T__7)
                            self.state = 39
                            self.expr(0) 
                        self.state = 44
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,3,self._ctx)



                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NodeCodeParser.T__7:
                    self.state = 47
                    self.match(NodeCodeParser.T__7)


                self.state = 50
                self.match(NodeCodeParser.T__4)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 68
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = NodeCodeParser.Eq_neContext(self, NodeCodeParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 53
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 54
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==NodeCodeParser.T__8 or _la==NodeCodeParser.T__9):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 55
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = NodeCodeParser.PowContext(self, NodeCodeParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 57
                        self.match(NodeCodeParser.T__10)
                        self.state = 58
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = NodeCodeParser.Mul_div_modContext(self, NodeCodeParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 60
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NodeCodeParser.T__11) | (1 << NodeCodeParser.T__12) | (1 << NodeCodeParser.T__13))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 61
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = NodeCodeParser.Add_subContext(self, NodeCodeParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 63
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==NodeCodeParser.T__6 or _la==NodeCodeParser.T__14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 64
                        self.expr(3)
                        pass

                    elif la_ == 5:
                        localctx = NodeCodeParser.Lt_gt_le_geContext(self, NodeCodeParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 65
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 66
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NodeCodeParser.T__15) | (1 << NodeCodeParser.T__16) | (1 << NodeCodeParser.T__17) | (1 << NodeCodeParser.T__18))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 67
                        self.expr(2)
                        pass

             
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         





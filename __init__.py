# Code To Node: Convert textual code to a blender node group
# Copyright (C) 2022  Spencer Killen
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "CodeToNode",
    "author": "sjkillen",
    "description": "Convert textual code to a blender node group",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Generic",
}

from sys import path
from os.path import dirname

path.insert(0, dirname(__file__))

from . import auto_load

auto_load.init()


def register():
    auto_load.register()


def unregister():
    auto_load.unregister()

import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class ArrayPopNode(ArmLogicTreeNode):
    '''Array pop node'''
    bl_idname = 'LNArrayPopNode'
    bl_label = 'Array Pop'
    bl_icon = 'NONE'

    def init(self, context):
        self.add_input('ArmNodeSocketArray', 'Array')
        self.add_output('NodeSocketShader', 'Value')

add_node(ArrayPopNode, category=MODULE_AS_CATEGORY)

import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class ArraySpliceNode(ArmLogicTreeNode):
    '''Array splice node'''
    bl_idname = 'LNArraySpliceNode'
    bl_label = 'Array Splice'
    bl_icon = 'NONE'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketArray', 'Array')
        self.add_input('NodeSocketInt', 'Index')
        self.add_input('NodeSocketInt', 'Length')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(ArraySpliceNode, category=MODULE_AS_CATEGORY)

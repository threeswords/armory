import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class NoneNode(ArmLogicTreeNode):
    '''None node'''
    bl_idname = 'LNNoneNode'
    bl_label = 'None'
    bl_icon = 'NONE'

    def init(self, context):
        self.add_output('NodeSocketShader', 'None')

add_node(NoneNode, category=MODULE_AS_CATEGORY)

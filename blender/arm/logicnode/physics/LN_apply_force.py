import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class ApplyForceNode(ArmLogicTreeNode):
    '''Apply force node'''
    bl_idname = 'LNApplyForceNode'
    bl_label = 'Apply Force'
    bl_icon = 'NONE'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_input('NodeSocketVector', 'Force')
        self.add_input('NodeSocketBool', 'On Local Axis')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(ApplyForceNode, category=MODULE_AS_CATEGORY, section='force')

import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class BoneFKNode(ArmLogicTreeNode):
    '''Bone Forward Kinematics node'''
    bl_idname = 'LNBoneFKNode'
    bl_label = 'Bone FK'
    bl_icon = 'NONE'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_input('NodeSocketString', 'Bone')
        self.add_input('NodeSocketShader', 'Transform')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(BoneFKNode, category=MODULE_AS_CATEGORY, section='armature')

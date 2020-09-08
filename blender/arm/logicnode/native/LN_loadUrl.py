import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class LoadUrlNode(ArmLogicTreeNode):
    '''Load Url'''
    bl_idname = 'LNLoadUrlNode'
    bl_label = 'Load Url (Browser only)'
    bl_icon = 'NONE'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketString', 'URL')

add_node(LoadUrlNode, category=MODULE_AS_CATEGORY)

import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class ScriptNode(ArmLogicTreeNode):
    '''Script node'''
    bl_idname = 'LNScriptNode'
    bl_label = 'Script'
    bl_icon = 'NONE'

    @property
    def property0(self):
        return bpy.data.texts[self.property0_].as_string() if self.property0_ in bpy.data.texts else ''


    property0_: StringProperty(name='Text', default='')

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketArray', 'Array')
        self.add_output('ArmNodeSocketAction', 'Out')
        self.add_output('NodeSocketShader', 'Result')

    def draw_buttons(self, context, layout):
        layout.prop_search(self, 'property0_', bpy.data, 'texts', icon='NONE', text='')

add_node(ScriptNode, category=MODULE_AS_CATEGORY, section='haxe')

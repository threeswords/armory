import bpy
import arm
from arm import log, props_ui

if arm.is_reload(__name__):
    props_ui = arm.reload_module(props_ui)
else:
    arm.enable_reload(__name__)

arm_keymaps = []


def register():
    wm = bpy.context.window_manager
    addon_keyconfig = wm.keyconfigs.addon

    # Keyconfigs are not available in background mode. If the keyconfig
    # was not found despite running _not_ in background mode, a warning
    # is printed
    if addon_keyconfig is None:
        if not bpy.app.background:
            log.warn("No keyconfig path found")
        return

    km = addon_keyconfig.keymaps.new(name='Window', space_type='EMPTY', region_type="WINDOW")
    km.keymap_items.new(props_ui.ArmoryPlayButton.bl_idname, type='F5', value='PRESS')
    km.keymap_items.new("tlm.build_lightmaps", type='F6', value='PRESS')
    km.keymap_items.new("tlm.clean_lightmaps", type='F7', value='PRESS')
    arm_keymaps.append(km)


def unregister():
    wm = bpy.context.window_manager
    for km in arm_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    del arm_keymaps[:]

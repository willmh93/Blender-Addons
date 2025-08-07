import bpy
import subprocess
import sys


bl_info = {
    "name": "Open Project Folder - Hotkey",
    "author": "Will Hemsworth",
    "version": (0, 1, 0),
    "blender": (2, 80, 0),
    "description": "Open Project Folder with 'CTRL-ALT-HOME'",
    "category": "Screen"
}

class Addon_OpenProjectFolder(bpy.types.Operator):
    
    bl_idname = "wm.open_project_folder"
    bl_label = "Open Project Directory"
    
    def __init__(self):
        print("Start")
        
    def __del__(self):
        print("End")
    
    def execute(self, context):     
        print("Executing Addon_OpenProjectFolder")
           
        path = bpy.path.abspath("//")
        sys.path.append(path)

        print(path)

        subprocess.Popen('explorer ' + path)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        print("Invoking Addon_OpenProjectFolder")
        return self.execute(context)

addon_keymaps = []

def register():
    bpy.utils.register_class(Addon_OpenProjectFolder)
    print("Registered Addon_OpenProjectFolder")
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name= 'Screen', space_type='EMPTY')
        kmi = km.keymap_items.new("wm.open_project_folder", type='HOME', value='PRESS', alt=True, ctrl=True)
        addon_keymaps.append((km, kmi))
        
def unregister():
    for km,kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(Addon_OpenProjectFolder)

if __name__ == "__main__":
    register()
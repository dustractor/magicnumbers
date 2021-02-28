bl_info = {
    "name":"Magic Numbers",
    "blender":(2,80,0),
    "category":"System",
    "description":"attempt to collect several useful quote unquote magic numbers",
    "location":"UI -> mostly useful places"
}
import bpy
class MAGICNUMBERS_OT_clipboard_set(bpy.types.Operator):
    bl_idname = "magicnumbers.clipboard_set"
    bl_label = "fill clipboard with value"
    value: bpy.props.StringProperty()
    def execute(self,context):
        context.window_manager.clipboard = self.value
        self.report({"INFO"},self.value)
        return {"FINISHED"}

data = (
    ("Magic Angle","54.73561"),
    ("Magic Angle Complement","35.26439"),
    ("Magic Angle [Formula]","acos(1/sqrt(3))*(180/acos(-1))"),
    ("Magic Angle Complement [Formula]","90-(acos(1/sqrt(3))*(180/acos(-1)))"),
    ("Golden Ratio","1.618034"),
    ("Golden Ratio [Formula]","(1+sqrt(5))/2")
)
class MAGICNUMBERS_MT_top_menu(bpy.types.Menu):
    bl_label = "Magic Numbers"
    def draw(self,context):
        layout = self.layout
        for label,value in data:
            op = layout.operator("magicnumbers.clipboard_set",text=label)
            op.value = value
        

drawfunc = lambda s,c:s.layout.menu("MAGICNUMBERS_MT_top_menu")
def register():
    print("bpy.app.version:",bpy.app.version)
    bpy.utils.register_class(MAGICNUMBERS_MT_top_menu)
    bpy.utils.register_class(MAGICNUMBERS_OT_clipboard_set)
    bpy.types.TOPBAR_MT_help.append(drawfunc)

def unregister():
    bpy.types.TOPBAR_MT_help.remove(drawfunc)
    bpy.utils.unregister_class(MAGICNUMBERS_MT_top_menu)
    bpy.utils.unregister_class(MAGICNUMBERS_OT_clipboard_set)

import bpy
from bpy.props import FloatProperty, IntProperty
from bpy.types import Panel, Operator


# ——————————————————————————————————————————————————————————————————————
# MARK: PROPERTIES
# ——————————————————————————————————————————————————————————————————————


class HelloWorldProperties(bpy.types.PropertyGroup):
    custom_1: FloatProperty(name="My Float")
    custom_2: IntProperty(name="My Int")


# ——————————————————————————————————————————————————————————————————————
# MARK: INTERFACE
# ——————————————————————————————————————————————————————————————————————


class TEMPLATE_PT_hello_world_panel(Panel):
    bl_label = "Hello World"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Hello World"
    bl_context = "objectmode"  # Optional for limiting access to the panel to a certain context

    def draw(self, context):
        props = context.scene.hello_world_properties

        layout = self.layout

        layout.label(text="Hello World")
        layout.prop(props, "custom_1")
        layout.prop(props, "custom_2")
        layout.operator("template.hello_world")

        header, panel = layout.panel("my_subpanel_id", default_closed=False)
        header.label(text="My Subpanel")
        if panel:
            panel.label(text="Success")


# ——————————————————————————————————————————————————————————————————————
# MARK: OPERATORS
# ——————————————————————————————————————————————————————————————————————


class TEMPLATE_OT_hello_world_operator(Operator):
    bl_idname = "template.hello_world"  # {category}.{operator_name} or {addon_name}.{operator_name}
    bl_label = "Minimal Operator"
    bl_context = "objectmode"
    bl_options = {"REGISTER", "UNDO"}  # Some operators shouldn't include an 'UNDO' (read-only and temporary UI e.g)
    # bl_options = {"INTERNAL"}        # ...this would be more suitable in such cases

    def execute(self, context):
        addon_prefs = context.preferences.addons[__package__]  # This is how we access the addon preferences

        print("Hello World")
        return {"FINISHED"}

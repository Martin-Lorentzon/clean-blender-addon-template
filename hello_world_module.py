import bpy
from bpy.props import FloatProperty, IntProperty


# ——————————————————————————————————————————————————
# PROPERTIES
# ——————————————————————————————————————————————————


class HelloWorldProperties(bpy.types.PropertyGroup):
    custom_1: FloatProperty(name="My Float")
    custom_2: IntProperty(name="My Int")


# ——————————————————————————————————————————————————
# USER INTERFACE
# ——————————————————————————————————————————————————


class TEMPLATE_PT_hello_world_panel(bpy.types.Panel):
    bl_label = "Hello World"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Hello World"
    bl_context = "object"

    def draw(self, context):
        properties = context.scene.hello_world_properties

        layout = self.layout

        layout.label(text="Hello World")
        layout.prop(properties, "custom_1")
        layout.prop(properties, "custom_2")


# ——————————————————————————————————————————————————
# OPERATORS
# ——————————————————————————————————————————————————


class TEMPLATE_OT_hello_world_operator(bpy.types.Operator):
    bl_idname = "template.hello_world"  # {category}.{operator_name}
    bl_label = "Minimal Operator"

    def execute(self, context):
        print("Hello World")
        return {"FINISHED"}

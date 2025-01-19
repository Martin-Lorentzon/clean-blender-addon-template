bl_info = {
    "name": "Template Add-on Name",
    "description": "Template add-on description",
    "author": "Your Name",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "location": "3D Viewport > N Panel > ...",
    # "doc_url": "https://github.com/{username}/{repo-name}",
    # "tracker_url": "https://github.com/{username}/{repo-name}/issues",
    # "warning": "BETA Version",
    # "warning": "Pre-Release",
    "support": "COMMUNITY",
    # Try to fit into an existing category (or your company name)
    "category": "Choose a category",
}


# ——————————————————————————————————————————————————
# IMPORTS
# ——————————————————————————————————————————————————


if "bpy" in locals():
    # Modules to reload during development go here
    import importlib

    importlib.reload(hello_world_module)
else:
    # ...and here
    from . import hello_world_module

import bpy


# ——————————————————————————————————————————————————
# REGISTRATION
# ——————————————————————————————————————————————————


# Classes Blender should know about go in this list
classes = [
    hello_world_module.HelloWorldProperties,
    hello_world_module.TEMPLATE_PT_hello_world_panel,
    hello_world_module.TEMPLATE_OT_hello_world_operator,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.hello_world_properties = bpy.props.PointerProperty(type=hello_world_module.HelloWorldProperties)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.hello_world_properties


if __name__ == "__main__":
    register()

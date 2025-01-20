import bpy
for i in bpy.data.images:
    i.name = bpy.path.display_name_from_filepath(i.filepath)
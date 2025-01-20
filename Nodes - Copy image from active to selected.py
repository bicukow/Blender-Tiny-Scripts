import bpy
image_of_active_node = bpy.context.active_object.active_material.node_tree.nodes.active.image
selected_nodes = [i for i in bpy.context.active_object.active_material.node_tree.nodes if i.select==True]

for i in selected_nodes:
    i.image = image_of_active_node
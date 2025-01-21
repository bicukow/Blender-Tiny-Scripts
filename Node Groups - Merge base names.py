import bpy
from re import search

#remove ".001" tail if node is single
for i in bpy.data.node_groups:
    if search('.\d\d\d', i.name):
        if bpy.data.node_groups.find(i.name[:-4]):
            print('will be renamed:', i.name)
            i.name = i.name[:-4]
       
def replace_node_groups():
    if node.type == 'GROUP' and search('.\d\d\d', node.node_tree.name): # search for group node AND .001 tails
        if 'Geometry Nodes' not in node.node_tree.name: # do not search for node groups with default names
            if 'NodeGroup' not in node.node_tree.name:  # do not search for node groups with default names
                node.node_tree = bpy.data.node_groups[node.node_tree.name[:-4]]

## for node_groups (geometry nodes)
for node_group in bpy.data.node_groups:
    for node in node_group.nodes:
        replace_node_groups()

## for materials
for mats in bpy.data.materials: 
    for node in mats.node_tree.nodes:
        replace_node_groups()     
        

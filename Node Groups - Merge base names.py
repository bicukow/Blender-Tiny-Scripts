import bpy
from re import search

def delete_single_tails():              #delete ".001" tail if node is single
    for i in bpy.data.node_groups:
        if search('.\d\d\d', i.name):
            if bpy.data.node_groups.find(i.name[:-4]):
                print('will be renamed:', i.name)
                i.name = i.name[:-4]
                
delete_single_tails()
       
def replace_node_groups():
    if node.type == 'GROUP' and search('.\d\d\d', node.node_tree.name):
        node.node_tree = bpy.data.node_groups[node.node_tree.name[:-4]]

for node_group in bpy.data.node_groups: # for node_groups (geometry nodes)
    for node in node_group.nodes:
        replace_node_groups()

for mats in bpy.data.materials:         # for materials
    for node in mats.node_tree.nodes:
        replace_node_groups()
            

        
        
import bpy
from re import search

node_groups = [_ for _ in bpy.data.node_groups if _.is_editable] #filter linked nodes  
regex_search = '\.\d\d\d'

#remove ".001" tail if node is single
for i in node_groups:
    if search(regex_search, i.name):
        if bpy.data.node_groups.find(i.name[:-4]):
            i.name = i.name[:-4]
       
def replace_node_groups():
    if node.type == 'GROUP':                                 # search for 'GROUP' type
        if type(node.node_tree) is not type(None):           # filter NoneType
            if node.node_tree.is_editable:                   # do not search linked nodes
                if all([
                search(regex_search,node.node_tree.name),       # search for .001 tails
                'Geometry Nodes' not in node.node_tree.name, # do not search for node groups with default names
                'NodeGroup'      not in node.node_tree.name, # do not search for node groups with default names
                ]):
                    node.node_tree = bpy.data.node_groups[node.node_tree.name[:-4]]

## for node_groups (geometry nodes)
for node_group in node_groups:
    for node in node_group.nodes:
        replace_node_groups()

## for materials
for mats in bpy.data.materials: 
    if type(mats.node_tree) is not type(None):
        for node in mats.node_tree.nodes:
            replace_node_groups()

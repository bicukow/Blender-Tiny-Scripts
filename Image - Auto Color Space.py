import bpy

for i in bpy.data.images:
    for tocken in ['nrm','norm','_n_']:
        if tocken in bpy.path.display_name(i.filepath):
            i.colorspace_settings.name = 'Non-Color'
            
for i in bpy.data.images:
    for tocken in ['rgh','rough','disp','dsp', 'dis', 'AO', 'occlusion', 'refl']:
        if tocken in bpy.path.display_name(i.filepath):
            i.colorspace_settings.name = 'Non-Color'
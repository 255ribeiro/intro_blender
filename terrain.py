import bpy
import numpy as np
from scipy.spatial import Delaunay


class OBJECT_OT_generate_terrain(bpy.types.Operator):
    bl_idname = "object.generate_terrain"
    bl_label = "Generate Terrain"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        # Initialize an empty list to store vertex coordinates
        points = []

        # Get selected objects in the scene
        selected_objects = context.selected_objects

        # Iterate through selected objects
        for obj in selected_objects:
            # Check if the object is a mesh
            if obj.type == 'MESH':
                # Ensure the object is active and in object mode'
                context.view_layer.objects.active = obj
                bpy.ops.object.mode_set(mode='OBJECT')

                # Get the mesh data
                mesh = obj.data
                
                # Collect vertex coordinates
                for vertex in mesh.vertices:
                    world_location = obj.matrix_world @ vertex.co
                    points.append(world_location)

        points = np.array(points)
        
        # Compute Delaunay triangulation
        tri = Delaunay(points[:,:2])

        # Create a new mesh
        mesh = bpy.data.meshes.new("terrain_mesh")
        
        # Assign vertices to the mesh
        mesh.from_pydata(points.tolist(), [], tri.simplices.tolist())
        
        # Update mesh geometry
        mesh.update()

        # Create a new object linked to the mesh
        obj = bpy.data.objects.new("terrain_3d", mesh)
        
        # Link the object to the scene
        scene = context.scene
        scene.collection.objects.link(obj)
        
        # Optionally, set the location of the object
        obj.location = (0, 0, 0)
        
        # Update the scene
        context.view_layer.update()

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(OBJECT_OT_generate_terrain.bl_idname, text="Generate Terrain")

### Step 2: Define the Panel



class OBJECT_PT_terrain_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_terrain_panel"
    bl_label = "Terrain Generator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_generate_terrain.bl_idname, text="Generate Terrain")

### Step 3: Register and Unregister the Addon

def register():
    bpy.utils.register_class(OBJECT_OT_generate_terrain)
    bpy.utils.register_class(OBJECT_PT_terrain_panel)
    bpy.types.VIEW3D_PT_tools_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_generate_terrain)
    bpy.utils.unregister_class(OBJECT_PT_terrain_panel)
    bpy.types.VIEW3D_PT_tools_object.remove(menu_func)

if __name__ == "__main__":
    

    register

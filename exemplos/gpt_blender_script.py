import bpy
import math
from mathutils import Matrix, Quaternion

def rotate_object_to_align_axis():
    # Check if an object is selected
    if bpy.context.object is None:
        print("Please select an object.")
        return

    # Get the active object
    obj = bpy.context.object

    # Check if the object has a mesh
    if obj.type != 'MESH':
        print("The selected object is not a mesh.")
        return

    # Check if a face is selected
    if bpy.context.face_select is False:
        print("Please select a face.")
        return

    # Get the selected face
    bm = bpy.context.object.data
    face = bm.polygons[bm.polygons.active]

    # Calculate the rotation matrix to align object's X-axis with face's Z-axis
    face_normal = face.normal.normalized()
    target_direction = mathutils.Vector((0, 0, 1))  # Target direction (Z-axis)
    rotation_axis = face_normal.cross(target_direction)
    rotation_angle = face_normal.angle(target_direction)

    # Align object's X-axis with face's Z-axis
    obj.rotation_euler = (rotation_angle, 0, rotation_axis[0], rotation_axis[1])

    # Rotate the object to align its Z-axis with global Z-axis
    z_axis_global = mathutils.Vector((0, 0, 1))
    z_axis_object = obj.rotation_euler.to_quaternion() @ Quaternion((0, 0, 1), 0)
    z_rot_quat = z_axis_object.rotation_difference(z_axis_global)
    obj.rotation_euler.rotate(z_rot_quat)

    # Update the scene
    bpy.context.view_layer.update()

# Run the function
rotate_object_to_align_axis()

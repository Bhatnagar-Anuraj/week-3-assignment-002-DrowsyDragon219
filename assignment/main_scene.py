import maya.cmds as cmds
import scene_functions as sf

cmds.file(new=True, force=True)

ground = cmds.polyPlane(name="ground", width=60, height=60,
                        subdivisionsX=1, subdivisionsY=1)[0]
"""This creates the ground plane."""
                        
"""I was going for a very angular geometric design here."""

sf.create_building(width=5, height=10, depth=5, position=(-10,0,20))
sf.create_building(width=5, height=10, depth=5, position=(-20,0,20))
sf.create_building(width=5, height=10, depth=5, position=(0,0,20))
sf.create_building(width=5, height=10, depth=5, position=(10,0,20))
sf.create_building(width=5, height=10, depth=5, position=(20,0,20))
"""This creates 5 buildings in a row."""

sf.create_tree(position=(-25, 0, 10))
sf.create_tree(position=(-25, 0, 5))
sf.create_tree(position=(-25, 0, 0))
sf.create_tree(position=(-25, 0, -5))
sf.create_tree(position=(-25, 0, -10))
"""This creates 5 trees in a row."""

sf.create_lamp_post(position=(25, 0, 10))
sf.create_lamp_post(position=(25, 0, 5))
sf.create_lamp_post(position=(25, 0, 0))
sf.create_lamp_post(position=(25, 0, -5))
sf.create_lamp_post(position=(25, 0, -10))
"""This creates 5 lamp posts in a row."""

sf.create_fence(length=12, post_count=7, position=(0, 0, 0))
"""This places a fence right in the middle of the scene."""

sf.place_in_circle(sf.create_tree, count=8, radius=10)
"""This places a bunch of trees in a circle."""

if __name__ == "__main__":
    cmds.viewFit(allObjects=True)
    print("Main scene built successfully!")

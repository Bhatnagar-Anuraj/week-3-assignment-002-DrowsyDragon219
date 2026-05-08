import maya.cmds as cmds

def create_building(width=4, height=8, depth=4, position=(0, 0, 0)):
    building = cmds.polyCube(width=width,height=height,depth=depth)[0]
    cmds.move(position[0],height/2,position[2],building)
    return building

def create_tree(trunk_radius=0.3, trunk_height=3, canopy_radius=2, position=(0, 0, 0)):
    trunk = cmds.polyCylinder(radius=trunk_radius,height=trunk_height)[0]
    cmds.move(0,trunk_height/2,0,trunk)
    canopy = cmds.polySphere(radius=canopy_radius)[0]
    canopy_y = trunk_height + canopy_radius
    cmds.move(0,canopy_y,0,canopy)
    tree = cmds.group(trunk,canopy, name="tree_group")
    cmds.move(position[0],position[1],position[2], tree)
    return tree
    
def create_fence(length=10, height=1.5, post_count=6, position=(0, 0, 0)):
        if post_count < 2: post_count = 2
        spacing = float(length) / (post_count - 1)
        fences = []
        for i in range(post_count):
            post = cmds.polyCube(width=0.1, height=height, depth=0.1, name="post#")[0]
            cmds.move(i*spacing,height,0, post)
            fences.append(post)
    rail = cmds.polyCube(width=length, height=0.1, depth=0.05, name="rail#")[0]
    cmds.move(length/2,height,0, rail)
    fences.append(rail)
    fence = cmds.group(fences, name="fence_group#")
    cmds.move(position[0],position[1],position[2], fence)
    return fence
    
def create_lamp_post(pole_height=5, light_radius=0.5, position=(0, 0, 0)):
    pole = cmds.polyCylinder(radius=0.2,height=pole_height)[0]
    cmds.move(0,pole_height/2,0, pole)
    light = cmds.polySphere(radius=light_radius)[0]
    cmds.move(0,pole_height+0.25,0, light)
    lamp = cmds.group(pole,light, name="lamp_group")
    cmds.move(position[0],position[1],position[2], lamp)
    return lamp

def place_in_circle(create_func, count=8, radius=10, center=(0, 0, 0),
                     **kwargs):
    results = []
    for i in range(count):
        angle = 2 * math.pi * i / count
        x = center[0] + radius * math.cos(angle)
        z = center[2] + radius * math.sin(angle)
        arrangement = create_func(position=(x, center[1], z), **kwargs)
        results.append(arrangement)

    return results

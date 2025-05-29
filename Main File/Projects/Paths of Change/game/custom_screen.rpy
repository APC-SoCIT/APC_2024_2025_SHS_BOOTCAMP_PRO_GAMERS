screen map:
    add "map/main.png"
    
    imagebutton:
        xpos 57
        ypos 55
        auto "map/state_1_%s.png"
        focus_mask True
        action NullAction()

    imagebutton:
        xpos 601
        ypos 119
        auto "map/state_2_%s.png"
        focus_mask True
        action NullAction()

    imagebutton:
        xpos 229
        ypos 257
        auto "map/state_3_%s.png"
        focus_mask True
        action NullAction()

screen state_1:
    add "map/state_1_idle.png" at truecenter zoom 1.5
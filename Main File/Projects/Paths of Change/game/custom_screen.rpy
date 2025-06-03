screen map:
    add "map/map.png"
    
    imagebutton:
        xpos 657
        ypos 555
        auto "map/state_1_%s.png"
        focus_mask True
        action Jump("fredintro")
        

    imagebutton:
        xpos 751
        ypos 9
        auto "map/state_2_%s.png"
        focus_mask True
        action NullAction()

    imagebutton:
        xpos 79
        ypos 137
        auto "map/state_3_%s.png"
        focus_mask True
        action NullAction()

    imagebutton:
        xpos 1269
        ypos 597
        auto "map/state_4_%s.png"
        focus_mask True
        action Jump("vinointro")

screen state_1:
    add "map/state_1_idle.png" at truecenter zoom 1.5
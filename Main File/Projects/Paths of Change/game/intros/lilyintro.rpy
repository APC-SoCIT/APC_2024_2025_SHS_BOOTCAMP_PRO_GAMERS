label lilyintro:

    if metLily == False:

        "jhdcvbgjkhsdvbhgfbhds"

        $ metLily = True

        if metFred == True and metKent == True and metVino == True and metLily == True:
            jump metAll

        else:
            call screen map
            
    elif metLily == True:

        jump lilyleft

label lilyleft:
    "Lily left the office"

    call screen map
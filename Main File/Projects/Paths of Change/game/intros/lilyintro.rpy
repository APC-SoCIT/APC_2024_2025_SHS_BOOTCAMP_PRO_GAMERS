label lilyintro:

    if metLily == False:

        "You take the elevator up to the guidance office to get some paperwork needed for new enrollees"

        "You knocked on the door of the guidance office only to be met with silence.... after a few seconds have passed you knock again but this time you tried peeking into the small window of the guidance office to see if there is anyone inside just as you were about to leave a face of girl peeked into the same window you were peeking at jumpscaring you a bit"

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

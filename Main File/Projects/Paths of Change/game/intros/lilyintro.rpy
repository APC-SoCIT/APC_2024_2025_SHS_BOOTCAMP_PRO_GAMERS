label lilyintro:

    if metLily == False:

        "You take the elevator up to the guidance office to get some paperwork needed for new enrollees"

        "You knocked on the door of the guidance office only to be met with silence.... after a few seconds have passed you knock again but this time you tried peeking into the 
        small window of the guidance office to see if there is anyone inside just as you were about to leave a face of girl peeked into the same window you were peeking at 
        jumpscaring you a bit"

        Unknown "Oh- I'm so sorry did I scare you? so sorry about that"

        "The girl sheepishly smiles. You notice that she is carrying lots of folders as well as pamphlets she reaches out her hand to you"

        Unknown "I'm really sorry about that. I'm Lily by the way and I do volunteer work here at the guidance office"

        "You shake her hand and you introduce yourself. She smiles brightly"

        Lily "Nice to meet you main are you here to apply for internships?"

        "You shake your head no"

        Lily "Oh- um- Are you here to do volunteer work?"

        "You shake your head no again"

        Lily "job application?"

        "You shake your head no again and before she continues asking you say"

        main "I'm just here to get some requirements from the councellor"

        "Lily looks slightly embarrassed as she got conscious"

        Lily "sorry I tend to ramble a lot... but um- the councellor's not here yet if you want you can wait inside the office so that 

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

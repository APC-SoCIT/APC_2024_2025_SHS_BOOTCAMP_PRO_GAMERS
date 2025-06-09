label kentintro:

    if metKent == False:

        scene bg black

        "You are headed towards your classroom, wandered a bit to find your seat number."

        "After finding your seat, you placed your belongings and sat down. There, you approached your seatmate and talked to him."

        scene bg class with dissolve

        main "Nice to meet you, my name is [mcName]. Let’s get along well, neighbor."

        show kent happy with dissolve

        Kent "Hi, nice to meet you. My name is Kent A. Ford. Let’s get along."

        "He was so pale, and his complexion looks concerning, you thought after looking at him."

        main "I am kinda new here so I would appreciate your company, if you don’t mind."

        show kent talk 

        Kent "You’re new here, huh? Sure, I don’t mind. Feel free, I have nothing better to do anyways."

        main "Thanks!"

        hide kent with dissolve

        scene bg black

        "You two talked a bit before the homeroom teacher arrived, and the classroom orientation started."

        "Lunchtime arrived as the orientation ended. You two met up in the hallway."

        scene bg hall

        show kent anxious with dissolve

        Kent "Hey, sorry but I won’t be able to accompany you for a bit since I have to do something real quick. Urgent thingy, trust."

        main "Oh, I see."

        main "Let’s talk later after you arrive then. For the meantime, I’ll wander around the school for a bit."

        show kent happy

        Kent "I see, then it’s settled. Really, sorry about this. Talk to you later."

        show kent huh

        Kent "By the way, just add me in social media. Just search up my name and it'll appear. Add me so that we can message each other."

        show kent bashful

        Kent "Bye now."

        "He said as he walks away in a rush."

        main "Yeah. Bye..."

        $ metKent = True

        if metFred == True and metKent == True and metVino == True and metLily == True:
            "After watching Kent dawdle around before walking away, [mcName] decided to head to the lobby"
            jump metAll

        else:
            call screen map

    elif metKent == True:

        jump kentleft
    
label kentleft:
    "Kent left the classroom"
    
    call screen map

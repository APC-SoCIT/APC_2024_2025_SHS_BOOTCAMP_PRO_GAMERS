label vinointro:

    if metVino == False:

        scene bg caf with dissolve

        "You look around to find a seat"

        main "Everywhere seems like it's full..."

        "As you look around, you lock eyes with someone calling you over"

        "You walk over there wondering who it is that called you"

        show vino neutral

        StudentV "Hey, you seem a bit lost."
        
        show vino talk

        StudentV "You need a place to sit?"

        main "Uhh yeah, though it looks like all the seats are taken..."

        StudentV "Then come over and sit with me, I'm not currently waiting on anyone."

        "You feel a bit uneasy meeting someone new"

        "Nevertheless, you still take the seat knowing all the others were taken"

        main "Oh sure, thanks."

        main "By the way, what's your name?"

        show vino smile

        Vino "You can call me Vino, I've been attending this school for a while now so if ever you need anything, you're always free to ask for my help"
        
        main "Thanks, I'm kinda having a hard time working my way around the school"

        show vino talk
        
        Vino "It's aight, you'll soon get the hang of it all"

        Vino "Anyways, should we go ahead and eat?"

        main "Sounds good"

        hide vino talk

        "You and Vino stood up to go get some food"

        "Not knowing where to go you just follow him and bought where he did"

        "Coming back to the seats, you and him talk for a while"

        main "So what are some stuff that you like to do?"

        show vino hmm

        Vino "Well I do love gardening and all that"

        Vino "I also sometimes do regular recycling around the park just to you know keep it clean"
        
        main "Oh that sounds nice, but why though?"

        main "Aren't there people who really clean those?"

        Vino "Well... yeah but they really don't clean it well and some students cause a mess throughout the day"

        show vino unamused

        Vino "It might seem like a hassle but it's just a small thing I can do to help"

        Vino "Our climate IS getting a bit worse each day so I love recycling and just helping around"

        main "That sounds great! I'm glad some people still care for our environment"

        main "It sounds interesting"

        main "I'd like to hear more about it sometimes!"

        show vino smile

        Vino "Of course! anytime"

        hide vino smile

        "Time passes and both are done eating"

        "You both stand up and are getting ready to leave"

        show vino smile

        Vino "Alright, it was good to meet you"
         
        Vino "I've got some stuff to do so I'll go ahead"

        main "Yea, it was nice meeting you too"

        hide vino smile

        main "I'll get going too, I've still got some things to do as well"
        scene bg lobby        
        $ metVino = True

        if metFred == True and metKent == True and metVino == True and metLily == True:
            "After waving bye to Vino, [mcName] decided to head to the lobby"
            jump metAll

        else:
            call screen map


    elif metVino == True:

        jump vinoleft
    
label vinoleft:
    scene bg caf with dissolve
    "Vino left the cafeteria"
    scene bg lobby with dissolve
    call screen map

    
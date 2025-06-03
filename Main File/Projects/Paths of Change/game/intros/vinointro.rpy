label vinointro:

    if metVino == False:

        "You look around to find a seat"

        main "Everywhere seems like it's full..."

        "As you look around, you lock eyes with someone calling you over"

        "You walk over there wondering who it is that called you"

        StudentV "Hey, you seem a bit lost."
        
        StudentV "You need a place to sit?"

        main "Uhh yeah, though it looks like all the seats are taken..."

        StudentV "Then come over and sit with me, I'm not currently waiting on anyone."

        "You feel a bit uneasy meeting someone new"

        "Nevertheless, you still take the seat knowing all the others were taken"

        main "Oh sure, thanks."

        main "By the way, what's your name?"

        Vino "You can call me Vino, I've been attending this school for a while now so if ever you need anything, you're always free to ask for my help"
        
        main "Thanks, I'm kinda having a hard time working my way around the school"
        
        Vino "It's aight, you'll soon get the hang of it all"

        Vino "Anyways, should we go ahead and eat?"

        main "Sounds good"

        "You and Vino stood up to go get some food"

        "Not knowing where to go you just follow him and bought where he did"

        "Coming back to the seats, you and him talk for a while"

        Vino "Alright, it was good to meet you"
         
        Vino "I've got some stuff to do so I'll go ahead"

        main "Yea, it was nice meeting you too"

        main "I'll get going too, I've still got some things to do as well"
        
        $ metVino = True

        call screen map

    elif metVino == True:

        jump vinoleft
    
label vinoleft:
    "Vino left the cafeteria"


    if all(metChars):
        jump metAll
    
    else:
        call screen map

    
label fredintro:

    if metFred == False:

        "You see a student walking around, near a bench."

        "His hair seems a bit scruffy while he’s scuffling a bunch of folders on his arm that seems like they’re about to slip off from his grip."

        "You also noticed that he has several pins on his lanyard. 3 of which look like custom-made pins of various characters, the other two are pins of pride flags that you are unfamiliar with."

        "He notices you staring at him as he tries to adjust his glasses and fix his collar."

        StudentF "Uhh, hi?"

        StudentF "Sorry, who are you?"

        main "Oh, hi. I’m sorta new to campus and I’m just checking the place out."

        "The student’s eyes immediately grew as a smirk began placing itself across his face. His awkward and confused expression immediately flipped to enthusiasm and confidence."

        StudentF "Oh, so you’re a freshman here. Happy to meet new RAMs!"

        Fred  "The name’s Fred, I came from the Senior High School batch from last year, so I kinda know the ropes around this place."

        Fred "Have you gotten a tour of campus yet? I would be glad to show you around"

        main "Yeah, I got a tour the first time I enrolled in here, was pretty surprised that the campus was this big."

        "Fred smiled as he picked up a bunch of the remaining folders from the bench, occasionally trying to support the bottom of the pile in hopes they don’t fall off"

        main "Do uhh…you need help with those? That’s a lot of files"
            
        Fred "Oh, don’t worry I’ve got a hold of them. I’ve carried more than this before"

        Fred "But I appreciate the offer."

        main "What are those for, anyways? Do you guys have a thesis defense or something?"

        "The student chuckled a bit after the last comment before organizing the folders and stuffing it in his backpack."

        Fred "No, nothing like that."

        Fred "Besides, it’s way too early in the semester to be having a thesis defense."

        Fred "I’m actually planning a bunch of events for this term, and our student’s activities office requires a bunch of files to be submitted for these events to be accepted."

        main "Oh, what kinda events?"

        Fred "Well, some events are for fun interactivity here on campus such as art events, seminars, booths, or small student parties."

        Fred "There’s a lot of events planned and I’m kind of trying to organize all of the ones I have under my belt."

        Fred "But what I’m particularly excited about are the Anti-Discriminatory Events planned for the next few months."

        main "Anti-Discriminatory Events?"

        "Fred’s eyes trailed to the side as if he’s trying to find the right words to give you."

        Fred "You know, racism, sexism, homophobia and transphobia, all that stuff."

        Fred "We’ve been having problems around here on campus with cases of bullying surrounding some students who are part of a minority. It’s starting to form a pattern"

        Fred "I, however, won’t stand that. Those idiots can’t find equality in anything even if it hit them in the face."

        "His tone soured as he talked about the situation. This is something you didn’t expect would happen from a campus such as this."

        "What more, you did not know that Fred’s mood shifts that easily."

        "For a second, he looks like your typical awkward student, then shifts to a cheery student body representative of some sort, then you realize he could be the school’s secret vigilante of justice."

        "Talk about cliche."

        "The bell suddenly bursts to life, leaving a high pitch ringing sound to echo throughout campus."

        "Fred jumps from the sudden loud noise as he frantically checked the time on his phone."

        Fred "Shoot! It’s already the first period, and I still need to get these papers to the Student’s Activities Office."

        Fred "I gotta go, it was nice meeting you stranger. I’ll see you around."

        Fred "You should probably head to your first class too. Don’t wanna be late for your first day on campus now, wouldn’t ya?"

        "And with that, Fred ran to the building in a hurry, casually almost stumbling on the pavement from his hasty footsteps."

        $ metFred = True

        call screen map

    elif metFred == True:

        jump fredleft
    
label fredleft:
    "Fred left"

    if all(metChars):
        jump metAll
    
    else:
        call screen map

    

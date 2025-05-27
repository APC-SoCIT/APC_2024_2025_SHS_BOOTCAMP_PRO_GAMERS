label joshroute:
        
    "You follow Josh to the main building’s 3rd Floor. Home of the Senior High School students and the School Activities Office."

    "He guides you towards a classroom parallel across the stairs. You can view the classroom from the outside via the window on their door"

    "Josh opens the door to an airconditioned room filled with paperwork, props, and an array of files scattered throughout the tables"

    "The classroom had at least 5-6 students working inside. Mountains of papers were stacked on top of each other like a game of Jenga as different students type away at their laptops"

    Josh "Welcome to Classroom 307, A.K.A my team’s workspace"

    Josh "....well, for about 3 hours a day after class hours, hehe"

    main "What did you bring me here for again?"

    Josh "Oh yeah, you wanted to know more about what I do around the school, didn’t ya?"

    main "Well I mean..yeah, but I didn’t really expect THIS"

    main "You have an entire room dedicated to your extracurriculars specifically"

    main "Well, what can I say? I like to drown myself in work sometimes"

    RandomStudent "THAT’S NOT TRUE, HE CRASHES OUT A LOT"

    Josh "...?!"

    Josh "I only crash out when things get overwhelming, you know, like Valid. Normal. PEOPLE."

    Josh "Anyways, this room is dedicated to a bunch of stuff actually"

    Josh "I work with the School’s class leaders, I host events, I run an art organization, the list goes on"

    "Josh gives you a bright smile that’s enough to light up the entire classroom as he rests his arm on a table…."

    "....which he then stumbles, almost knocking an entire pile of student activities documents off of its pristine stack"

    main "Are you uhhm.…ok?"

    Josh "Never better!"

    "Josh adjusts his stance and fixes the papers back to its stack"

    "He proceeds to open his bag and pulls out another file filled with papers stapled neatly together"

    Josh "I’m hosting another event about Equality Awareness, and I’m struggling to find for a second host"

    "Josh hands you a flier for the upcoming event, the poster shows the face of the speaker for the seminar: A bald man with a suit and tie with a picture perfect smile."

    "The poster has the caption ‘International Awareness’ on bold as different symbols surround the picture of the speaker. You can easily notice what some of them represent"

    "A female symbol for Empowering Women, A rainbow flag for LGBTQ+ Rights, An infinity symbol for representing Autism, A silhouette of a fist for Black Lives, A Green Ribbon symbolizing Mental Health"

    "And some other symbols you don’t know"

    Josh "I really commend the efforts to spread awareness this school does to certain minorities. So when I found out the school was holding a seminar for it, it was a pretty huge deal for me."

    Josh "Apparently, this seminar is a pretty big deal cuz many of the school heads endorsed this event so they expect it to perform really well"

    Josh "And that’s why I volunteered to host this event alongside the speaker!"

    Josh "Sadly, they require at least two hosts for the event and I haven’t had any luck with finding a second host"

    main "Why can’t they just let one host run the event?"

    main "I mean by the looks of it, you’re really capable of running this whole show solo"

    "Josh perks up to your comment as a smile that he can’t seem to stop slide onto his face"

    Josh "Thanks! I’ve been trying to pull some strings behind this event but I can’t seem to convince the event organizer to let me host on my own"

    Josh "Something about ‘needing someone to balance my energy’ or something. No clue what that means, but whatever"

    "Suddenly, something inside his head sparks as he looks up at you with stars in his eyes, filling him with hope"

    Josh "Hey, I know you’re new to this school and all, and I really do apologize for suddenly dropping this on you, but would you be willing to be my second host?"

    main "Wh- Me?? Hosting?"

    main "I dunno, Josh…I mean I don’t really have any prior knowledge to host events. I struggle talking to a group of people, what more the entire school?"

    main "Plus, I’ve barely been here for a day and pulling a new kid to the frame for a very important event seems pretty risky"

    "Josh’s mood dies down as he seems defeated, staring at the corner of the room as his soul was sucked out of him"

    Josh "I know, I know"

    Josh "But I can take you under my wing, teach you everything I know, I just really need someone to back me up for the event"

    Josh "I know this is a lot for me to ask, but would you be interested in being my second host?"

    main "I…I uhmmm…"

label Joshchoice:

    main "What do I say?"

menu:

    "I can't be your second host...":

        "WARNING: This option will abort Josh’s route completely"

        "Do you wish to proceed?"

        menu:
            "Yes":
                jump abortroute
            "No":
                jump Joshchoice
    
    "I can help you out":
        jump continueroute

label abortroute:

    main "I’m really sorry Josh, but I don’t think I’m cut out for being a host"

    "Josh seems very distraught from your response and can only let out a deep disappointed sigh"

    Josh "That’s alright. Thanks for considering it though"

    Josh "I guess I’ll try to find for someone else to help me host the event"

    main "Will you be alright though? Seems like it’s been stressing you out for quite a while now"

    Josh "I’ve survived worse"

    Josh "I guess I’ll be doing some paperwork in the meantime, but thanks for swinging by. I’ll see you around"

    "You walk out of the classroom with a hint of guilt seeing the guy all disappointed."

    "But as he said, he’s been through worse."

    "You shrug off the uneasy feeling of guilt off of you and decide to set on a next course of action"

    main "Who should I go with?"

    #add an option where you choose Gian, Remie, or Alf
    return

    

label continueroute:

    main "Well, I guess I can give it a shot-"

    Josh "REALLY?!"

    Josh "I’m glad you came to your senses"

    Josh "Don’t worry, I’ll be a great teacher!"

    main "Well…I-"

    "Before you could finish your sentence, Josh drags you to a corner of the room with a whiteboard stand filled with a bunch of topics jotted down on the board"

    "There also seems to be a bunch of sticky notes scattered around the board to add extra bits of information"

    Josh "As you can see here, I’ve laid out each and every bit of information regarding the discussion we’ll be having on the seminar"

    Josh "With a bit of help, I’ve gotten access to the powerpoint presentation of the presenter and decided to write down all the necessary main points the speaker pointed out"

    main "Hold on hold on, slow down there, Josh"

    main "This seems like a lot of stuff to take in, I thought I was just gonna help you on hosting, not presenting or whatever"

    "Josh blinked at you in response, waiting for his brain to load in the correct words to tell you."

    Josh "This is part of hosting."

    Josh "As a host, it is our job to know the ins and outs of the speaker’s presentation to be able to control the flow of the event and maintain a smooth and interactive experience for the audience!"

    Josh "Isn’t that fun"

    main "No, not really. It’s pretty boring if I’m being honest."

    "The student before you frowned as he pouted his lips at you with a look in his eye that seems like a disappointed mother would give to her kids"

    Josh "Don’t be such a stick-up, this is the joy of hosting. I promise, you’ll love it when we’re on stage"

    Josh "Plus, we’ve got some time to kill. Might as well start with teaching you the basics of the different minorities and their relation in a school setting"

    main "Well, I mean, this does seem like it’ll help me with my future social science classes."

    main "Alright, I’m in"

    Josh "Great! Let’s start with-"

    "BANG BANG BANG"

    "Heavy knocking was heard from the door, leaving the entire room silent as all of your eyes darted towards the source of the sound"

    "You look back at Josh whose mood completely soured like food left out in the sun for too long."

    Josh "Ugh, not him again"

    main "Who?"

    Josh "Chad, one of the student school leaders and an absolute headache"

    Josh "He comes knocking on our door every so often to collect a bunch of papers from me for certain events but does it in the most brute-force way possible"

    main "What’s his deal"

    Josh "Think of the world’s most generic high-school bully, now imagine that and let it manifest and boom you have him."

    Josh "I don’t know how this guy got in the student leaders roster, but by god, do I despise him, and I think the feeling is mutual"

    Josh "I’ll deal with this. Everyone just continue what you’re doing"

    "Josh rolls his eyes as he takes a deep sigh and walks to the door"

    "From the corner of Josh’s figure, you could see another student towering above Josh with an estimated height of about 6’3ft, compared to Josh’s 5’4 stature"

    "The student was wearing a typical red varsity jacket and denim pants. He was a brunette with a more lean and bulky body type. The embodiment of a typical Jock."

    Josh "What is it this time, Cha-"

    Josh "OOF- HEY"

    "The other student pushes Josh to the side with ease as he makes his way in the classroom."

    "His eyes trails around as he examines all the paperwork stacked everywhere. He then looks back at Josh with the other completely glaring daggers into the other man’s soul"

    Chad "This is what you call a student head’s office? What a joke"

    Josh "Well sorry, I’m not a Nepo-baby to get all the great stuff you guys got going on at the top floor"

    Chad "Enough talk from you, boykisser. At least I don’t run an org dedicated to your artsy autistic fantasies"

    "Josh’s eyes bore holes hot enough to penetrate deep inside Chad’s skull. His fist clenched as a murderous look was slowly making its way onto his face"

    "But as quick as he was to anger, his demeanor quickly took a recovering point as he took a deep breath and sighed, relaxing himself."

    Chad "Where’s the papers I asked for? I sent you the templates last week"

    Josh "APFs and lists of event Agendas take time to prepare, Chad"

    Josh "Maybe that’s why most of your events end up in flames"

    Chad "Speak up? Couldn’t hear you from all the way up here, shortstack"

    Josh "Nothing, I said you are so great my awe-inspiring student leader king"

    Josh "Oh, and if you must know, I already gave the documents you needed to your organization advisor."

    Josh "Next time, find for a valid reason to come barging in on us instead of spewing derogatory insults"

    "Ignoring Josh, Chad shoves him once again to the side completely muting out Josh’s voice from his head"

    "Chad makes a 180 and slams the door, making a reverberated echo through the halls"

    main "God, what’s his deal?"

    Josh "Don’t know, don’t care. If I try to stoop to his level, that doesn’t make me better than him, now, does it?"

    "Josh sighs tiringly as he drags himself back towards the whiteboard"

    "He quickly attempts to spiff himself up and shake off the negativity brought to the room from the sudden outburst of the other student"

    Josh "Anyways, back to hosting!"

    Josh "Before we can get into hosting an event, I’d like to test your knowledge on the different types of discrimination"

    main "Wait what"

    main "You never told me I had to be quizzed"

    Josh "Oh come on main , it’s not like it’s graded or anything"

    main "Yeah, but you could’ve at least given me a heads up or something"

    main "Plus you said this was a hosting gig, so I expected more hosting and less uhh….studying?"

    Josh "Well, I did mention that to be a host, you must first be familiarized with the topic of the hosting event, didn’t I?"

    main "Well, yeah but-"

    Josh "Alrighty then let’s get started!"

    "You stifle a sigh and an eyeroll in which Josh cheerfully ignores"

    "Josh immediately brings out a stack of flashcards from a nearby drawer that seems to be a stack of notes and a bunch of pictures stapled together to form what seems to be an index card of info"

    "The cards had students’ names written on the top with different pictures from what seemed to be separate incidents on the cards’ left side"

    "There was also a wall of information on them pertaining to each incident"

    "These cards seem to be mini-crafted files"

    Josh "Throughout the years, we’ve had different cases of discrimination against students that fall under a certain minority"

    Josh "These cases have already been issued to the school board so the student cases on these cards have been resolved with the higher ups"

    Josh "I jotted down a bunch of notes from their pre-existing records because I sensed a pattern in some of these incidents"

    main "Ok that’s cool and all but like, what does this have to do with hosting again?"

    Josh "main , this is more than just hosting; It’s about familiarizing yourself with the early signs of a discriminatory act against students"

    Josh "If you’ve ever been in their shoes, it really hurts to be shunned away because of the school’s bullying problem"

    Josh "Trust me I know"

    Josh "That’s why hosting this event is such a big deal for those students"

    main "Alright, alright, I’ll read the cases"

    "main groans as he swiped 3 cards from Josh’s hands"

    main "{i}What did I get myself into?{/i}"

    Josh "I’ll help you with the cases as you go through them. I want you to find a common ground stemming from these problems"
    jump cardsection

label cardsection:

    $ chosen = []
    menu cards:
        set chosen
        "Pick a card"
        " Card labelled \"Jones Cooper\" ":
            Josh "Ah, Jones"
            Josh "Jones was your typical jock part of our school’s varsity running for a scholarship for his upcoming college years"
            Josh "However, one of his football teammates found out that he had a crush on one of the guys in their team"
            Josh "So they decided to call him queer slurs and make fun of him for liking guys"
            main "Geez…poor guy"
            main "What happened afterwards?"

            Josh "After incidents of the football team trashing his locker with queer slurs painted in graffiti, that was the last straw and he quit the team"
            Josh "The cases were reported to the Discipline Office and our varsity team’s games were upheld due to their delinquency"
            Josh "—deserved if you ask me"
            Josh "After that, Jones decided to move to a different school after his graduation to avoid anymore torment from the varsity team"

            main "Yikes…"

            Josh "The varsity team targeted him for being an {i}easy target{/i} since he was considered as the team’s rookie"
            Josh "Rookie or not though, Jones could’ve physically beaten them up, but chose to endure their attacks against him instead"

            main "Well I guess he knew how to choose his battles then"
            main "How’s he doing now?"

            Josh "He’s doing fine, so I’ve heard"
            Josh "He enrolled in a university with a much bigger campus than ours"
            Josh "Heard he’s got a boyfriend there too"

            main "Huh, good for him"

            jump cards

        "Card labelled \"Byeong-Yeon\" ":
            Josh "Bon"
            jump cards

        "Card labelled \"Chica Palmer\" ":
            Josh "Somewhere else."
            jump cards

    Josh "Now that you've reviewed all the cards, let's see if you saw the pattern"

    return



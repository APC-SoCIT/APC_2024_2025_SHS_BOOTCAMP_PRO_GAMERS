label fredroute:
        
    "You follow Fred to the main building’s 3rd Floor. Home of the Senior High School students and the School Activities Office."

    "He guides you towards a classroom parallel across the stairs. You can view the classroom from the outside via the window on their door"

    "Fred opens the door to an airconditioned room filled with paperwork, props, and an array of files scattered throughout the tables"

    "The classroom had at least 5-6 students working inside. Mountains of papers were stacked on top of each other like a game of Jenga as different students type away at their laptops"

    Fred "Welcome to Classroom 307, A.K.A my team’s workspace"

    Fred "....well, for about 3 hours a day after class hours, hehe"

    main "What did you bring me here for again?"

    Fred "Oh yeah, you wanted to know more about what I do around the school, didn’t ya?"

    main "Well I mean..yeah, but I didn’t really expect THIS"

    main "You have an entire room dedicated to your extracurriculars specifically"

    main "Well, what can I say? I like to drown myself in work sometimes"

    RandomStudent "THAT’S NOT TRUE, HE CRASHES OUT A LOT"

    Fred "...?!"

    Fred "I only crash out when things get overwhelming, you know, like Valid. Normal. PEOPLE."

    Fred "Anyways, this room is dedicated to a bunch of stuff actually"

    Fred "I work with the School’s class leaders, I host events, I run an art organization, the list goes on"

    "Fred gives you a bright smile that’s enough to light up the entire classroom as he rests his arm on a table…."

    "....which he then stumbles, almost knocking an entire pile of student activities documents off of its pristine stack"

    main "Are you uhhm.…ok?"

    Fred "Never better!"

    "Fred adjusts his stance and fixes the papers back to its stack"

    "He proceeds to open his bag and pulls out another file filled with papers stapled neatly together"

    Fred "I’m hosting another event about Equality Awareness, and I’m struggling to find for a second host"

    "Fred hands you a flier for the upcoming event, the poster shows the face of the speaker for the seminar: A bald man with a suit and tie with a picture perfect smile."

    "The poster has the caption ‘International Awareness’ on bold as different symbols surround the picture of the speaker. You can easily notice what some of them represent"

    "A female symbol for Empowering Women, A rainbow flag for LGBTQ+ Rights, An infinity symbol for representing Autism, A silhouette of a fist for Black Lives, A Green Ribbon symbolizing Mental Health"

    "And some other symbols you don’t know"

    Fred "I really commend the efforts to spread awareness this school does to certain minorities. So when I found out the school was holding a seminar for it, it was a pretty huge deal for me."

    Fred "Apparently, this seminar is a pretty big deal cuz many of the school heads endorsed this event so they expect it to perform really well"

    Fred "And that’s why I volunteered to host this event alongside the speaker!"

    Fred "Sadly, they require at least two hosts for the event and I haven’t had any luck with finding a second host"

    main "Why can’t they just let one host run the event?"

    main "I mean by the looks of it, you’re really capable of running this whole show solo"

    "Fred perks up to your comment as a smile that he can’t seem to stop slide onto his face"

    Fred "Thanks! I’ve been trying to pull some strings behind this event but I can’t seem to convince the event organizer to let me host on my own"

    Fred "Something about ‘needing someone to balance my energy’ or something. No clue what that means, but whatever"

    "Suddenly, something inside his head sparks as he looks up at you with stars in his eyes, filling him with hope"

    Fred "Hey, I know you’re new to this school and all, and I really do apologize for suddenly dropping this on you, but would you be willing to be my second host?"

    main "Wh- Me?? Hosting?"

    main "I dunno, Fred…I mean I don’t really have any prior knowledge to host events. I struggle talking to a group of people, what more the entire school?"

    main "Plus, I’ve barely been here for a day and pulling a new kid to the frame for a very important event seems pretty risky"

    "Fred’s mood dies down as he seems defeated, staring at the corner of the room as his soul was sucked out of him"

    Fred "I know, I know"

    Fred "But I can take you under my wing, teach you everything I know, I just really need someone to back me up for the event"

    Fred "I know this is a lot for me to ask, but would you be interested in being my second host?"

    main "I…I uhmmm…"

label Fredchoice:

    main "What do I say?"

menu:

    "I can't be your second host...":

        "WARNING: This option will abort Fred’s route completely"

        "Do you wish to proceed?"

        menu:
            "Yes":
                jump abortfredroute
            "No":
                jump Fredchoice
    
    "I can help you out":
        jump continuefredroute

label abortfredroute:

    main "I’m really sorry Fred, but I don’t think I’m cut out for being a host"

    "Fred seems very distraught from your response and can only let out a deep disappointed sigh"

    Fred "That’s alright. Thanks for considering it though"

    Fred "I guess I’ll try to find for someone else to help me host the event"

    main "Will you be alright though? Seems like it’s been stressing you out for quite a while now"

    Fred "I’ve survived worse"

    Fred "I guess I’ll be doing some paperwork in the meantime, but thanks for swinging by. I’ll see you around"

    "You walk out of the classroom with a hint of guilt seeing the guy all disappointed."

    "But as he said, he’s been through worse."

    "You shrug off the uneasy feeling of guilt off of you and decide to set on a next course of action"

    main "Who should I go with?"

    menu:
        "Message Kent to hang out":
            jump kentroute
        "Head to Lily's Office":
            jump lilyroute
        "Go to the park where Vino resides":
            jump vinoroute

    

label continuefredroute:

    main "Well, I guess I can give it a shot-"

    Fred "REALLY?!"

    Fred "I’m glad you came to your senses"

    Fred "Don’t worry, I’ll be a great teacher!"

    main "Well…I-"

    "Before you could finish your sentence, Fred drags you to a corner of the room with a whiteboard stand filled with a bunch of topics jotted down on the board"

    "There also seems to be a bunch of sticky notes scattered around the board to add extra bits of information"

    Fred "As you can see here, I’ve laid out each and every bit of information regarding the discussion we’ll be having on the seminar"

    Fred "With a bit of help, I’ve gotten access to the powerpoint presentation of the presenter and decided to write down all the necessary main points the speaker pointed out"

    main "Hold on hold on, slow down there, Fred"

    main "This seems like a lot of stuff to take in, I thought I was just gonna help you on hosting, not presenting or whatever"

    "Fred blinked at you in response, waiting for his brain to load in the correct words to tell you."

    Fred "This is part of hosting."

    Fred "As a host, it is our job to know the ins and outs of the speaker’s presentation to be able to control the flow of the event and maintain a smooth and interactive experience for the audience!"

    Fred "Isn’t that fun"

    main "No, not really. It’s pretty boring if I’m being honest."

    "The student before you frowned as he pouted his lips at you with a look in his eye that seems like a disappointed mother would give to her kids"

    Fred "Don’t be such a stick-up, this is the joy of hosting. I promise, you’ll love it when we’re on stage"

    Fred "Plus, we’ve got some time to kill. Might as well start with teaching you the basics of the different minorities and their relation in a school setting"

    main "Well, I mean, this does seem like it’ll help me with my future social science classes."

    main "Alright, I’m in"

    Fred "Great! Let’s start with-"

    "BANG BANG BANG"

    "Heavy knocking was heard from the door, leaving the entire room silent as all of your eyes darted towards the source of the sound"

    "You look back at Fred whose mood completely soured like food left out in the sun for too long."

    Fred "Ugh, not him again"

    main "Who?"

    Fred "Chad, one of the student school leaders and an absolute headache"

    Fred "He comes knocking on our door every so often to collect a bunch of papers from me for certain events but does it in the most brute-force way possible"

    main "What’s his deal"

    Fred "Think of the world’s most generic high-school bully, now imagine that and let it manifest and boom you have him."

    Fred "I don’t know how this guy got in the student leaders roster, but by god, do I despise him, and I think the feeling is mutual"

    Fred "I’ll deal with this. Everyone just continue what you’re doing"

    "Fred rolls his eyes as he takes a deep sigh and walks to the door"

    "From the corner of Fred’s figure, you could see another student towering above Fred with an estimated height of about 6’3ft, compared to Fred’s 5’4 stature"

    "The student was wearing a typical red varsity jacket and denim pants. He was a brunette with a more lean and bulky body type. The embodiment of a typical Jock."

    Fred "What is it this time, Cha-"

    Fred "OOF- HEY"

    "The other student pushes Fred to the side with ease as he makes his way in the classroom."

    "His eyes trails around as he examines all the paperwork stacked everywhere. He then looks back at Fred with the other completely glaring daggers into the other man’s soul"

    Chad "This is what you call a student head’s office? What a joke"

    Fred "Well sorry, I’m not a Nepo-baby to get all the great stuff you guys got going on at the top floor"

    Chad "Enough talk from you, boykisser. At least I don’t run an org dedicated to your artsy autistic fantasies"

    "Fred’s eyes bore holes hot enough to penetrate deep inside Chad’s skull. His fist clenched as a murderous look was slowly making its way onto his face"

    "But as quick as he was to anger, his demeanor quickly took a recovering point as he took a deep breath and sighed, relaxing himself."

    Chad "Where’s the papers I asked for? I sent you the templates last week"

    Fred "APFs and lists of event Agendas take time to prepare, Chad"

    Fred "Maybe that’s why most of your events end up in flames"

    Chad "Speak up? Couldn’t hear you from all the way up here, shortstack"

    Fred "Nothing, I said you are so great my awe-inspiring student leader king"

    Fred "Oh, and if you must know, I already gave the documents you needed to your organization advisor."

    Fred "Next time, find for a valid reason to come barging in on us instead of spewing derogatory insults"

    "Ignoring Fred, Chad shoves him once again to the side completely muting out Fred’s voice from his head"

    "Chad makes a 180 and slams the door, making a reverberated echo through the halls"

    main "God, what’s his deal?"

    Fred "Don’t know, don’t care. If I try to stoop to his level, that doesn’t make me better than him, now, does it?"

    "Fred sighs tiringly as he drags himself back towards the whiteboard"

    "He quickly attempts to spiff himself up and shake off the negativity brought to the room from the sudden outburst of the other student"

    Fred "Anyways, back to hosting!"

    Fred "Before we can get into hosting an event, I’d like to test your knowledge on the different types of discrimination"

    main "Wait what"

    main "You never told me I had to be quizzed"

    Fred "Oh come on main , it’s not like it’s graded or anything"

    main "Yeah, but you could’ve at least given me a heads up or something"

    main "Plus you said this was a hosting gig, so I expected more hosting and less uhh….studying?"

    Fred "Well, I did mention that to be a host, you must first be familiarized with the topic of the hosting event, didn’t I?"

    main "Well, yeah but-"

    Fred "Alrighty then let’s get started!"

    "You stifle a sigh and an eyeroll in which Fred cheerfully ignores"

    "Fred immediately brings out a stack of flashcards from a nearby drawer that seems to be a stack of notes and a bunch of pictures stapled together to form what seems to be an index card of info"

    "The cards had students’ names written on the top with different pictures from what seemed to be separate incidents on the cards’ left side"

    "There was also a wall of information on them pertaining to each incident"

    "These cards seem to be mini-crafted files"

    Fred "Throughout the years, we’ve had different cases of discrimination against students that fall under a certain minority"

    Fred "These cases have already been issued to the school board so the student cases on these cards have been resolved with the higher ups"

    Fred "I jotted down a bunch of notes from their pre-existing records because I sensed a pattern in some of these incidents"

    main "Ok that’s cool and all but like, what does this have to do with hosting again?"

    Fred "main , this is more than just hosting; It’s about familiarizing yourself with the early signs of a discriminatory act against students"

    Fred "If you’ve ever been in their shoes, it really hurts to be shunned away because of the school’s bullying problem"

    Fred "Trust me I know"

    Fred "That’s why hosting this event is such a big deal for those students"

    main "Alright, alright, I’ll read the cases"

    "main groans as he swiped 3 cards from Fred’s hands"

    main "{i}What did I get myself into?{/i}"

    Fred "I’ll help you with the cases as you go through them. I want you to find a common ground stemming from these problems"
    jump cardsection

label cardsection:

    $ chosen = []
    menu cards:
        set chosen
        "Pick a card"
        " Card labelled \"Jones Cooper\" ":
            Fred "Ah, Jones"
            Fred "Jones was your typical jock part of our school’s varsity running for a scholarship for his upcoming college years"
            Fred "However, one of his football teammates found out that he had a crush on one of the guys in their team"
            Fred "So they decided to call him queer slurs and make fun of him for liking guys"

            main "Geez…poor guy"
            main "What happened afterwards?"

            Fred "After incidents of the football team trashing his locker with queer slurs painted in graffiti, that was the last straw and he quit the team"
            Fred "The cases were reported to the Discipline Office and our varsity team’s games were upheld due to their delinquency"
            Fred "—deserved if you ask me"
            Fred "After that, Jones decided to move to a different school after his graduation to avoid anymore torment from the varsity team"

            main "Yikes…"

            Fred "The varsity team targeted him for being an {i}easy target{/i} since he was considered as the team’s rookie"
            Fred "Rookie or not though, Jones could’ve physically beaten them up, but chose to endure their attacks against him instead"

            main "Well I guess he knew how to choose his battles then"
            main "How’s he doing now?"

            Fred "He’s doing fine, so I’ve heard"
            Fred "He enrolled in a university with a much bigger campus than ours"
            Fred "Heard he’s got a boyfriend there too"

            main "Huh, good for him"

            jump cards

        "Card labelled \"Byeong-Yeon\" ":
            Fred "Oh, its Byeong-Yeon"
            Fred "He was a korean student in Band, I’m pretty sure he was an exchange student from Seoul"
            Fred "The guy could barely speak English and was still adjusting to the school’s environment but he was a bit shy for the most part"
            Fred "His case of discrimination was when people started calling him names because of his Korean nationality"
            Fred "He basically started breaking down in a bathroom once because of the cruel jokes the other students were making"

            main "What kind of cruel jokes"
            
            Fred "Oh you know, typical stereotypes yada-yada. The joke got so bad once that a bunch of students managed to lure him on stage in front of the entire Senior High district and started playing K-Pop"
            Fred "Then they were shouting chants and telling him to dance"

            main "Public humiliation…yikes"

            Fred "I don’t remember exactly how the case was resolved, but it ended up with the guy having to take remote classes online instead of being onsite due to the jokes he had to deal with"
            Fred "I mean, the guy was practically jumped on by a group of bullies in his class. Can’t say I exactly blame him"

            main "What happened to the bullies though? Does the school do anything about this or do the students just endure this"

            Fred "...."
            Fred "That's the thing,"
            Fred "Byeong-Yeon's case was so widespread that the school wasn't able to pinpoint a direct perpetrator"
            Fred "Even he couldn't point fingers cuz usually he would get ganged up by a bunch of people"
            Fred "Says alot about our school, huh?"
            
            main "Man, the poor guy though...I'm glad he's doing alright"

            Fred "Yeah, I'd like to say something about our school's discipline office, but even they're too tired to deal with this problem"
            Fred "Really sucks what Byeong-Yeon went through"

            jump cards


        "Card labelled \"Chica Palmer\" ":
            Fred "Chica Palmer..."
            Fred "Her case was...something"

            main "What happened to her?"

            Fred "She used to be part of a religious group that used to do bible study every Sunday"
            Fred "But then she was diagnosed with a case of ADHD and Autism"
            Fred "The people who ran the bible study used to be adults from church who also happened to be associates of the school"
            Fred "And when they found out about this, they started praying for Chica, hoping her 'problem' would go away with God's power"

            main "Were they-"

            Fred "Conservative? Yes."
            Fred "They believed that Chica's neurological problems was solvable with enough praying"
            Fred "Chica felt a bit uncomfy with how they viewed her so she opted to 'take a break' from that bible study"
            Fred "However, word got out about her neurological problems and a specific group of boys started calling her names like \"Tism\" or something"
            Fred "What's worse is that boy group had her crush in it"
            Fred "She felt so ashamed that she didn't want to show her face to school anymore"

            main "How did the guidance office catch wind of this?"
            main "I'm sure she had someone to back her up at least"

            Fred "She did, until her friends graduated and she was left to fend for herself"
            Fred "She didn't have any friends her level so that left her defenseless"
            Fred "The bullying stopped once the guidance office caught up with them"
            Fred "Surprisingly, they also supported Chica with therapy to help her gain the confidence and to recover from the bullying"
            Fred "Thankfully her case was solved and she's doing fine nowadays"

            main "That's a relief"

            jump cards

    main "Wow....this is a lot to take in"
    main "This feels like I'm peering into to much personal stuff"

    Fred "Sometimes, incidents like these tend to bring out a lot of personal information about a person and their life"
    Fred "Sometimes they're things you least expect"
    Fred "It's a bit disappointing cases like these in school tend to pop up"
    Fred "But I'm glad there's a few people who are willing to help out those in need"
    Fred "Moving on, now that you viewed all of the cases, let's move onto the quiz part of your training"
    
    main "Do I have to?"

    Fred "Hush"
    Fred "There will be a total of 5 questions and all you gotta do is answer them right"
    Fred "Are you ready?"

menu:
    "Yes":
        "Now that's what I'm talkin' about, let's go"
        jump questions

    "No":
        Fred "Too late, already whipping out the questions"
        Fred "Get Ready"
        jump questions

label questions:

    default wrong = 0

    Fred "Ok, first things first. What did all students, aside from being discriminated, have in common"
    Fred "Don't worry about this one, there isn't a wrong answer, I just want your honest viewpoint on it"

    label question1:
        menu:
            "The students were overpowered by a certain group":
                Fred "That is true"
                Fred "All 3 cases included a group of students ganging up on them"
                Fred "Honestly makes me think"
                jump q2
            "The students did not have anyone to back them up":
                Fred "Hmm, I like your viewpoint on that"
                Fred "The problem with discrimination is it can sometimes be a silent or messy fight"
                Fred "Such as these students, it wasn't easy for them to reach out for help"
                "Fred sighs disappointingly"
                Fred "Let alone anyone outside reaching out to help them"
                jump q2
            "The perpetrators think highly of themselvess":
                Fred "Yeah, well that's life for ya"
                Fred "One day you're just vibing, and the next, someone jumps at you for existing"
                Fred "In discrimination, usually the abuser or offender's way of reason is that"
                jump q2
            "Chad.":
                Fred "Chad literally is out in the picture with any of these cases"
                Fred "Buttttt... he is a huge pain in the ass"
                Fred "Still, not the answer I was looking for"
                Fred "Try again, dude"
                $ wrong = wrong + 1
                jump question1

    label q2:
        Fred "Ok, ok, let's get a bit more technical here."
        Fred "That first question was just a test of opinion"
        Fred "Question 2: What is the best way to deal with discrimination, shown by the 3 cases you've read"
        
        label question2:
            menu:
                "Find the source and stop it":
                    Fred "That may be right depending on someone's morals, but it really isn't advised to do so"
                    Fred "No matter how annoying and pressuring it can get, you don't throw a fist to another fist"
                    Fred "Unless, only when needed. Heh..."
                    $ wrong = wrong + 1
                    jump q3
                "Ignore the torment, they'll get tired eventually":
                    Fred "Sorry [mcName], that's not the right answer"
                    Fred "Ignorance is a band-aid solution and will only prolong the bullying"
                    Fred "What's worse, it could deepen the situation the victim is in"
                    $ wrong = wrong + 1
                    jump q3
                "Provide full support for the discriminated in overcoming prejudice and provide a safe space":
                    Fred "Nice one!"
                    Fred "It's best to remember the best way to deal with victims of prejudice is to assure them that they are not alone"
                    Fred "Support is the best weapon against Derogatory nitwits"
                    jump q3
                "Immediately report the instance of discrimination to a higher position in-charge":
                    Fred "While that is true..."
                    Fred "Sad to say that the higher ups don't really care sometimes"
                    Fred "I mean, yeah they'd do something to punish the perpetrators, but uhhh that's it."
                    $ wrong = wrong + 1
                    jump q3

    label q3:
        Fred "Ok, that one was easy, let's try to test your memory"
        Fred "Out of the three cases, which of them was publicly humiliated?"

        label question3:
            menu:
                "Jones Cooper":
                    Fred "Heh...sorry bud, wrong answer"
                    $ wrong = wrong + 1
                "Byeong-Yeon":
                    Fred "Heh...sorry bud, wrong answer"
                    $ wrong = wrong + 1
                "Chica Palmer":
                    Fred "Heh...sorry bud, wrong answer"
                    $ wrong = wrong + 1
                "None of the above":
                    Fred "...."
                    Fred "Seriously?"
                    $ wrong = wrong + 1
                "All of the above":
                    "Good job, my little detective."
        
        Fred "Trick question: it was all of them"
        Fred "I may have mentioned that it was only Byeong-Yeon who was publicly humiliated,"
        Fred "but with the spread of gossip with how the others were different, they also suffered through public humiliation"
        jump q4

    label q4:
        Fred "Question number four. You're nearing the end here, buddy."
        Fred "What was each student disciminated against them?"

        label question4:
            default q4choice = True
            menu:
                "Jones:Gender Identity; Byeong-Yeon:Race; Chica:Religion":
                    Fred "Nope! Sorry bucko"
                    $ wrong = wrong + 1
                    $ q4choice = False
                "Jones:Sexuality; Byeong-Yeon:Nationality; Chica:Developmental Disability":
                    Fred "Right you are, nice work"
                "Jones:Gender Expression; Byeong-Yeon:Ethnicity; Chica:Learning Disability":
                    Fred "Ehh, not quite..."
                    $ wrong = wrong + 1
                    $ q4choice = False

            if q4choice == False:
                Fred "Jones was discriminated for being gay, ergo they targetted his sexuality"
                Fred "Byeon-Yeon was made fun of for being Korean, therefore, Nationality"
                Fred "And lastly, Chica's Autism is a Developmental Disability"
                Fred "Did the similar choices mess ya up?"
                jump q5
            else:
                Fred "Not bad, glad to see you knew the difference of each choice"
                jump q5

    label q5:
        Fred "Alrighty then, we're at the last question"
        Fred "Out of all of these, what is the ONE main thing discrimination strip people away from"
        
        label question5:
            menu:
                "Freedom":
                    Fred "Ohh...sorry not quite"
                    jump outro
                "Unity":
                    Fred "Nope, sorry bud wrong answer"
                    jump outro
                "Human Rights":
                    Fred "Well done, [mcName]"
                    jump outro
                "Opportunities":
                    Fred "Not the answer I was looking for, sadly. But you were close."
                    jump outro

    label outro:
        Fred "Well. that wraps up about the small test for today"
        Fred "Great work on our warm up, bud"

        main "Wait....warm up?"

        Fred "Well I mean, yeah, this is literally just the first day of your training"
        Fred "Don't forget, we still gotta train you up for the big event!"

        main "Then what was all of today for???"
        
        Fred "That was an introduction, a small taste of what's to come, if you will"

        Fred "Anyways, let's review your score."
        if wrong <= 3:
            jump goodend

        else:
            jump badend

    label goodend:
        Fred "In total, you got atleast [wrong] mistakes"
        Fred "Not bad, seems like you really did listen to a word I said"

        main "Surprisingly, yeah"
        main "Hey, the next time we do this, please give me a heads up at least"

        Fred "Heh...no promises"
        Fred "It's called the art of always being ready for a popquiz"
        Fred "Trust me, you're gonna need that in this kinda school"

        main "God spare me"

        "Fred chuckles as he pats you in the back and gives you a warm smile"
        jump end
        

    label badend:
        Fred "In total, you got atleast [wrong] mistakes"
        Fred "Not that I expected any specific outcome from today, but....we can work on it I guess"

        main "To be fair, I was so not prepared for that quiz"

        Fred "You gotta start being prepared for anything, [mcName]"
        Fred "But yeah, mind handing me your schedule later, I really do think we need to practice this a bit more"

        "Fred fidgets around his phone as he types away, trying to schedule what seems to be your future training sessions with him"

        main "HEY HEY HOLD ON"
        main "It is quite literally my first day in college, don't tell me you're scheduling more trainings"

        "Fred blinks at you dumbfounded as he stops what he's doing and scratches his head"

        Fred "Heh...sorry. Got a bit carried away there"
        Fred "Totally forgot about that"
        jump end


    label end:
        "A ringing alarm errupts from Fred's pocket. He pulled his phone out to silence the alarm"

        Fred "Huh, 6:30 already. I guess it's time to pack up and head home"

        main "Yeah, I'm pretty beat from today"

        Fred "C'mon, let's head to the cafeteria and grab a coffee or something. Pretty sure my boyfriend's waiting for me there"

        main "You're....boyfriend?"

        Fred "Yeah, he's pretty chill, I can introduce him to ya"
        Fred "Wait haven't I mentioned him yet or-"

        main "N-nope..."

        "Fred blinked a few times densely before smirking at you as he raised a brow and a toothy grin"

        Fred "Why? Any particular reason you were asking?"

        menu:
            "NO. not at all":
                Fred "Sure thing, hehe"
            "I thought you were single":
                Fred "Pffft, yea even I was surprised how I managed to fish a guy in"
            "I'm not into you":
                Fred "Bummer, so tragic, I'm sobbing, seething of rage even"
        
        Fred "Anyways, let's go before the shuttle stops service for tonight"
        Fred "You did good today, let's try to keep this up before the event"

        main "Thanks...evem if you did just drag me here by the wrist forcefully"
        main "And threw me into a mini gameshow quiz"

        Fred "What can I say, I'm pretty unpredictable"

        "Fred's phone began to ring, pulling it out of his pocket to be met by an incoming call from his partner"

        Fred "Welp, looks like that's our call. C'mon, I can show you all the good types of coffee they have at this hour"

        "Fred jogs off out of the room in an excited hurry as you chase on after him"
        "This is gonna be a long journey at your new college, but hey, at least you're having fun with it"
        "End of Fred's Chapter."
    return



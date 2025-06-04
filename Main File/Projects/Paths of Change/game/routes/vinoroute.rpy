label vinoroute:

    "You see a boy picking up trash and recycling"

    "He seems familiar to you as you have seen him before"

    main "I wonder what he's doing out here all alone...?"

    Vino "Oh, hello there"

    Vino "You were the one I met at the cafeteria, right?"

    main "Yeah..."

    Vino "So... what are you doing out here?"

    main "Well... I just coincidentally passed by, though the sky has been looking dark and gas emissions have been heard to be through the roof"

    main "How about you? You shouldn’t be out here during a time like this"

    Vino "Well remember what we talked about last time?"

    Vino "How I like to help around the park and all"

    Vino "And as you said, gas emissions have been up... So, I'm trying my best to help even through recycling"

label Vinochoice:

    main "What should I do?"

menu:

    "You walk away":

        "WARNING: This option will abort Vino's route completely"

        "Do you wish to proceed?"

        menu:
            "Yes":
                jump abortvinoroute
            "No":
                jump Vinochoice
    
    "You help Vino":
        jump continuevinoroute

label abortvinoroute:

    main "Oh, alright, well, good luck with what you’re doing!"

    main "I’ve got some things to do so I’ll be going first"

    Vino "Thanks! See you at school!"

    $ abortVino = True

    jump abort

label continuevinoroute:

    scene bg park

    main "That's a great idea, do you mind if I come along? I'd like to help as much as I can!"

    Vino "Oh! You'd like to help? I'd gladly accept it!"

    Vino "Okay, so our task is to collect all this trash on the floor and dispose of it properly and for the things that could be recycled, we'll put them into another bin"

    Vino "Sounds easy, right? Alright! I'll start over here and you can start over there. Get back to me when you're done"

    main "Sure! I'll get started then"

    "Some time passes..."

    Vino "Hey, I'm done over there, how is it here on your side?"

    main "It's bad. There's trash everywhere and whenever I do pick some up, there's just more coming... it feels endless"

    main "I'm glad that I was able to come and help you out here, it would have taken too long if you had done it by yourself..."

    Vino "Yea... but I've got to do something about all this trash, so it can't be helped"

    Vino "Though it was nice that you were able to help me!"

    main "Of course! This task is too heavy for one person"

    Vino "That just gave me an idea!"

    main "hm?"

    Vino "We should gather more people to help us clean this park up, so many use it but no one takes care of it as much as it should be"

label Vinochoice2:

    main "Do you wish to go with the plan?"

menu:
    "Disagree with the plan":
        jump disagreevinoplan

    "Agree with than plan":
        jump agreevinoplan


label disagreevinoplan:

    scene bg park

    main "I don't know about that one... It might get a bit messy if we involve other people..."

    Vino "Hm... I think you have got a point there, but nevertheless we still need to find a way to help as much as we can"

    main "We should just continue recycling from time to time, it'll still be good help"

    Vino "Yeah I guess... though I wish we could do find a more efficient and effective way that could help on a larger scale"

    Vino "Anyways, thanks for your help"

    Vino "I really appreciate it, even if it's just the two of us"

    main "no problem... anytime"

    scene bg black

    "You both leave and went home"

    "As you are walking, you get a notification from your phone about the current news"

    News "Breaking News!!! after gathering further statistics, it has been confirmed that greenhouse gas levels have been through the roof! and without further action this might lead to severe cliate changes throughout the year"

    main "Oh no..."

    main "This is getting out of hand..."

    "You think twice about what Vino said while you walk home"

    "Time passes and it's the next day..."

    main "Should I bring it up with Vino...?"

    main "After what I said yesterday, I'm not sure..."

    "LUNCHTIME"

    scene bg caf

    "You see Vino in the cafeteria"

    "You feel hesitant approaching him"

    main "Will you approach him?"

menu:
    "Approach Vino":
        jump approachvino

    "Continue on without noticing him":
        jump ignorevino

label ignorevino:

    scene bg caf

    "The feeling of reluctancy you continue walking"

    "You make eye contact with him as you pass by but chose to ignore him"

    "A few weeks have passed..."

    "You being on your phone"

    "A notification popped up"

    "You check it out as you noticed it was about the latest news"

    News "INCOMING NEWS! Statistics have shown that for the pass few weeks, gas emissions have been through the roof!"

    News "It is also stated that in the upcoming months, these levels may increase rapidly!"

    main "I wish I did something back then..."

    "The route ends with a feeling of regret..."

    $ abortVino = True

    jump abort

label approachvino:

    scene bg caf

    "As you see Vino you continue to walk towards him"

    "With the slight feeling of reluctance you muster up the courage to talk with him"

    main "Hey, Vino"

    Vino "Oh, hey"

    Vino "Is there something you need?"

    main "Uhm.. yeah"

    main "It's about what we talked about yesterday"

    Vino "Hm?"

    main "I think we should continue it"

    Vino "What do you mean?"

    main "We had this idea, right?"

    main "Where we would gather people that could help recycle and all"

    Vino "Oh... that"

    Vino "What changed your mind?"

    main "After seeing the latest news update..."

    main "I gave it some thought last night and I think we do need to take action"

    main "Even the slightest help can reduce the gas emissions"

    main "So I think we should continue our plan"

    Vino "Alright, I'm glad you changed your mind!"

    Vino "Are you free after this?"

    main "Yeah, I am"

    Vino "Let's grab some food and continue with what we were talking about yesterday"

    main "Sounds like a good idea"

    "You both grab some food to eat"

    "Time passes..."

    "You both finish your food"

    main "Alright, so where do we start?"

    Vino "Okay so, I think we should start getting the attention of people first"

    Vino "I was thinking, what if we posted a quick poster or something online about helping around in the park"

    Vino "It could be about recycling, pickup up trash, waste disposal, etc."

    Vino "This should catch peoples attention"

    main "Yeah, that sounds great!"

    main "We could also set up a schedule for whenever we meet up in the park"

    Vino "Exactly!"

    Vino "Alright so I'll go ahead and make the poster as soon as I can"

    Vino "What I need you to do is spread the word about it"

    Vino "I'll do the same with the people I do gardening with. they for sure would love to help"

    main "Okay okay, I'll get going then"

    Vino "Same for me, I'll get started with the poster and everything else"

    scene bg black

    "Some time passes..."

    "Both of you accomplish the distributed tasks"

    "You both meet up and felt accomplished knowing you have done something to help"

    scene bg caf

    Vino "Alright, everything seems to be going according to plan"

    main "Yeah, I even got some people who were already interested"

    Vino "For now, we'll just have to see how it all plays out"

    main "That's true"

    main "From this onwards, we'll have to continue putting in the effort"

    scene bg black

    "After a few weeks passing by..."

    News "INCOMING NEWS! Updated statistics have shown that throughout the pass week, gas emissions have shown signs of dropping!"

    News "It is said that after a few months, it may drop by a whole 20 percent!"

    scene bg park

    "You and Vino are in the park"

    "You look around and see all the people helping"

    "Vino takes a deep breath and looks at you with dedication in his eyes"

    Vino "Dude, we've done it"

    Vino "We were able to make a small thing turn into a huge impact"

    main "Yeah, it was all worth it"

    "You both look around once more and feel satisfied"

    Vino "I really can't believe that we were able to do this"

    Vino "Honestly, all I can say is thank you"

    main "Man, it wasn't just me"

    main "You were the one who opened my eyes and made me see the bigger picture"

    main "If you didn't influence me, I probably wouldn't even be doing anything about it right now"

    Vino "Yeah, I'm glad we were both able to infleunce each other and a lot more"

    "You both feel proud and accomplished after all the hardwork"

    "You have reached the ending of this route..."

label agreevinoplan:

    main "That sounds like a fantastic plan! I could already think of what we could do!"

menu: 
    "We should post online about inviting people to maybe like a community and gather those who want to help!":
        jump vinoideachoice1

    "We should scream at people to join our community and make them help!":
        jump vinoideachoice2

label vinoideachoice2:

    scene bg park

    Vino "Are you for real...?"

    Vino "Uhm... I think I’ve got this... You can go ahead and continue what you were doing..."

    "Vino walks back to cleaning the park surroundings and recycling"

    "Your route has ended"

    $ abortVino = True

label vinoideachoice1:

    scene bg park

    Vino "That sounds like an amazing idea! We should do it when we’re both free from school!"

    main "Right! Here is my number..."

    Vino "Alright! Thanks! I’m grateful for your help!"

    Vino "I’ll message you when I can, so look out for it!"

    main "Sure, I'll be waiting!"

    "Some time passes..."

    "You and Vino met up to discuss the plans"

    scene bg caf

    Vino "Okay so, I think we should start getting the attention of people first"

    Vino "I was thinking, what if we posted a quick poster or something online about helping around in the park"

    Vino "It could be about recycling, pickup up trash, waste disposal, etc."

    Vino "This should catch peoples attention"

    main "Yeah, that sounds good for me"

    main "I'll go ahead and spread the word about it throughout the school"

    Vino "Right! and I'll start with the poster"

    "You both leave to complete your own tasks"

    scene bg black

    "A week has passed by..."

    scene bg hall

    "You were walking in the hallway and suddenly got a notification"

    "Checking it you noticed it was from the news"

    News "Breaking News!!! after gathering further statistics, it has been confirmed that greenhouse gas levels have been through the roof! and without further action this might lead to severe cliate changes throughout the year"

    main "I hope this plan works..."

    "You get another notification"

    main "Oh, Vino"

    "You checked his message"

    Vino "DUDE, THE POSTER WE POSTED ONLINE!"

    Vino "It's through the roof right now! A lot of people have been looking into it and are even talking about it!"

    Vino "There are also some people who already volunteered!"

    "You think to yourself"

    main "It's working!"

    main "Now, we just need to expand and gather more people"

    scene bg black

    "A few weeks have passed by"

    News "INCOMING NEWS! Updated statistics have shown that throughout the pass week, gas emissions have shown signs of dropping!"

    News "It is said that after a few months, it may drop by a whole 20 percent!"

    scene bg park

    "You and Vino are in the park"

    "You see the amount of people who have gathered to help"

    Vino "I'm glad we did this"

    main "Yeah, even though it just started as the two of us we were still able to accomplish something this big"

    Vino "It was good to work with you"

    main "Right back at you man"

    "You both look around once more, amazed with the amount of people that have helped for a greater cause"

    "Your route has ended..."

    return








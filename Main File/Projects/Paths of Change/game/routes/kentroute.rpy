image bg_ApartmentIn = "ApartmentIn.avif"
image bg_ConvinienceOutside = "ConvinienceOutside.jpg"
image bg_Convinience = "Convinience.jpg"
image bg_Gym = "Gym.png"
image bg_McdIn = "McdIn.jpg"
image bg_McdoOutside = "McdoOutside.jpg"
image bg_Kitchen = "Kitchen.jpg"
image bg_Park = "Park_jpg"
image bg_Door = "Door_jpg"
image bg_Black = "Black.png"
image bg_City = "City.jpg"

label kentroute:
    Kent "You wanna hang out with me?"

menu:
    "Yeah...":
        jump yh1

    "On second thought, I remembered you said that you have something else to do."
        "WARNING: This option will abort Kent's route completely."
        "Do you wish to proceed?"

        menu:
            "Yes":
                jump routeabort

            "No":
                jump kentroute

label routeabort:
    main "On second thought, I remembered you said that you have something else to do."
    "You remembered your conversation with him earlier."
    Kent "Oh yeah, I do have something else to do."
    Kent "Well, we can always hang out if you want to. We are seatmates so..." 
    Kent "Just not for now since I am occupied with something."
    main "What are you so occupied with?"
    Kent "Well... Let's say it's a secret."
    Kent "(Can't really say that I am occupied with games.)"
    Kent "Well then, talk to you later."
    main "Yeah..."
    "After some time... You thought about your next course of action."
    main "Who should I go with?"
    
    #Needed to add options that can redirect to other routes
    return


label yh1:
    main "Yeah..."
    Kent "Alright..."
    "Kent nodded."
    Kent "Knowing that you are new here, I’ll take the lead."
    Kent "You okay with that?"
    main "Yeah."
    Kent "Of course, if you have anywhere you want to go, then we’ll go there as well."
    main "Oh, thanks."
    Kent "Nice. Now with that decided, let’s go to the nearest fast-food restaurant first to eat before going anywhere else."
    Kent "You good with it?"
 
menu:
    "Yup.":
        jump yer
 
    "Well, I am a little hungry so...":
        jump yerr
 
label yer:
    main "Yup."
    Kent "The nearest fast-food restaurant here is McDonald's. Let’s go there."
    jump goi
 
label yerr:
    main "Well, I am a little hungry so..."
    Kent "Same here!"
    Kent "The nearest fast-food restaurant here is McDonald's. Let’s go there."
    jump goi
 
label goi:
    scene bg_Black
    "After walking for a while..."
    scene bg_McdoOutside with dissolve
    Kent "W-we’re here. Let’s go in."
    "You noticed how exhausted Kent is despite just walking for a short while."
 
menu:
    "Hey, are you alright?":
        jump yera
 
    "Wait, you’re exhausted already?":
        jump yerb
 
label yera:
    main "Hey, are you alright?"
    Kent "Yeah, just a bit tired."
    jump yerc
 
label yerb:
    main "Wait, you’re exhausted already?"
    Kent "How rude. Though yeah, my stamina is dead."
    jump yerc
 
label yerc:
    Kent "Well, this has always been the case for me though."
    Kent "Nothing new, really."
    main "Oh, I see."
    Kent "Well, enough about me. Ready to go in?"
    main "Absolutely!"
    Kent "Woah, so enthusiastic."
    scene bg_Black
    "You both got inside and took a seat…"
    scene bg_McdIn with dissolve
    Kent "Finally! Air that really feels good to the touch."
    "Kent said excitedly."
    Kent "By the way, do you know what you want to get?"
 
menu:
    "Yup":
        jump yes
 
    "Not yet... Too many choices here.":
        jump no
 
label yes:
    main "Yup."
    "You told Kent what you want."
    Kent "Oh? You’ve got quite the interesting combination."
    jump next
 
label no:
    main "Not yet... Too many choices here."
    Kent "Take your time, though don’t take too long."
    main "No, it’s fine. I know what I want now."
    "You told Kent what you want."
    Kent "Oh? You’ve got quite the interesting combination."
    jump next
 
label next:
    main "Well, gotta balance what I eat after all."
    "You were curios as to what Kent wants to order."
    main "What do you want to get for yourself?"
    Kent "Well... I will order fried chicken, burger, fries, and coke."
 
menu:
    "...That’s a lot":
        jump lot
 
    "Are you sure about that? Those are quite the unhealthy combo you have.":
        jump sure
 
label lot:
    main "...That’s a lot"
    Kent "Gotta eat a lot, you know?"
    jump sure
 
label sure:
    main "Are you sure about that? Those are quite the unhealthy combo you have."
    Kent "Nah, it’s fine. I eat these types of food almost every day. And look, nothing happened."
 
menu:
    "(Let him be)":
        jump be
 
    "(Suggest something)":
        jump something
 
label be:
    main "If you say so..."
    "You reluctantly said."
    Kent "I’ll order now."
    jump arrive
 
label something:
    main "Why not, you know? Add something green alongside?"
    Kent "Ehh..."
    "Kent said in an aloof manner, expressing his unenthusiasm"
    Kent "Fine, I’ll add some of that just as you've said. Although just once."
    "He said reluctantly"
    main "Nice. That's it, my guy."
    Kent "I’ll order now."
    jump arrive
 
label arrive:
    "While waiting for the orders to arrive…"
    Kent "What do you do usually?"
 
menu:
    "Well... That's sudden. Though it's a secret":
        jump secret
 
    "Hmm... I usually study, exercise, and do what I like.":
        jump usual
 
label secret:
    main "Well... That's sudden. Though it's a secret"
    Kent "Eh… No secrets please."
    main "Just kidding."
    main "Well, I usually study, exercise, and do what I like."
    jump usual1
 
label usual:
    main "Hmm... I usually study, exercise, and do what I like."
    Kent "You’re so active, huh?"
    main "How about you?"
    jump ab
 
label usual1:
    main "Well, I usually study, exercise, and do what I like."
    Kent "Wow, so active."
    main "How about you?"
    jump ab
 
label ab:
    main "How about you?"
    Kent "About me..."
    Kent "Well, I just play games and laze around all around the clock. I don’t really go out that often so..."
    Kent "That’s it."
    main "..."
    "You stared at him in silence."
    Kent "Hey… What’s with the silent stare? You’re scaring me."
    "You asked him again."
 
menu:
    "Not working out, studying, or breathing fresh air frequently?":  
        jump LED
 
    "...Are you a vampire avoiding the big LED outside? So sensitive to vitamin D?":
        jump vamp
 
label LED:
    main "Not working out, studying, or breathing fresh air frequently?"
    Kent "Well, yeah. More or less."
    "You thought to yourself that it’s no wonder why he is physically weak."
    jump gue
 
label vamp:
    main "...Are you a vampire avoiding the big LED outside? So sensitive to vitamin D?"
    Kent "So harsh! It's not that bad, bro."
    "He said in a mild exasperated expression."
    jump gue
 
label gue:
    main "I guess... so?"
    "You are pondering about something."
    main "You know what? Why don’t we hangout often?"
    Kent "Wait wait wait... How come?"
    "Kent was surprised by your sudden suggestion."
 
menu:
    "Hearing what you said, I just thought it would be a good idea, no?":
        jump idea
 
    "You won’t live long bro. You won’t reach the release of GTA 6 at this rate.":
        jump longa
 
label idea:
    main "Hearing what you said, I just thought it would be a good idea, no?"
    Kent "Ehh… What a pain that is."
    jump next1
 
label longa:
    main "You won’t live long bro. You won’t reach the release of GTA 6 at this rate."
    "You said smugly."
    Kent "Hey… That’s rude. Though I would hate it if I can’t get myself to play that game."
    jump next2
 
label next1:
    "Kent is spacing out thinking about something."
    Kent "Well, I guess it’s alright?"
    Kent "I’ve got nothing better to do anyways other than what I said. And you’re fun to be with also so it’s a win-win for me."
    jump next3
 
label next2:
    "After a while..."
    Kent "Alright, you win... I’ve got nothing better to do anyways other than what I said. And you’re fun to be with also so it’s a win-win for me."
    jump next3
 
label next3:
    "Just then, the orders arrived."
    main "Then it’s decided! We can talk about what to do later. We’ll eat for now."
    Kent "Yep, I feel hungry after seeing the food haha."
    "He said while looking at the food happily."
    "After some time..."
    Kent "I’m stuffed!"
    "He said while patting his stomache."
    main "So, what do we do now?"
    Kent "Let’s see..."
    Kent "Why don’t we leave for now?"
    main "Yeah, let do that."
    scene bg_Black
    "After leaving KFC, Kent groans, rubbing his stomach as they walk down the street. The sun is setting, casting an orange glow over the sidewalk."
    scene bg_McdoOutside with dissolve
    Kent "Ugh… I might have overdone it."
 
menu:
    "Saw this coming knowing how much you ate.":
        jump saw
 
    "Want to walk it off? Looks like there's a convenience store just in front with water.":
        jump conv
 
label saw:
    main "Saw this coming knowing how much you ate."
    "You said bluntly as if you expected this much to happen."
    Kent "W-well..."
    "He said with an awkward laugh."
    jump conv
 
label conv:
    main "Want to walk it off? Looks like there's a convenience store just in front with water."
    Kent "Water? Bold of you to assume I hydrate."
    main "Yeah yeah..."
    scene bg_Black
    "Inside the convenience store, fluorescent lights buzz overhead. Kent immediately veers toward the energy drinks. You step in front of him, blocking the way."
    scene bg_Convinience with dissolve

menu:
    "Nope. Try this one instead.":
        jump this
 
    "You’ll literally turn into a glow stick if you drink another one of those sooner or later, you know?":
        jump this1
 
label this:
    main "Nope. Try this one instead."
    "You gave Kent coconut water, and he reluctantly took a sip of the coconut water and gags."
    Kent "Ugh, this tastes like regret."
    main "It’s not that bad, you know?"
    jump noto
 
label this1:
    main "You’ll literally turn into a glow stick if you drink another one of those sooner or later, you know?"
    "You handed Kent a coconut water, and he reluctantly took a sip of the coconut water and gags."
    Kent "Ugh, this tastes like regret."
    main "It’s not that bad, you know?"
    "You said while smirking."
    Kent "Yes, it is…"
 
label noto:
    scene bg_Black
    "Despite what he said, he bought another anyway, sulking as you two exit."
    scene bg_ConvinienceOutside with dissolve
    "You both sat on a bench outside the store, watching pigeons fight over a discarded fry. Kent swirls his coconut water like it’s a fine wine he hates."
    Kent "Hey… Why do you even care about my ‘health’ or whatever?"
    "He said, avoiding eye contact, kicking at the pavement."
 
menu:
    "I already told you the reason earlier though. Forgot it already?":
        jump already
 
    "Someone’s gotta call you out when you’re being a self-destructive gremlin.":
        jump grem
 
label already:
    main "I already told you the reason earlier though. Forgot it already?"
    Kent "Well... no?"
    "He said looking nervously"
    main "Right..."
    "You are doubting what he said."
    "You told Kent the reason and he was listening closely."
    main "I wanna hang out with you for a lot longer. Can't have you dying early now, can I?"
    Kent "Huh? The heck was with that reason?"
    "You grin as you said that, bumping his shoulder while he look flabbergasted."
    "He said that but you know that he understood what you were trying to convey to him."
    jump reas
 
label grem:
    main "Someone’s gotta call you out when you’re being a self-destructive gremlin."
    "You grin as you said that, bumping his shoulder."
    Kent "Gremlin? Rude."
    "He said smiling, and there’s a flicker of something softer in his expression."
    "Knowing that you were concerned for him made him happy."
    main "Eh... Are you that happy?"
    "You said mockingly..."
    Kent "You shut it. I'm going home."
    main "Yeah yeah, I'll do that as well."
    jump nex
 
label reas:
    Kent "Eh, is that really it?"
    main "Yes sir"
    "You said proudly"
    Kent "I see.. Haha"
    "He said while laughing."
    jump nex
 
label nex:
    scene bg_Black
    "The next day and following days, you two are hanging out. More accurately, you are dragging him around all over the place."
    scene bg_City with dissolve
    Kent "Don't you get tired?"
 
menu:
    "Of course not.":
        jump answ
 
    "Heh... It's gonna take more than that to exhaust me.":
        jump exha
 
label exha:
    main "Heh... It's gonna take more than that to exhaust me."
    "You said while looking at him, grinning."
    Kent "But it is for me, though..."
    main "Yes yes. Let's go."
    Kent "Ugh, I’d rather die."
    "He said as if he is in despair."
    jump shr
 
label answ:
    main "Of course not."
    main "And you are going to go along with me and I won't be taking no as an answer."
    Kent "I don't even have a choice anymore?!"
    main "Nada, stop whining bro. You can do it!"
    "You said to cheer him."
    jump shr
 
label shr:
    scene bg_Black
    "One week later, you dragged Kent to a local gym’s free trial day. Kent clings to the doorway like a cat avoiding a bath."
    scene bg_Gym with dissolve
    Kent "I will never let go. Never!"
    "He said, looking so fired up and motivated"
 
menu:
    "You’re at it again, huh? You will die if you don’t move. C’mon, just the treadmill!":
        jump nochoi
 
    "Fine. But if you refuse, we’re volunteering at the animal shelter next weekend.":
        jump nochoi
 
label nochoi:
    Kent "…Treadmill. But I’m setting it to ‘snail’."
    "He lasts four minutes before dramatically collapsing onto the machine, wheezing."
    main "You lasted longer than thought."
    Kent "W-well, it’s me we are talking here."
    "He said proudly."
    main "Really?"
    "You said to Kent while smirking wickedly."
    Kent "No, no. I’m joking. Please no more. I’ll die at this rate."
    "He said while sweating bullets and shivering."
    main "I’m joking. Let's take a short break."
    "Kent looked at you like you’re a saint."
    main "Stop looking at me like that."
    scene bg_Black
    "After the gym session, you invited Kent in your apartment."
    scene bg_Kitchen with dissolve
    "Later in your apartment. Smoke billows from a pan as Kent frantically waves a towel at the screeching smoke alarm."
    Kent "I told you I’m a takeout guy! I don’t cook!"
    main "We’re trying again. And no, ordering pizza doesn’t count as ‘cooking’."
    "You thought to yourself that maybe starting to cook from the get-go is tough for beginners."
    main "…Okay, maybe we’ll start with sandwiches next time."
    "You said with a defeated sigh, opened the window."
    Kent "I miss my chicken nuggets."
    "He said while holding up a charred lump that was supposed to be chicken."
    scene bg_Black
    "Months later, at 7 AM, Your doorbell rang. Kent stands there in neon-orange sneakers, looking like he hasn’t slept."
    scene bg_Door with dissolve
    Kent "I hate you for this. Let’s go before I change my mind."
 
menu:
    "Who are you and what have you done to Kent?":
        jump jog
 
    "Proud of you. Now suffer with me.":
        jump jog
 
label jog:
    "You two have jogged on the nearby park."
    main "Here, water."
    "You handed him a bottle of water."
    "The two of you jog half the path before Kent stops, hands on his knees, panting."
    "But he doesn’t complain, just staring at the horizon above."
    main "See?"
    Kent "Hmm? What do you mean?"
    main "Compare to how you look when we first met, you look far better. A little movement doesn’t exhaust you anymore."
    main "At first, you looked so pale, and your complexion looks so dire. I also remember the fact that you tend to get too easily get sick."
    main "But now? Those problems are already gone when I more or less forced you into getting back in shape. Though you were reluctant at it first."
    "You said with a faint laugh."
    Kent "W-well, it thought it was hard, and yes it was. But I kinda, you know? Enjoyed it more or less doing it with someone."
    main "Now you're talking like someone living life to the fullest."
    Kent "Shut it."
    main "Haha, alright alright."
    "You two continued to talk before going home."
    scene bg_Black
    "Montage of progress: Kent’s gaming streams now feature \"Fitness Fail\" compilations. His fridge has two vegetables. He still groans about weekly runs, but he’s there every time."
    Kent "…Okay, maybe endorphins are a real thing."
    main "Told you. Next goal: Yoga. No excuses."
    main "You said while grinning."
    Kent "I will block your number."
    "But he’s already following, shaking his head with a smile."
    scene bg_Black

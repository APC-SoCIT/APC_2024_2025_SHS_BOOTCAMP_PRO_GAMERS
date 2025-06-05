label lilyroute:

    scene bg guidance_office

    "You return to the guidance office, pamphlet in hand. A quiet tension sits in your chest—you’re still unsure about your future."

    "The room feels the same, neat and quiet, but there's a sense of warmth to it now. Maybe because you remember the face from before."

    "At the front desk, a familiar girl is hunched over a small stack of papers, focused."

    "You hesitate, then clear your throat."

    main "Excuse me, miss?"

    "She looks up and beams when she sees you. It’s Lily."

    Lily "Oh hey, you came back! That’s a nice surprise."

    main "I was hoping you could help me again. It’s about the pamphlet you gave me… the one with the seminars."

    Lily "Of course!"  

    "She reaches under the desk and pulls out a fresh copy of the seminar guide."

    Lily "I actually hoped you’d come back. Most students just grab it and leave. Not many take the time to ask more."

    main "I wasn’t sure if I’d come back either… but I guess I kept thinking about it."

    Lily "That’s a good sign. It means something stuck."

    "She lays out the pamphlet on the counter and taps a few parts with her pen."

    Lily "There’s a variety of topics covered here—business, tech, science, health care, and creative fields too."

    main "I’ve been thinking. I like drawing, and… maybe something creative?"

    Lily "That narrows it down! We have a design and multimedia seminar next week—it’s a mix of visual arts and digital content creation. You’d probably enjoy it."

    main "That does sound interesting."

    Lily "And it’s hands-on! You’ll get to try out basic editing software, sketch some mockup designs, maybe even collaborate on a mini-project."

    main "That sounds... kind of fun, actually."

    Lily "Great! I can sign you up now if you want."

    main "Yeah. Please do."

    "Lily writes your name down on a small clipboard and smiles."

    Lily "There we go. You’re officially registered."

    main "Thanks. You really make this stuff easier to think about."

    Lily "That’s kind of the point. You don’t have to figure it all out alone."

    "She gives you a playful wink."

label Lilychoice:

    main "What should I do now?"

menu:
    "Thank her and leave":
        jump lilyabortending

        "WARNING: This option will abort Lily's route completely"

        "Do you wish to proceed?"

    "Ask her if she’s attending too":
        jump lilycloseroute

label lilyabortending:

    scene bg hallway
    with dissolve

    "You thank Lily politely, but your steps feel heavier as you leave the office."

    "You pause in the hallway, the pamphlet crinkling in your grip."

    "Your thoughts buzz—was this the right path? Were you ready?"

    "Slowly, you fold the pamphlet and slide it into your bag, but you already know you won’t be showing up to the seminar."

    "Maybe next time… or maybe not."

    scene bg black
    with fade

    "You left without committing, unsure of the road ahead."

    "You chose the Abort Ending."

     $ abortVino = True

    jump abort


label lilycloseroute:

    scene bg guidance_office

    main "Hey… are you attending the seminar too?"

    Lily "Hmm? Me? Well, not as a guest. I help with organizing and setup. So I’ll be there the whole time."

    main "Cool. Maybe I’ll see you around then?"

    Lily "Definitely. And hey—if you get nervous or lost, just look for me, alright?"

    main "I will. Thanks again, Lily."

    Lily "Anytime."

    scene bg black

    "A few days later…"

    scene bg seminar_room

    "The seminar room buzzes with quiet chatter as students take their seats."

    "You glance around and spot Lily near the projector, arranging materials."

    "You feel oddly calmer knowing she’s here."

    Lily "Hey! You made it."

    main "Yeah. I guess I’m actually excited now."

    Lily "That’s the spirit. Go on, grab a seat—I’ll be around if you need anything."

    scene bg seminar_hands_on

    "The seminar unfolds with hands-on activities—sketching wireframes, using simple editing software, and discussing creative challenges."

    "You dive into it more than you expected. Ideas begin to flow."

    "During the break, Lily approaches with two bottled drinks."

    Lily "Thirsty? I figured you’d be working hard."

    main "Thanks. This is actually more fun than I thought."

    Lily "Told you! It’s all about finding that spark."

    scene bg park_evening

    "After the seminar, you and Lily walk around campus as the sun sets."

    Lily "You really lit up during that seminar. It was nice to see you so focused."

    main "I didn't expect to enjoy it this much. You were right."

    Lily "You have talent. Don’t let it go to waste."

    "She stops walking for a moment and turns to you."

    Lily "Actually... there's a student creative group forming soon. We work on design projects, do exhibitions, help promote events. I think you'd fit in."

    main "Oh—really?"

    Lily "Yeah. Want to join?"

label lilyfinalchoice:

menu:
    "Join the group and keep spending time with Lily":
        jump lilybestending

    "Thank her but say you're not ready yet":
        jump lilygoodending

    "Say you're not really interested after all":
        jump lilybadending

label lilybestending:

    main "Yeah… I want to be part of it. With you."

    Lily "That makes me really happy. I was hoping you'd say that."

    scene bg clubroom_day

    "A few weeks later, you’re part of the creative group. You attend weekly meetings, help organize posters, and even lead your own project."

    "Lily becomes a constant presence—not just a mentor, but a close friend… maybe something more."

    scene bg rooftop_evening

    "One evening, the two of you sit together on the school rooftop, watching the sky darken."

    Lily "I knew from the start you had something special. I’m glad you trusted yourself."

    main "I wouldn’t have found that out without you."

    Lily "Maybe. But you’re the one who chose to try."

    "She rests her head on your shoulder."

    "The path ahead doesn’t seem so uncertain anymore."

    scene bg black

    "You found both a direction and a person to walk it with."

    "You chose the Best Ending."

    return

label lilygoodending:

    main "Thanks, Lily. I think I’ll keep working on my own for now. But I really appreciate everything."

    Lily "That’s totally fair. I just hope you keep going—you’ve got a real spark."

    main "I will. I’m really grateful to you."

    Lily "Anytime. And hey… even if we’re not in the same group, don’t be a stranger, alright?"

    "You smile and nod."

    scene bg black

    "You take what you learned and pursue your creative interests."

    "You and Lily stay in touch, and maybe someday… something more might blossom."

    "You chose the Good Ending."

    return

label lilybadending:

    main "I don’t think I’m interested anymore. It was fun, but… I guess I’m just not cut out for it."

    "Lily’s expression falters, but she recovers quickly."

    Lily "I see. That’s okay—sometimes we try things and find out they’re not for us."

    main "Yeah… sorry if I wasted your time."

    Lily "You didn’t. Just… don’t give up on yourself completely, okay?"

    "You nod, but part of you isn’t sure."

    scene bg black

    "You walk away from the chance to grow—uncertain, and with a subtle feeling of regret."

    "You and Lily drift apart. The moment passes, never to return."

    "You chose the Bad Ending."

    return

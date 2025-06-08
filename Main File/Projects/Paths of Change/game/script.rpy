label start:

    "Ughh...new college, new headache"
    "This year, my parents wanted me to go to a newly appointed university in town"
    "Quite surprising, really I honestly didn't expect to be in this university of all things"
    "Pretty peculiar honestly"
    "Oh wait...before I forget, my ID"
    "Where is it...I know its here somewhere"

    $ mcName = renpy.input("Enter your name", length = 32)
    if not mcName:
        $ mcName = "You"

    main "Ah, there it is"

    "You put on your lanyard with a bright yellow shade and blue highlights that reflects your school's main color palette"
    "On your lanyard is a fresh new ID with your name and face on it, dresssed in a business attire they made you wear when you admissioned"
    "\"[mcName]\""
    
    main "Welp, time to get ready for school"

    play music "bgmusic.mp3"
    scene bg shuttleout with dissolve

    "On your way to the bus stop, or...the shuttle station, as how you hear other students call it, you seem to be the only one there"
    "You try to stop and take in the environment as you wait for the bus"
    "Lush trees, a clear sky, a peaceful neighborhood, it reminds you a bit of home"
    "Your peace is interrupted briefly as you hear a loud clang behind you"
    "You turn back to see two other students who seem to have fumbled onto another"

    StudentV "Hey, watch it! You made me drop my water bottle"
    StudentL "We wouldn't have hit you if you weren't like so in the way, Vino"
    StudentF "Guys...it is so early in the morning, can we please not make a fuss at the shuttle"
    
    "The trio's quarrel went on for a bit as you just watched in silence as the ruckus behind you unfolded"

    StudentL "It's just the first day of school and you're making such a big deal about accidentally dropping your water container"
    StudentV "Well yeah, my girlfriend gave this to me. How would you feel if I wiped the make up off of your powdered face in front of-"
    StudentL "Take. that. {i}back.{/i}"
    StudentF "There is someone in front of us..."

    "As the other two's eyes slowly trail towards you, you look at a different direction, ignoring their presence in awkwardness"
    "From the side of your eye, you could see the other two brush themselves off and remained somewhat behave throughout the rest of the wait for the school's shuttle"
    "Although, you can still faintly hear murmuring and banter from the trio behind you"

    scene bg shuttlein with dissolve

    "As the shuttle arrived, you four make your way in the bus, with the three students behind you politely greeting the driver"
    "Must be practiced courtesy here on campus. You take a mental note of that"
    "As the shuttle begins to make its way to school, you can't help but wonder what this school is like"
    "Your Senior years were quite problematic with the people you tended to encounter. You just hope that this school isn't as bad"
    "Praying for a friend, an angel even, or whatever comes your way. First days are usually the more lonelier days"
    "Your thoughts were interrupted by the lingering conversation you can hear from the students before"

    StudentV "I have not eaten anything after helping out the community yesterday, I need something in my system STAT"
    StudentL "Lucky for you, I packed an extra Onigiri today, I'd hate to see you starve here"
    StudentF "Aww, thats sweet of you Lily. Didn't expect a sudden change of heart from you"
    StudentL "Shut it, Fred. Only doing this cuz I owe Vino for saving me from last night's game"
    StudentF "Ah...of course"
    StudentF "So, any plans today?"
    StudentV "Plan on helping out at the school's garden again, and maybe another bite to eat"

    "You watch as the taller student scowled down the Onigiri in hunger, seeming unsatisfied"

    StudentL "Manners."
    StudentV "You're one to talk"
    StudentF "If Kent was here, you would've bashed him"
    StudentL "Hehe, well you know me"
    StudentF "The poor guy barely gets out anymore, you could at least cut him some slack"
    StudentL "Hmmmmm...."
    StudentL "We'll see about that later"
    StudentL "Anyways,"
    StudentL "I was thinking of fixing the Guidance Office up for a bit, I gotta file some stuff for the new students. I love my job"
    StudentV "Girl please, that ain't even part of your internship"
    StudentL "But it's gonna look great on my resume~"

    "Oh right, the guidance office. You think to yourself as you stiffle a sigh"
    "You have to go there too to get some paperwork from your enrollment, alongside your schedule from admissions"

    "The shuttle made its stop at the front of the school's gates"
    "Passing by, you notice the numerous amounts of stalls right next to the benches at the parking lot"
    "Looking at them made you hungry"
    
    scene bg lobby with dissolve

    "You got up and waltzed your way through the guards that met you by the school's entrance"
    "Before anything, you head to your left to the admissions office to get your schedule"

    scene bg office with dissolve

    main "Uhh hi, my name is [mcName], I've come for my schedule for the day"
    "A friendly admission office worker approached you and handded you a specific folder she oddly handed to you as if she was expecting you"
    Admission "Ah, you must be the last one to recieve their schedule for the day! I've been expecting you"
    "Yeesh, you think to yourself. You didn't expect to be the last student to recieve their schedule"
    Admission "You could check your entire schedule and payments and such on our website, you know"
    main "Yeah sorry, I kinda enrolled late"
    Admission "It's alright, have a good day!"

    scene bg lobby with dissolve

    "You walk out of the admissions office, clutching the folder on your arm."
    "You check to see what the lady was talking about all your information being in their website"
    "To be fair, it was only faintly mentioned in your enrollment, either that or you haven't been paying good attention at things"
    "Checking your phone, you pull up the website and view your schedule from their"

    main "Huh...first class is at 9:00?"
    "You look at your phone's clock, it's currently 8:19"
    main "Well, I still got time to kill before class"
    main "There's a few places I haven't checked yet, maybe I could wander around before actually heading to class"

    call screen map
    
    return

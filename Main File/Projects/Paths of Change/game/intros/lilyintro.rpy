label lilyintro:

    if metLily == False:

        scene bg hall

        "You take the elevator up to the guidance office to get some paperwork needed for new enrollees"

        "You knocked on the door of the guidance office only to be met with silence.... after a few seconds have passed you knock again

        but this time you tried peeking into the small window of the guidance office to see if there is anyone inside just as you were

        about to leave a face of girl peeked into the same window you were peeking at jumpscaring you a bit"

        show lily flustered

        StudentL "Oh- I'm so sorry did I scare you? so sorry about that"

        show lily awkward

        "The girl sheepishly smiles. You notice that she is carrying lots of folders as well as pamphlets she reaches out 

        her hand to you"

        Lily "I'm really sorry about that. I'm Lily by the way and I do volunteer work here at the guidance office"

        show lily glad

        "You shake her hand and you introduce yourself. She smiles brightly"

        Lily "Nice to meet you [mcName] are you here to apply for internships?"

        show lily talk

        "You shake your head no"

        Lily "Oh- um- Are you here to do volunteer work?"

        "You shake your head again"

        Lily "job application?"

        "You shake your head again and before she continues asking, you say"

        main "I'm just here to get some requirements from the councellor"

        show lily flustered

        "Lily looks slightly embarrassed as she got conscious"

        Lily "sorry I tend to ramble a lot... but um- the councellor's not here yet if you want you can wait inside the office"

        "You both head into the office"

        scene bg guidance_office

        "Feeling a bit awkward you decided to make small talk by asking about the pamphlets Lily was holding"

        main "What are those pamphlets about?"

        show lily talk

        Lily "oh they're just seminars for people who are looking to take internships but at the same time the seminar also gives 
        advice to people who can't decide which course they'll take up for their career path."

        Lily "Would you like one?"

        "You take a pamphlet"

        "Lily then perks up like she remembered something she quickly checks her watch then mutters a curse"

        show lily flustered

        Lily "sorry to cut our conversation short but I have class in 5 so I should really get going-"

        Lily "you can wait here for the councellor"

        Lily "if you're interested in seminars and such you can come here to the office and ask for me."

        Lily "I'm really sorry I have to go- it was nice meeting you!"

        hide Lily with dissolve

        "Lily quickly runs out the office and rushes down the stairs"
        scene bg lobby
        $ metLily = True

        if metFred == True and metKent == True and metVino == True and metLily == True:
            "After watching Lily run off and getting your requirements, [mcName] decided to head to the lobby"
            jump metAll

        else:
            call screen map
            
    elif metLily == True:

        jump lilyleft

label lilyleft:
    scene bg office with dissolve
    "Lily left the office"
    scene bg lobby with dissolve
    call screen map

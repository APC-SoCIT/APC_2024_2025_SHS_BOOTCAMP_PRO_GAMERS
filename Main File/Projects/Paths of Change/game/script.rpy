label start:

    $ mcName = renpy.input("Enter your name", length = 32)
    if not mcName:
        $ mcName = "You"

    main "Hi im [mcName]"

    jump fredroute

    return

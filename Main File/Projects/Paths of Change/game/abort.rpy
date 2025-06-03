label abort:

    main "Who should I go with?"

    if all(metChars):
        jump abortAll

    elif abortFred == True and abortKent == True and abortVino == True:

            menu:
                "Head to Lily's Office":
                    jump lilyroute

    elif abortFred == True and abortKent == True and abortLily == True:

            menu:
                "Go to the park where Vino resides":
                    jump vinoroute
    
    elif abortFred == True and abortVino == True and abortLily == True:

            menu:
                "Message Kent to hang out":
                    jump kentroute

    elif abortKent == True and abortVino == True and abortLily == True:

            menu:
                "Take Fred's offer":
                    jump fredroute

    elif abortFred == True and abortKent == True:

        menu:
            "Head to Lily's Office":
                jump lilyroute
            "Go to the park where Vino resides":
                jump vinoroute

    elif abortFred == True and abortVino == True:

        menu:
            "Head to Lily's Office":
                jump lilyroute
            "Message Kent to hang out":
                jump kentroute

    elif abortFred == True and abortLily == True:

        menu:
            "Go to the park where Vino resides":
                jump vinoroute
            "Message Kent to hang out":
                jump kentroute

    elif abortKent == True and abortVino == True:

        menu:
            "Take Fred's offer":
                    jump fredroute
            "Head to Lily's Office":
                jump lilyroute

    elif abortKent == True and abortLily == True:

        menu:
            "Take Fred's offer":
                jump fredroute
            "Go to the park where Vino resides":
                jump vinoroute

    elif abortVino == True and abortLily == True:

        menu:
            "Take Fred's offer":
                jump fredroute
            "Message Kent to hang out":
                jump kentroute


    elif abortFred == True:

        menu:
            "Message Kent to hang out":
                jump kentroute
            "Head to Lily's Office":
                jump lilyroute
            "Go to the park where Vino resides":
                jump vinoroute

    elif abortKent == True:

        menu:
            "Take Fred's offer":
                jump fredroute
            "Head to Lily's Office":
                jump lilyroute
            "Go to the park where Vino resides":
                jump vinoroute

    elif abortVino == True:

        menu:
            "Take Fred's offer":
                jump fredroute
            "Head to Lily's Office":
                jump lilyroute
            "Message Kent to hang out":
                jump kentroute

    elif abortLily == True:

        menu:
            "Take Fred's offer":
                jump fredroute
            "Message Kent to hang out":
                jump kentroute
            "Go to the park where Vino resides":
                jump vinoroute

    
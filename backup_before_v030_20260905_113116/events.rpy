# ============================================================
# STORY EVENTS
# Each event is small, self-contained and triggered by systems.rpy.
# ============================================================

label ev_aya_intro:
    $ mark_event("aya_intro")
    $ quests["aya_charm"] = "active"

    "A courier nearly collides with you while crossing the square."

    aya "You're the one who just came back to the village, right?"
    mc "That's me."

    aya "Then maybe you can help. I lost a silver charm near the river."

    menu:
        "How do you answer?"

        "I'll help you find it.":
            $ change_relation("aya", "love", 1)
            aya "Thanks. I owe you."

        "Only if you can keep up with me later.":
            $ change_relation("aya", "hatred", 1)
            aya "You're already annoying. Fine."

    $ spend_time(1)
    jump map

label ev_find_charm:
    $ mark_event("find_charm")
    $ add_item("Silver Charm")

    "Between the river stones, something reflects the light."
    "You found a Silver Charm."

    $ spend_time(1)
    jump map

label ev_return_charm:
    $ mark_event("return_charm")
    $ remove_item("Silver Charm")
    $ quests["aya_charm"] = "complete"
    $ flags["aya_charm_returned"] = True
    $ reputation += 1

    aya "You found it?"

    menu:
        "Hand it over without asking for anything":
            $ change_relation("aya", "love", 2)
            aya "I underestimated you."

        "Make her admit you won":
            $ change_relation("aya", "hatred", 2)
            aya "Fine. You win this round."

    "Quest completed: The Lost Charm."
    "Reputation +1."

    $ spend_time(1)
    jump map

label ev_ren_intro:
    $ mark_event("ren_intro")

    "A lone instructor is practicing precise strikes."

    ren "Watching won't make you stronger."

    menu:
        "Ask him to teach you":
            $ change_relation("ren", "love", 1)
            ren "Then start with discipline."

        "Tell him you can keep up":
            $ change_relation("ren", "hatred", 1)
            ren "We'll see."

    $ spend_time(1)
    jump map

label ev_aya_house_invite:
    $ mark_event("aya_house_invite")
    $ unlocked_locations["aya_house"] = True

    aya "You kept your word, and you didn't make a big deal out of it."
    aya "If you're around later, come by my place. There's something I could use help with."

    "New location unlocked: Aya's Household."

    $ spend_time(1)
    jump map

label ev_rooftop_test:
    $ mark_event("rooftop_test")

    "As the Square empties for the night, a messenger approaches."

    "Messenger" "People have noticed you've been helping around the village."
    "Messenger" "There's a small assignment available for someone with a decent reputation."

    if strength >= 3:
        "Your Strength is high enough to unlock the direct approach."
        $ coins += 20
        $ reputation += 1
        "You complete the assignment successfully. Coins +20. Reputation +1."
    else:
        "You can accept the assignment later, but more training may create another option."
        $ flags["rooftop_assignment_pending"] = True

    $ spend_time(1)
    jump map



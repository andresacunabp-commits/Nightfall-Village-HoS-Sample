# ============================================================
# STORY EVENTS v0.3
# Self-contained narrative nodes triggered by systems.rpy.
# ============================================================

label ev_aya_intro:
    $ mark_event("aya_intro")
    $ quests["aya_charm"] = "active"

    "A courier nearly collides with you in the Square."

    aya "You're the one who came back to the village, right?"
    mc "That's me."
    aya "Then maybe you can help. I lost a silver charm near the river."

    menu:
        "How do you answer?"

        "I'll help you find it.":
            $ change_relation("aya", "love", 1)
            aya "Thanks. I owe you."

        "Only if you admit I'm faster.":
            $ change_relation("aya", "hatred", 1)
            aya "You're already annoying. Fine."

    $ spend_time(1)
    jump map

label ev_find_charm:
    $ mark_event("find_charm")
    $ add_item("Silver Charm")

    "Something catches the light between the river stones."
    "You found Aya's Silver Charm."

    $ spend_time(1)
    jump map

label ev_return_charm:
    $ mark_event("return_charm")
    $ remove_item("Silver Charm")
    $ quests["aya_charm"] = "complete"
    $ flags["aya_charm_returned"] = True
    $ change_stat("reputation", 1)

    aya "You actually found it?"

    menu:
        "Return it without asking for anything":
            $ change_relation("aya", "love", 2)
            aya "I underestimated you."

        "Make her admit you won":
            $ change_relation("aya", "hatred", 2)
            aya "Fine. You win this round."

    "Quest complete: The Lost Charm."
    $ spend_time(1)
    jump map

label ev_ren_intro:
    $ mark_event("ren_intro")
    $ flags["ren_met"] = True

    "A lone instructor practices precise strikes."

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

label ev_night_trader_intro:
    $ mark_event("night_trader_intro")

    "Most of the Market is closed, but one narrow stall is still lit."

    sora "People who wander after dark are either lost or looking for something."
    mc "Which one am I?"
    sora "Come back enough times and I might decide."

    $ sora_trust = 1
    $ spend_time(1)
    jump map

label ev_aya_house_invite:
    $ mark_event("aya_house_invite")
    $ unlock_location("aya_house")

    aya "You kept your word. And you didn't make a spectacle of it."
    aya "Come by my place sometime. I could use another set of eyes on something."

    $ spend_time(1)
    jump map

label ev_shrine_rumor:
    $ mark_event("shrine_rumor")
    $ unlock_location("old_shrine")

    "Two residents lower their voices as you pass."

    "Resident" "The old shrine path is open again. I still wouldn't go there after dark."
    "Resident" "Especially not if you find one of those strange moon-marked tokens."

    "New location discovered: Old Shrine."

    $ spend_time(1)
    jump map

label ev_ren_spar:
    $ mark_event("ren_spar")

    ren "Your stance isn't terrible anymore."
    mc "That's almost a compliment."

    menu:
        "Fight carefully":
            $ change_relation("ren", "love", 1)
            $ change_stat("reputation", 1)
            ren "Good. You listened."

        "Try to overpower him":
            $ change_relation("ren", "hatred", 1)
            $ change_stat("strength", 1)
            ren "Reckless. But stronger."

    $ coins += 10
    "Ren tosses you a small training reward: 10 coins."
    $ spend_time(1)
    jump map

label ev_archive_discovery:
    $ mark_event("archive_discovery")
    $ remove_item("Moon Token")
    $ flags["moon_token_used"] = True
    $ unlock_location("archive")

    "The Moon Token fits into a circular recess behind the shrine."
    "Stone grinds against stone."
    "A narrow stairway descends beneath the old structure."

    "New location unlocked: Hidden Archive."

    $ spend_time(1)
    jump map

label ev_archive_love_echo:
    $ mark_event("archive_love_echo")

    "Among the records is a journal about two operatives who survived because they learned to trust one another."
    "Your choices with Aya give the entry a different weight."

    $ change_relation("aya", "love", 1)
    $ spend_time(1)
    jump map

label ev_archive_hatred_echo:
    $ mark_event("archive_hatred_echo")

    "One record describes a partnership destroyed by escalating competition."
    "It feels uncomfortably relevant."

    $ change_relation("aya", "hatred", 1)
    $ spend_time(1)
    jump map

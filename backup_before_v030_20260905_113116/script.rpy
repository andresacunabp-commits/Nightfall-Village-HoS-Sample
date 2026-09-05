# ============================================================
# MAIN FLOW
# ============================================================

define mc = Character("You", color="#8bd5ff")
define aya = Character("Aya", color="#ff9fd2")
define ren = Character("Ren", color="#9dffb5")
define merchant = Character("Merchant", color="#f4d38a")

label start:
    scene black
    with fade

    "NIGHTFALL VILLAGE"
    "Sandbox Systems Demo â€” Portfolio Build 0.2"

    "This project is an original technical demo focused on systems used by non-linear sandbox visual novels."

    mc "A new assignment has brought me back to Nightfall Village."
    mc "I can choose where to go, who to meet, and how to spend each part of the day."

    jump map

label map:
    if energy <= 0:
        jump forced_rest

    call screen world_map
    jump map

label resolve_location_event(location_id):
    $ _event_label = next_event_for(location_id)

    if _event_label:
        $ renpy.jump(_event_label)

    return

# ============================================================
# HOME
# ============================================================

label loc_home:
    scene black
    "You return home."

    menu:
        "What do you want to do?"

        "Check the interactive guide":
            call screen guide_screen(close_action=Return())
            jump loc_home

        "Rest for this time period":
            "You take some time to recover."
            $ energy = min(3, energy + 1)
            $ spend_time(0)
            jump map

        "Sleep until the next morning":
            jump sleep_until_morning

        "Return to map":
            jump map

label sleep_until_morning:
    scene black
    with fade
    "You end Day [day]."
    $ start_new_day()
    "Day [day] begins."
    jump map

label forced_rest:
    scene black
    "You're too tired to continue today."
    $ start_new_day()
    "After resting, Day [day] begins."
    jump map

# ============================================================
# SQUARE
# ============================================================

label loc_square:
    scene black
    "Village Square â€” [period_name()]"

    call resolve_location_event("square")

    $ aya_here = npc_location("aya") == "square"
    $ ren_here = npc_location("ren") == "square"

    menu:
        "What do you do?"

        "Talk to Aya" if aya_here:
            jump square_talk_aya

        "Talk to Ren" if ren_here:
            ren "Still wandering around? Keep your eyes open. Schedules matter."
            $ change_relation("ren", "love", 1)
            $ spend_time(1)
            jump map

        "Help with village errands":
            "You spend some time helping local merchants and residents."
            $ reputation += 1
            $ coins += 5
            $ spend_time(1)
            jump map

        "Return to map":
            jump map

label square_talk_aya:
    if dominant_route("aya") == "Love":
        aya "You always show up when people need you."
    elif dominant_route("aya") == "Hatred":
        aya "Still trying to prove you're better than me?"
    else:
        aya "You're difficult to read."

    menu:
        "Choose your approach"

        "Be supportive":
            mc "You don't have to handle everything alone."
            $ change_relation("aya", "love", 1)
            aya "I'll remember that."

        "Challenge her":
            mc "If you want my respect, earn it."
            $ change_relation("aya", "hatred", 1)
            aya "Good. I prefer honesty."

        "Leave":
            pass

    $ spend_time(1)
    jump map

# ============================================================
# TRAINING
# ============================================================

label loc_training:
    scene black
    "Training Ground â€” [period_name()]"

    call resolve_location_event("training")

    menu:
        "What do you do?"

        "Strength training" if energy > 0:
            "You complete a demanding training session."
            $ strength += 1
            $ spend_time(1)

            if strength == 3:
                "Your Strength reached 3. New stat-gated events may now become available."

            jump map

        "Talk to Ren" if npc_location("ren") == "training":
            ren "Consistency matters more than showing off."
            $ change_relation("ren", "love", 1)
            $ spend_time(1)
            jump map

        "Return to map":
            jump map

# ============================================================
# MARKET
# ============================================================

label loc_market:
    scene black
    "Market Alley â€” [period_name()]"

    merchant "Need something?"

    menu market_menu:
        "Flowers â€” 10 coins" if coins >= 10:
            $ coins -= 10
            $ add_item("Flowers")
            merchant "Fresh enough."
            jump market_menu

        "Energy Snack â€” 8 coins" if coins >= 8:
            $ coins -= 8
            $ add_item("Energy Snack")
            merchant "Don't waste it."
            jump market_menu

        "Use Energy Snack" if has_item("Energy Snack"):
            $ remove_item("Energy Snack")
            $ energy = min(3, energy + 1)
            "You recover some energy."
            jump market_menu

        "Leave":
            jump map

# ============================================================
# RIVERSIDE
# ============================================================

label loc_riverside:
    scene black
    "Riverside â€” [period_name()]"

    call resolve_location_event("riverside")

    if npc_location("aya") == "riverside":
        aya "I come here when the village gets too loud."

        menu:
            "Sit quietly with her":
                $ change_relation("aya", "love", 1)
                "Neither of you says much, but the silence feels comfortable."

            "Turn it into a competition":
                $ change_relation("aya", "hatred", 1)
                aya "A race back to the bridge? You're on."

            "Leave her alone":
                pass

        $ spend_time(1)
        jump map

    "Nothing unusual catches your attention."
    $ spend_time(1)
    jump map

# ============================================================
# AYA HOUSE â€” UNLOCKED STORY LOCATION
# ============================================================

label loc_aya_house:
    scene black
    "Aya's Household â€” [period_name()]"

    if not is_location_unlocked("aya_house"):
        "You don't know where Aya lives yet."
        jump map

    $ stage = event_stages.get("aya_house_visit", 0)

    if stage == 0:
        "This is your first visit."
        aya "You actually came."

        menu:
            "Thank her for the invitation":
                $ change_relation("aya", "love", 1)
                aya "Don't make me regret it."

            "Tease her about the formal invitation":
                $ change_relation("aya", "hatred", 1)
                aya "Keep talking and I'll throw you back outside."

        $ event_stages["aya_house_visit"] = 1

    elif stage == 1:
        "On your second visit, Aya is sorting mission reports."

        menu:
            "Offer to help":
                $ change_relation("aya", "love", 1)
                $ reputation += 1
                "Working together reveals more about how she approaches problems."

            "Try to finish the reports faster than her":
                $ change_relation("aya", "hatred", 1)
                "The work turns into a competitive challenge."

        $ event_stages["aya_house_visit"] = 2

    else:
        if dominant_route("aya") == "Love":
            aya "You're becoming part of my routine."
        elif dominant_route("aya") == "Hatred":
            aya "I was wondering when you'd come looking for another challenge."
        else:
            aya "Back again?"

        "This repeatable visit changes dialogue according to relationship state."

    $ spend_time(1)
    jump map



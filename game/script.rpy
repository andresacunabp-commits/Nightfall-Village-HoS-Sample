# ============================================================
# NIGHTFALL VILLAGE — MAIN FLOW v0.3
# ============================================================

define mc = Character("You", color="#89d8ff")
define aya = Character("Aya", color="#ff9db6")
define ren = Character("Ren", color="#a6f4c5")
define merchant = Character("Merchant", color="#ffd184")
define sora = Character("Sora", color="#c9a8ff")

label start:
    scene bg_main
    with fade

    centered "{size=54}{b}NIGHTFALL VILLAGE{/b}{/size}\n{size=24}Shinobi Sandbox Systems Demo{/size}"
    pause 0.8

    mc "A new assignment has brought me back to Nightfall Village."
    mc "Here, time matters. People move. Opportunities appear and disappear."
    mc "What I do — and how I treat people — will decide which paths open."

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
    scene bg_home
    with dissolve

    "You return home."

    menu:
        "What do you want to do?"

        "Review the Interactive Guide":
            call screen guide_screen(close_action=Return())
            jump loc_home

        "Review event progress":
            call screen gallery_screen(close_action=Return())
            jump loc_home

        "Rest for one time period":
            "You take some time to recover."
            $ energy = min(4, energy + 1)
            $ spend_time(0)
            jump map

        "Sleep until the next morning":
            jump sleep_until_morning

        "Return to map":
            jump map

label sleep_until_morning:
    scene bg_home
    with fade
    "You call it a day."
    $ start_new_day()
    "Morning arrives over Nightfall Village."
    jump map

label forced_rest:
    scene bg_home
    with fade
    "You've run out of energy for today."
    $ start_new_day()
    "After a full night's rest, you wake up ready to continue."
    jump map

# ============================================================
# VILLAGE SQUARE
# ============================================================

label loc_square:
    scene bg_square
    with dissolve

    "Village Square — [period_name()]"

    call resolve_location_event("square")

    $ aya_here = npc_location("aya") == "square"
    $ ren_here = npc_location("ren") == "square"

    menu:
        "What do you do?"

        "Talk to Aya" if aya_here:
            jump square_talk_aya

        "Talk to Ren" if ren_here:
            ren "The village looks calm. That usually means someone isn't paying attention."
            $ change_relation("ren", "love", 1)
            $ spend_time(1)
            jump map

        "Help with village errands":
            "You spend time helping residents carry supplies and repair a damaged stall."
            $ change_stat("reputation", 1)
            $ coins += 6
            "You earn 6 coins."
            $ spend_time(1)
            jump map

        "Observe the crowd":
            if flags.get("aya_charm_returned", False):
                "You overhear people discussing Aya's recent delivery route. The world is already reacting to what happened."
            else:
                "Nothing important stands out yet."
            $ spend_time(1)
            jump map

        "Return to map":
            jump map

label square_talk_aya:
    if dominant_route("aya") == "Love":
        aya "You keep finding reasons to check on me."
    elif dominant_route("aya") == "Hatred":
        aya "Here to compete again? Fine. Try not to fall behind."
    else:
        aya "You're difficult to read."

    menu:
        "Choose your approach."

        "Be supportive":
            mc "You don't have to handle everything alone."
            $ change_relation("aya", "love", 1)
            aya "I'll remember that."

        "Push her buttons":
            mc "You'd be faster if you spent less time arguing."
            $ change_relation("aya", "hatred", 1)
            aya "Keep talking. You're making this interesting."

        "Give her flowers" if has_item("Flowers"):
            $ remove_item("Flowers")
            $ change_relation("aya", "love", 2)
            aya "You planned this? ...Thanks."

        "Leave":
            pass

    $ spend_time(1)
    jump map

# ============================================================
# TRAINING GROUND
# ============================================================

label loc_training:
    scene bg_training
    with dissolve

    "Training Ground — [period_name()]"

    call resolve_location_event("training")

    menu:
        "What do you do?"

        "Strength training" if energy > 0:
            "You complete a demanding training routine."
            $ change_stat("strength", 1)
            $ spend_time(1)
            jump map

        "Talk to Ren" if npc_location("ren") == "training":
            ren "Technique first. Speed comes after."
            $ change_relation("ren", "love", 1)
            $ spend_time(1)
            jump map

        "Return to map":
            jump map

# ============================================================
# MARKET
# ============================================================

label loc_market:
    scene bg_market
    with dissolve

    "Market Alley — [period_name()]"

    call resolve_location_event("market")

    if npc_location("sora") == "market":
        jump night_market_menu

    merchant "Need supplies?"

    menu market_day_menu:
        "Flowers — 10 coins" if coins >= 10:
            $ coins -= 10
            $ add_item("Flowers")
            merchant "Fresh from the eastern gardens."
            jump market_day_menu

        "Energy Snack — 8 coins" if coins >= 8:
            $ coins -= 8
            $ add_item("Energy Snack")
            merchant "Good for a long day."
            jump market_day_menu

        "Use Energy Snack" if has_item("Energy Snack"):
            $ remove_item("Energy Snack")
            $ energy = min(4, energy + 1)
            "You recover 1 energy."
            jump market_day_menu

        "Leave":
            jump map

label night_market_menu:
    sora "The regular shops close. Mine opens."

    menu:
        "Talk":
            if sora_trust < 3:
                sora "Bring me stories, favors, and proof that you notice what everyone else ignores."
                $ sora_trust += 1
                "Sora Trust +1"
            else:
                sora "You've been useful. That makes you interesting."
            $ spend_time(1)
            jump map

        "Buy Moon Token — 25 coins" if sora_trust >= 3 and coins >= 25 and not has_item("Moon Token") and not flags.get("moon_token_used", False):
            $ coins -= 25
            $ add_item("Moon Token")
            sora "It opens something. I won't tell you what."
            $ spend_time(1)
            jump map

        "Buy Energy Snack — 6 coins" if coins >= 6:
            $ coins -= 6
            $ add_item("Energy Snack")
            jump night_market_menu

        "Leave":
            jump map

# ============================================================
# RIVERSIDE
# ============================================================

label loc_riverside:
    scene bg_riverside
    with dissolve

    "Riverside — [period_name()]"

    call resolve_location_event("riverside")

    if npc_location("aya") == "riverside":
        aya "This place is quieter than the Square."

        menu:
            "Sit with her":
                $ change_relation("aya", "love", 1)
                "For a while, neither of you needs to say anything."

            "Challenge her to a race":
                $ change_relation("aya", "hatred", 1)
                aya "First one to the old bridge wins."

            "Leave her alone":
                pass

        $ spend_time(1)
        jump map

    "The river carries the village lights downstream."
    $ spend_time(1)
    jump map

# ============================================================
# AYA HOUSE
# ============================================================

label loc_aya_house:
    scene bg_aya_house
    with dissolve

    if not is_location_unlocked("aya_house"):
        "You haven't unlocked this location."
        jump map

    "Aya's Household — [period_name()]"

    $ stage = event_stages.get("aya_house_visit", 0)

    if stage == 0:
        aya "You actually came."

        menu:
            "Thank her for the invitation":
                $ change_relation("aya", "love", 1)
                aya "Don't make me regret it."

            "Tease her about inviting you":
                $ change_relation("aya", "hatred", 1)
                aya "You're unbearable."

        $ event_stages["aya_house_visit"] = 1

    elif stage == 1:
        "Aya is sorting mission reports across the table."

        menu:
            "Offer to help":
                $ change_relation("aya", "love", 1)
                $ change_stat("reputation", 1)
                "Working together reveals more about how she approaches problems."

            "Turn it into a competition":
                $ change_relation("aya", "hatred", 1)
                "The paperwork somehow becomes a race."

            "Inspect a strange drawer":
                if not has_item("Old Key"):
                    $ add_item("Old Key")
                    "You quietly find an Old Key hidden beneath a stack of reports."
                else:
                    "You've already searched here."

        $ event_stages["aya_house_visit"] = 2

    else:
        if dominant_route("aya") == "Love":
            aya "You're becoming part of my routine."
        elif dominant_route("aya") == "Hatred":
            aya "I knew you'd come looking for another challenge."
        else:
            aya "Back again?"

        "This repeatable scene changes according to your relationship history."

    $ spend_time(1)
    jump map

# ============================================================
# OLD SHRINE
# ============================================================

label loc_old_shrine:
    scene bg_old_shrine
    with dissolve

    if not is_location_unlocked("old_shrine"):
        "You don't know how to reach this place yet."
        jump map

    "Old Shrine — [period_name()]"

    call resolve_location_event("old_shrine")

    menu:
        "Search the grounds":
            if not flags.get("shrine_searched", False):
                $ flags["shrine_searched"] = True
                $ coins += 10
                "You discover a weathered cache with 10 coins."
            else:
                "You've already searched the obvious hiding places."
            $ spend_time(1)
            jump map

        "Return to map":
            jump map

# ============================================================
# HIDDEN ARCHIVE
# ============================================================

label loc_archive:
    scene bg_archive
    with dissolve

    if not is_location_unlocked("archive"):
        "This location is still hidden."
        jump map

    "Hidden Archive — [period_name()]"

    call resolve_location_event("archive")

    if dominant_route("aya") == "Love":
        "The notes you find here make you think about the trust you've built."
    elif dominant_route("aya") == "Hatred":
        "The notes you find here feel like fuel for a rivalry that has gone too far."
    else:
        "The archive contains fragments of stories that still lack context."

    $ spend_time(1)
    jump map

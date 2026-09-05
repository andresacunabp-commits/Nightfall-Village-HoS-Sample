# ============================================================
# NIGHTFALL VILLAGE — SANDBOX SYSTEMS v0.3
# Original portfolio architecture inspired by large sandbox VNs.
# ============================================================

init python:
    PERIODS = ("Morning", "Afternoon", "Evening", "Night")

    LOCATION_ORDER = (
        "home", "square",
        "training", "market",
        "riverside", "aya_house",
        "old_shrine", "archive",
    )

    LOCATION_DATA = {
        "home": {
            "name": "Home",
            "label": "loc_home",
            "description": "Rest, review objectives, and prepare for the next day.",
            "icon": "⌂",
        },
        "square": {
            "name": "Village Square",
            "label": "loc_square",
            "description": "The social center. Storylines and schedules often cross here.",
            "icon": "◇",
        },
        "training": {
            "name": "Training Ground",
            "label": "loc_training",
            "description": "Raise Strength and train with Ren.",
            "icon": "⚔",
        },
        "market": {
            "name": "Market Alley",
            "label": "loc_market",
            "description": "Buy supplies by day. Someone unusual appears after dark.",
            "icon": "¤",
        },
        "riverside": {
            "name": "Riverside",
            "label": "loc_riverside",
            "description": "A quiet place for exploration and private conversations.",
            "icon": "≈",
        },
        "aya_house": {
            "name": "Aya's Household",
            "label": "loc_aya_house",
            "description": "A relationship-gated location with multi-stage visits.",
            "icon": "⌂",
        },
        "old_shrine": {
            "name": "Old Shrine",
            "label": "loc_old_shrine",
            "description": "An abandoned shrine outside the busy streets.",
            "icon": "△",
        },
        "archive": {
            "name": "Hidden Archive",
            "label": "loc_archive",
            "description": "A secret location unlocked by exploration and items.",
            "icon": "▣",
        },
    }

    CHARACTER_DATA = {
        "aya": {
            "name": "Aya",
            "description": "A guarded courier whose storyline can develop through Love or Hatred.",
        },
        "ren": {
            "name": "Ren",
            "description": "A disciplined instructor tied to Strength progression.",
        },
        "sora": {
            "name": "Sora",
            "description": "A mysterious night trader tied to hidden items and exploration.",
        },
    }

    EVENT_DATA = [
        {
            "id": "aya_intro",
            "title": "A Courier's Request",
            "label": "ev_aya_intro",
            "location": "square",
            "times": ("Morning", "Afternoon"),
            "min_day": 1,
            "priority": 100,
            "once": True,
        },
        {
            "id": "find_charm",
            "title": "Something in the Water",
            "label": "ev_find_charm",
            "location": "riverside",
            "times": ("Morning", "Afternoon", "Evening"),
            "priority": 95,
            "once": True,
            "quest": ("aya_charm", "active"),
        },
        {
            "id": "return_charm",
            "title": "Return the Charm",
            "label": "ev_return_charm",
            "location": "square",
            "times": ("Morning", "Afternoon", "Evening"),
            "priority": 120,
            "once": True,
            "quest": ("aya_charm", "active"),
            "requires_item": ("Silver Charm", 1),
        },
        {
            "id": "ren_intro",
            "title": "The Instructor",
            "label": "ev_ren_intro",
            "location": "training",
            "times": ("Morning", "Afternoon"),
            "priority": 90,
            "once": True,
        },
        {
            "id": "night_trader_intro",
            "title": "The Night Trader",
            "label": "ev_night_trader_intro",
            "location": "market",
            "times": ("Night",),
            "min_day": 2,
            "min_stat": ("reputation", 1),
            "priority": 100,
            "once": True,
        },
        {
            "id": "aya_house_invite",
            "title": "An Unexpected Invitation",
            "label": "ev_aya_house_invite",
            "location": "square",
            "times": ("Afternoon", "Evening"),
            "min_day": 2,
            "priority": 105,
            "once": True,
            "requires_flag": "aya_charm_returned",
            "min_relation": ("aya", "love", 3),
        },
        {
            "id": "shrine_rumor",
            "title": "Whispers of an Old Shrine",
            "label": "ev_shrine_rumor",
            "location": "square",
            "times": ("Evening", "Night"),
            "min_day": 2,
            "min_stat": ("reputation", 2),
            "priority": 70,
            "once": True,
        },
        {
            "id": "ren_spar",
            "title": "A Serious Spar",
            "label": "ev_ren_spar",
            "location": "training",
            "times": ("Afternoon", "Evening"),
            "min_day": 2,
            "min_stat": ("strength", 3),
            "requires_flag": "ren_met",
            "priority": 80,
            "once": True,
        },
        {
            "id": "archive_discovery",
            "title": "Behind the Stone Door",
            "label": "ev_archive_discovery",
            "location": "old_shrine",
            "times": ("Night",),
            "min_day": 3,
            "requires_item": ("Moon Token", 1),
            "priority": 110,
            "once": True,
        },
        {
            "id": "archive_love_echo",
            "title": "An Echo of Trust",
            "label": "ev_archive_love_echo",
            "location": "archive",
            "times": ("Evening", "Night"),
            "min_day": 3,
            "min_relation": ("aya", "love", 5),
            "priority": 80,
            "once": True,
        },
        {
            "id": "archive_hatred_echo",
            "title": "An Echo of Conflict",
            "label": "ev_archive_hatred_echo",
            "location": "archive",
            "times": ("Evening", "Night"),
            "min_day": 3,
            "min_relation": ("aya", "hatred", 5),
            "priority": 80,
            "once": True,
        },
    ]

    def period_name():
        return PERIODS[store.period_index]

    def is_location_unlocked(location_id):
        return bool(store.unlocked_locations.get(location_id, False))

    def has_item(item_name, qty=1):
        return store.inventory.get(item_name, 0) >= qty

    def add_item(item_name, qty=1, notify=True):
        store.inventory[item_name] = store.inventory.get(item_name, 0) + qty
        if notify:
            renpy.notify("{} +{}".format(item_name, qty))

    def remove_item(item_name, qty=1):
        if not has_item(item_name, qty):
            return False
        new_qty = store.inventory.get(item_name, 0) - qty
        if new_qty <= 0:
            store.inventory.pop(item_name, None)
        else:
            store.inventory[item_name] = new_qty
        return True

    def relation(character_id, route):
        return store.relationships.get(character_id, {}).get(route, 0)

    def change_relation(character_id, route, amount, notify=True):
        if character_id not in store.relationships:
            store.relationships[character_id] = {"love": 0, "hatred": 0}
        old = store.relationships[character_id].get(route, 0)
        new = max(0, min(10, old + amount))
        store.relationships[character_id][route] = new
        if notify and amount:
            display_name = CHARACTER_DATA.get(character_id, {}).get("name", character_id.title())
            sign = "+" if amount > 0 else ""
            renpy.notify("{} {} {}{}".format(display_name, route.title(), sign, amount))

    def dominant_route(character_id):
        love = relation(character_id, "love")
        hatred = relation(character_id, "hatred")
        if love >= 4 and love > hatred:
            return "Love"
        if hatred >= 4 and hatred > love:
            return "Hatred"
        return "Undecided"

    def change_stat(stat_name, amount, notify=True):
        old = getattr(store, stat_name, 0)
        new = max(0, old + amount)
        setattr(store, stat_name, new)
        if notify and amount:
            sign = "+" if amount > 0 else ""
            renpy.notify("{} {}{}".format(stat_name.title(), sign, amount))

    def spend_time(cost=1):
        store.energy = max(0, store.energy - cost)
        if store.period_index < len(PERIODS) - 1:
            store.period_index += 1
        else:
            start_new_day()

    def start_new_day():
        store.day += 1
        store.period_index = 0
        store.energy = 4
        store.daily_flags = {}
        renpy.notify("Day {} — Morning".format(store.day))

    def npc_location(character_id):
        p = period_name()

        if character_id == "aya":
            if is_location_unlocked("aya_house") and p == "Night":
                return "aya_house"
            if p in ("Morning", "Afternoon"):
                return "square"
            if p == "Evening":
                return "riverside"
            return None

        if character_id == "ren":
            if p in ("Morning", "Afternoon"):
                return "training"
            if p == "Evening":
                return "square"
            return None

        if character_id == "sora":
            if p == "Night" and store.seen_events.get("night_trader_intro", False):
                return "market"
            return None

        return None

    def residents_at(location_id):
        names = []
        for cid in CHARACTER_DATA:
            if npc_location(cid) == location_id:
                names.append(CHARACTER_DATA[cid]["name"])
        return ", ".join(names)

    def _event_requirement_reason(ev):
        if store.day < ev.get("min_day", 1):
            return "Requires Day {}+".format(ev.get("min_day", 1))

        if period_name() not in ev.get("times", PERIODS):
            return "Wrong time: {}".format("/".join(ev.get("times", PERIODS)))

        if ev.get("once") and store.seen_events.get(ev["id"], False):
            return "Already completed"

        flag = ev.get("requires_flag")
        if flag and not store.flags.get(flag, False):
            return "Missing flag: {}".format(flag)

        quest = ev.get("quest")
        if quest:
            qid, required_state = quest
            if store.quests.get(qid) != required_state:
                return "Quest {} must be {}".format(qid, required_state)

        item = ev.get("requires_item")
        if item:
            item_name, qty = item
            if not has_item(item_name, qty):
                return "Needs {} x{}".format(item_name, qty)

        rel = ev.get("min_relation")
        if rel:
            cid, route, amount = rel
            if relation(cid, route) < amount:
                return "{} {} must be {}+".format(CHARACTER_DATA[cid]["name"], route.title(), amount)

        stat = ev.get("min_stat")
        if stat:
            stat_name, amount = stat
            if getattr(store, stat_name, 0) < amount:
                return "{} must be {}+".format(stat_name.title(), amount)

        return "AVAILABLE"

    def event_is_available(ev):
        return _event_requirement_reason(ev) == "AVAILABLE"

    def next_event_for(location_id):
        candidates = [
            ev for ev in EVENT_DATA
            if ev["location"] == location_id and event_is_available(ev)
        ]
        if not candidates:
            return None
        candidates.sort(key=lambda e: e.get("priority", 0), reverse=True)
        return candidates[0]["label"]

    def location_has_event(location_id):
        return next_event_for(location_id) is not None

    def mark_event(event_id):
        store.seen_events[event_id] = True

    def unlock_location(location_id):
        if not store.unlocked_locations.get(location_id, False):
            store.unlocked_locations[location_id] = True
            renpy.notify("Location unlocked: {}".format(LOCATION_DATA[location_id]["name"]))

    def guide_objectives():
        objectives = []

        if store.quests.get("aya_charm") == "locked":
            objectives.append(("AYA", "Visit the Village Square during Morning or Afternoon."))
        elif store.quests.get("aya_charm") == "active" and not has_item("Silver Charm"):
            objectives.append(("AYA", "Search a quiet location near the water."))
        elif store.quests.get("aya_charm") == "active" and has_item("Silver Charm"):
            objectives.append(("AYA", "Return to the Village Square before night."))
        elif store.quests.get("aya_charm") == "complete" and not is_location_unlocked("aya_house"):
            objectives.append(("AYA", "Raise Aya's Love to 3 and revisit the Square later in the day."))
        else:
            route = dominant_route("aya")
            objectives.append(("AYA", "Current route: {}. Revisit her at different times.".format(route)))

        if not store.seen_events.get("ren_intro"):
            objectives.append(("REN", "Visit the Training Ground during the day."))
        elif store.strength < 3:
            objectives.append(("TRAINING", "Raise Strength to 3 to unlock a new event."))
        elif not store.seen_events.get("ren_spar"):
            objectives.append(("TRAINING", "Return to the Training Ground in the Afternoon or Evening."))

        if not store.seen_events.get("night_trader_intro"):
            if store.reputation < 1:
                objectives.append(("MARKET", "Raise Reputation, then explore the Market at Night."))
            else:
                objectives.append(("MARKET", "Explore the Market at Night."))
        elif not has_item("Moon Token") and not store.flags.get("moon_token_used", False):
            objectives.append(("MARKET", "Build Sora's trust and obtain a Moon Token."))

        if not is_location_unlocked("old_shrine"):
            objectives.append(("VILLAGE", "Raise Reputation to 2 and listen for rumors in the Square after sunset."))
        elif not is_location_unlocked("archive"):
            objectives.append(("SECRETS", "Investigate the Old Shrine at Night with the right item."))
        else:
            objectives.append(("SECRETS", "The Hidden Archive may react to your relationship route."))

        return objectives

    def inventory_lines():
        if not store.inventory:
            return ["Empty"]
        return ["{} x{}".format(name, qty) for name, qty in sorted(store.inventory.items())]

    def completion_count():
        return sum(1 for ev in EVENT_DATA if store.seen_events.get(ev["id"], False))

    def completion_percent():
        if not EVENT_DATA:
            return 0
        return int((completion_count() * 100.0) / len(EVENT_DATA))

    # ----------------------
    # Developer tools
    # ----------------------
    def debug_change_day(amount):
        store.day = max(1, store.day + amount)

    def debug_change_period(amount):
        store.period_index = max(0, min(len(PERIODS) - 1, store.period_index + amount))

    def debug_change_energy(amount):
        store.energy = max(0, min(4, store.energy + amount))

    def debug_change_coins(amount):
        store.coins = max(0, store.coins + amount)

    def debug_change_stat(stat_name, amount):
        change_stat(stat_name, amount, notify=False)

    def debug_change_relation(character_id, route, amount):
        change_relation(character_id, route, amount, notify=False)

    def debug_toggle_flag(flag_name):
        store.flags[flag_name] = not store.flags.get(flag_name, False)

    def debug_toggle_location(location_id):
        store.unlocked_locations[location_id] = not store.unlocked_locations.get(location_id, False)

    def debug_add_item(item_name):
        add_item(item_name, 1, notify=False)

    def event_debug_rows():
        rows = []
        for ev in EVENT_DATA:
            reason = _event_requirement_reason(ev)
            rows.append((ev["title"], LOCATION_DATA[ev["location"]]["name"], reason, ev["label"]))
        return rows

# --------------------
# Save-game state
# --------------------

default day = 1
default period_index = 0
default energy = 4
default coins = 30
default strength = 0
default reputation = 0
default sora_trust = 0

default inventory = {}
default flags = {}
default daily_flags = {}
default seen_events = {}
default event_stages = {}

default quests = {
    "aya_charm": "locked",
}

default relationships = {
    "aya": {"love": 0, "hatred": 0},
    "ren": {"love": 0, "hatred": 0},
}

default unlocked_locations = {
    "home": True,
    "square": True,
    "training": True,
    "market": True,
    "riverside": True,
    "aya_house": False,
    "old_shrine": False,
    "archive": False,
}

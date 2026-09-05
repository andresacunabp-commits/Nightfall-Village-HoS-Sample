# ============================================================
# NIGHTFALL VILLAGE â€” SANDBOX SYSTEMS
# Data/state layer for a Ren'Py portfolio demo.
# ============================================================

init python:
    PERIODS = ("Morning", "Afternoon", "Evening", "Night")

    LOCATION_DATA = {
        "home": {
            "name": "Home",
            "label": "loc_home",
            "description": "Rest, inspect your notes, and end the day."
        },
        "square": {
            "name": "Village Square",
            "label": "loc_square",
            "description": "A social hub where schedules and story events intersect."
        },
        "training": {
            "name": "Training Ground",
            "label": "loc_training",
            "description": "Raise Strength and meet the village instructor."
        },
        "market": {
            "name": "Market Alley",
            "label": "loc_market",
            "description": "Buy items used by quests and event requirements."
        },
        "riverside": {
            "name": "Riverside",
            "label": "loc_riverside",
            "description": "A quieter area with exploration events."
        },
        "aya_house": {
            "name": "Aya's Household",
            "label": "loc_aya_house",
            "description": "A relationship-gated location unlocked through story progress."
        },
    }

    CHARACTER_DATA = {
        "aya": {
            "name": "Aya",
            "description": "A guarded courier with a branching Love / Hatred storyline."
        },
        "ren": {
            "name": "Ren",
            "description": "A disciplined instructor tied to Strength progression."
        },
    }

    # Data-driven event definitions. Higher priority events are selected first.
    EVENT_DATA = [
        {
            "id": "aya_intro",
            "label": "ev_aya_intro",
            "location": "square",
            "times": ("Morning", "Afternoon"),
            "min_day": 1,
            "priority": 100,
            "once": True,
        },
        {
            "id": "find_charm",
            "label": "ev_find_charm",
            "location": "riverside",
            "times": ("Morning", "Afternoon", "Evening"),
            "min_day": 1,
            "priority": 95,
            "once": True,
            "quest": ("aya_charm", "active"),
        },
        {
            "id": "return_charm",
            "label": "ev_return_charm",
            "location": "square",
            "times": ("Morning", "Afternoon", "Evening"),
            "min_day": 1,
            "priority": 110,
            "once": True,
            "requires_item": ("Silver Charm", 1),
            "quest": ("aya_charm", "active"),
        },
        {
            "id": "ren_intro",
            "label": "ev_ren_intro",
            "location": "training",
            "times": ("Morning", "Afternoon"),
            "min_day": 1,
            "priority": 90,
            "once": True,
        },
        {
            "id": "aya_house_invite",
            "label": "ev_aya_house_invite",
            "location": "square",
            "times": ("Afternoon", "Evening"),
            "min_day": 2,
            "priority": 85,
            "once": True,
            "requires_flag": "aya_charm_returned",
            "min_relation": ("aya", "love", 3),
        },
        {
            "id": "rooftop_test",
            "label": "ev_rooftop_test",
            "location": "square",
            "times": ("Night",),
            "min_day": 3,
            "priority": 80,
            "once": True,
            "min_stat": ("reputation", 2),
        },
    ]

    def period_name():
        return PERIODS[store.period_index]

    def is_location_unlocked(location_id):
        return bool(store.unlocked_locations.get(location_id, False))

    def has_item(item_name, qty=1):
        return store.inventory.get(item_name, 0) >= qty

    def add_item(item_name, qty=1):
        store.inventory[item_name] = store.inventory.get(item_name, 0) + qty

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

    def change_relation(character_id, route, amount):
        if character_id not in store.relationships:
            store.relationships[character_id] = {"love": 0, "hatred": 0}
        store.relationships[character_id][route] = max(
            0, store.relationships[character_id].get(route, 0) + amount
        )

    def dominant_route(character_id):
        love = relation(character_id, "love")
        hatred = relation(character_id, "hatred")
        if love >= 5 and love > hatred:
            return "Love"
        if hatred >= 5 and hatred > love:
            return "Hatred"
        return "Undecided"

    def spend_time(cost=1):
        """Consumes energy and advances the period.
        When Night is passed, the next day begins automatically.
        """
        store.energy = max(0, store.energy - cost)
        if store.period_index < len(PERIODS) - 1:
            store.period_index += 1
        else:
            start_new_day()

    def start_new_day():
        store.day += 1
        store.period_index = 0
        store.energy = 3
        store.daily_flags = {}

    def npc_location(character_id):
        """Very small schedule system used by the map/status UI."""
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

        return None

    def _event_requirement_ok(ev):
        if store.day < ev.get("min_day", 1):
            return False

        if period_name() not in ev.get("times", PERIODS):
            return False

        if ev.get("once") and store.seen_events.get(ev["id"], False):
            return False

        flag = ev.get("requires_flag")
        if flag and not store.flags.get(flag, False):
            return False

        not_flag = ev.get("forbid_flag")
        if not_flag and store.flags.get(not_flag, False):
            return False

        quest = ev.get("quest")
        if quest:
            qid, required_state = quest
            if store.quests.get(qid) != required_state:
                return False

        item = ev.get("requires_item")
        if item:
            item_name, qty = item
            if not has_item(item_name, qty):
                return False

        rel = ev.get("min_relation")
        if rel:
            cid, route, amount = rel
            if relation(cid, route) < amount:
                return False

        stat = ev.get("min_stat")
        if stat:
            stat_name, amount = stat
            if getattr(store, stat_name, 0) < amount:
                return False

        return True

    def next_event_for(location_id):
        candidates = [
            ev for ev in EVENT_DATA
            if ev["location"] == location_id and _event_requirement_ok(ev)
        ]
        if not candidates:
            return None
        candidates.sort(key=lambda e: e.get("priority", 0), reverse=True)
        return candidates[0]["label"]

    def mark_event(event_id):
        store.seen_events[event_id] = True

    def guide_objectives():
        """Spoiler-light objective tracker inspired by sandbox VN guide systems."""
        objectives = []

        if store.quests.get("aya_charm") == "locked":
            objectives.append(("Aya", "Visit the Village Square during the day."))
        elif store.quests.get("aya_charm") == "active" and not has_item("Silver Charm"):
            objectives.append(("Aya", "Search somewhere quiet near the village."))
        elif store.quests.get("aya_charm") == "active" and has_item("Silver Charm"):
            objectives.append(("Aya", "Return to the Village Square."))
        elif store.quests.get("aya_charm") == "complete" and not is_location_unlocked("aya_house"):
            objectives.append(("Aya", "Raise Aya's Love and revisit the Square later."))
        else:
            objectives.append(("Aya", "Visit Aya at different times and explore both relationship approaches."))

        if not store.seen_events.get("ren_intro"):
            objectives.append(("Ren", "Visit the Training Ground during the day."))
        elif store.strength < 3:
            objectives.append(("Training", "Train until Strength reaches 3."))
        else:
            objectives.append(("Training", "Your Strength may now unlock new interactions."))

        if store.reputation < 2:
            objectives.append(("Village", "Complete helpful actions to raise Reputation."))
        elif not store.seen_events.get("rooftop_test"):
            objectives.append(("Village", "Something may happen in the Square at night."))

        return objectives

    def inventory_lines():
        if not store.inventory:
            return ["Empty"]
        return ["{} x{}".format(name, qty) for name, qty in sorted(store.inventory.items())]

# --------------------
# Save-game state
# --------------------

default day = 1
default period_index = 0
default energy = 3
default coins = 30
default strength = 0
default reputation = 0

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
}


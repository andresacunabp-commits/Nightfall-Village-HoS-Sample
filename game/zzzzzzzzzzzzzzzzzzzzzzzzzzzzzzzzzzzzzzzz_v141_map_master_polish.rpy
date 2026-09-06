# ============================================================
# NIGHTFALL VILLAGE v0.14.1 — MAP MASTER POLISH
# ============================================================
# Final node placement pass for the four 1920x1080 v0.14 map masters.
# All four time-of-day maps share the same village geometry, so the
# destination anchors stay fixed while only the lighting changes.
# ============================================================

init 18000 python:

    # Positions authored in the 1280x720 runtime space.
    # They follow the actual geography of the new master map:
    # market west, village core center-left, training center,
    # river southeast, Aya residence east, shrine northeast.
    NV127_MAP_NODES = (
        ("market", 92, 392),
        ("square", 348, 292),
        ("training", 610, 322),
        ("home", 430, 515),
        ("riverside", 820, 500),
        ("aya_house", 1000, 365),
        ("old_shrine", 1000, 116),
        ("archive", 1080, 238),
    )

    # Prefer the v0.14 protagonist-home master as the home thumbnail.
    _v141_home_thumb = NV140_ROOT + "/home/exterior.jpg"
    if renpy.loadable(_v141_home_thumb):
        NV127_MAP_THUMBS["home"] = _v141_home_thumb


# Slightly tighter map-node chrome so more of the master illustration
# remains visible underneath the travel UI.
style nv127_map_node is button:
    background None
    hover_background Solid("#0bd4ff20")
    insensitive_background None
    xpadding 0
    ypadding 0

# The existing v131 screen already resolves its background through
# nv131_map_background(); the v140 pipeline redirects that resolver to
# map_morning/day/evening/night when those masters are available.

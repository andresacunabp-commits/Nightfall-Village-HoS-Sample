# ============================================================
# NIGHTFALL VILLAGE v0.8.0 — VISIBLE VERSION CONSISTENCY FIX
# Keeps the Household vertical slice branded as part of the
# current v0.8 portfolio build instead of displaying v0.7.
# ============================================================

screen nv_v080_version_consistency_overlay():
    zorder 5000

    # The Household slice was introduced in v0.7, but it now ships
    # inside the v0.8 build. Cover its old module footer with the
    # current build label so the visible UI is consistent.
    if renpy.get_screen("v07_house_hub") is not None:
        frame:
            xpos 890
            ypos 638
            xsize 355
            ysize 38
            background Solid("#02070aef")
            padding (12, 7)

            text "v0.8.0 • Household Module • route-aware events":
                size 10
                color "#7f9ca7"
                xalign 0.5

init 3000 python:
    if "nv_v080_version_consistency_overlay" not in config.overlay_screens:
        config.overlay_screens.append("nv_v080_version_consistency_overlay")

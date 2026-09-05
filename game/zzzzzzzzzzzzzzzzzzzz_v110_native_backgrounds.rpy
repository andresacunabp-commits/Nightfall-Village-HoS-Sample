# ============================================================
# NIGHTFALL VILLAGE v0.11.0 — NATIVE MASTER ART
# ============================================================

init 9000 python:

    NV110_BG = "images/backgrounds/v110/"

    renpy.image("bg_home", NV110_BG + "aya_house_hallway.jpg")
    renpy.image("bg_square", NV110_BG + "village_square.jpg")
    renpy.image("bg_training", NV110_BG + "training_ground.jpg")
    renpy.image("bg_market", NV110_BG + "market_alley.jpg")
    renpy.image("bg_riverside", NV110_BG + "riverside.jpg")
    renpy.image("bg_aya_house", NV110_BG + "aya_house_hallway.jpg")
    renpy.image("bg_aya_house_ext", NV110_BG + "aya_house_ext.jpg")
    renpy.image("bg_old_shrine", NV110_BG + "shrine_path.jpg")
    renpy.image("bg_archive", NV110_BG + "aya_house_hallway.jpg")

    if "V09_LOCATION_VISUALS" in globals():

        V09_LOCATION_VISUALS["home"]["thumb"] = NV110_BG + "aya_house_hallway.jpg"
        V09_LOCATION_VISUALS["square"]["thumb"] = NV110_BG + "village_square.jpg"
        V09_LOCATION_VISUALS["training"]["thumb"] = NV110_BG + "training_ground.jpg"
        V09_LOCATION_VISUALS["market"]["thumb"] = NV110_BG + "market_alley.jpg"
        V09_LOCATION_VISUALS["riverside"]["thumb"] = NV110_BG + "riverside.jpg"
        V09_LOCATION_VISUALS["aya_house"]["thumb"] = NV110_BG + "aya_house_ext.jpg"
        V09_LOCATION_VISUALS["old_shrine"]["thumb"] = NV110_BG + "shrine_path.jpg"
        V09_LOCATION_VISUALS["archive"]["thumb"] = NV110_BG + "aya_house_hallway.jpg"

    renpy.log("Nightfall v0.11.0: native-resolution background masters active.")

# ============================================================
# ORIGINAL VISUAL ASSET DEFINITIONS — v0.9 CINEMATIC COMPOSITES
# ============================================================
# The original location art remains in the project, but v0.9 blends
# each scene with the richer village-night painting so the prototype
# stops feeling like flat placeholder geometry while preserving a
# distinct base composition per district.

image bg_main = "images/ui/main_menu_bg.png"

image bg_home = Composite(
    (1280, 720),
    (0, 0), im.Scale("images/ui/home_bg.png", 1280, 720),
    (0, 0), Transform(im.Scale("images/ui/village_night_bg.png", 1280, 720), alpha=0.24)
)

image bg_square = Composite(
    (1280, 720),
    (0, 0), im.Scale("images/ui/square_bg.png", 1280, 720),
    (0, 0), Transform(im.Scale("images/ui/village_night_bg.png", 1280, 720), alpha=0.34)
)

image bg_training = Composite(
    (1280, 720),
    (0, 0), im.Scale("images/ui/training_bg.png", 1280, 720),
    (0, 0), Transform(im.Scale("images/ui/village_night_bg.png", 1280, 720), alpha=0.20)
)

image bg_market = Composite(
    (1280, 720),
    (0, 0), im.Scale("images/ui/market_bg.png", 1280, 720),
    (0, 0), Transform(im.Scale("images/ui/village_night_bg.png", 1280, 720), alpha=0.30)
)

image bg_riverside = Composite(
    (1280, 720),
    (0, 0), im.Scale("images/ui/riverside_bg.png", 1280, 720),
    (0, 0), Transform(im.Scale("images/ui/village_night_bg.png", 1280, 720), alpha=0.22)
)

image bg_aya_house = Composite(
    (1280, 720),
    (0, 0), im.Scale("images/ui/aya_house_bg.png", 1280, 720),
    (0, 0), Transform(im.Scale("images/ui/village_night_bg.png", 1280, 720), alpha=0.23)
)

image bg_old_shrine = Composite(
    (1280, 720),
    (0, 0), im.Scale("images/ui/old_shrine_bg.png", 1280, 720),
    (0, 0), Transform(im.Scale("images/ui/village_night_bg.png", 1280, 720), alpha=0.18)
)

image bg_archive = Composite(
    (1280, 720),
    (0, 0), im.Scale("images/ui/archive_bg.png", 1280, 720),
    (0, 0), Transform(im.Scale("images/ui/village_night_bg.png", 1280, 720), alpha=0.16)
)

transform slow_float:
    yoffset 0
    linear 2.0 yoffset -5
    linear 2.0 yoffset 0
    repeat

# ============================================================
# NIGHTFALL v0.6 HOTFIX 01
# Calendar helper missing from visual polish.
# ============================================================

init -200 python:

    NIGHTFALL_WEEKDAYS = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    )

    def weekday_name(value):
        try:
            value = int(value)
        except:
            value = 1

        value = max(1, value)

        return NIGHTFALL_WEEKDAYS[(value - 1) % 7]

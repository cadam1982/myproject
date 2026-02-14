trainings = [
    {"sport": "run", "duration": 45},
    {"sport": "bike", "duration": 60},
    {"sport": "swim", "duration": 30},
    {"sport": "run", "duration": 50},
    {"sport": "strength", "duration": 40},
    {"sport": "bike", "duration": 75},
    {"sport": "mobility", "duration": 20},
    {"sport": "run", "duration": 35},
]

totals = {}

counts = {}

for session in trainings:
    sport = session["sport"]
    duration = session["duration"]
    
    if sport not in totals:
        totals[sport] = 0
        counts[sport] = 0

    totals[sport] += duration
    counts[sport] += 1

for sport in totals:
    minutes = totals[sport]
    sessions = counts[sport]
    print(f"{sport} → {minutes} Minuten, {sessions} Einheiten")
              
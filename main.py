trainings = [
    {"sport": "run", "duration": 45},
    {"sport": "bike", "duration": 60},
    {"sport": "swim", "duration": 20},
    {"sport": "run", "duration": 40},
    {"sport": "strength", "duration": 30}

]

total_run = 0
total_bike = 0
total_swim = 0

total_time = 0

for session in trainings:
    if session["sport"] == "run":
        total_run += session["duration"]
    elif session["sport"] == "bike":
        total_bike += session["duration"]
    else:
        total_swim += session["duration"]


    total_time += session["duration"]


print("Total run time:", total_run, "minutes")
print("Total bike time:", total_bike, "minutes")
print("Total swim time:", total_swim, "minutes")
print("Total training time:", total_time, "minutes")
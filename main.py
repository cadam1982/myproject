trainings = [
    {"sport": "run", "duration": 45},
    {"sport": "bike", "duration": 60},
    {"sport": "swim", "duration": 20},
]

total_time = 0

for session in trainings:
    print(session)
    total_time += session["duration"]


print("Total training time:", total_time, "minutes")
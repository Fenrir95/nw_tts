from datetime import datetime
import pyttsx3

spawn = []
with open("spawns.txt") as file:
    for row in file:
        minute, second = row.split(":")
        spawn.append(int(minute) * 60 + int(second))
tts = pyttsx3.init()
while True:
    current = datetime.now()
    if current.minute >= 30:
        war_minute = 60 - current.minute
    else:
        war_minute = 30 - current.minute
    war_seconds = war_minute * 60 - current.second
    for spawn_timer in spawn:
        if spawn_timer < war_seconds:
            countdown = war_seconds - spawn_timer
            break
        else:
            countdown = war_seconds
    if countdown % 10 == 0 or countdown <= 5:
        tts.say(str(countdown))
        tts.runAndWait()
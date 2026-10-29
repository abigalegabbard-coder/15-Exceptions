import random; import time

creepyMessages = ["Someone is standing behind you.",
                  "I know what you did yesterday.",
                  "Your webcam is already on.",
                  "Don't turn around.",
                  "Boo! You can't find me!"
                  ]

for x in range(10):
    try:
        random_index = random.randint(0,5)
        print(creepyMessages[random_index])
    except IndexError:
        print("ERROR: Something is trying to comminiate...")
    finally:
        print("The computer is watching you.")
        print()
        time.sleep(1)
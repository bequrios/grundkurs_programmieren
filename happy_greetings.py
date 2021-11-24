import random

my_greetings = ["Ich wünsche Dir einen sensationellen Tag!",
            "Allerallerallerliebste Grüsse an Dich!",
            "Einen formidablen Tag sei Dir gegönnt!"]


def nice_greeting():
    print(my_greetings[random.randint(0,2)])
import random
from random import randint

random_library = {
    'random_events':
    {'Chekhov': 'Lady and the dog',
    'Belarus': {'population': 9486000, 'president': None, 'political_sys': 'Dictatorship'},
    'World GDP': 9999999999999999999999999999999,
    'The sense of life': 42}
}

random_events = random_library['random_events']

print(random_events['Belarus'])

def pick_event():
    event_list = list(random_events.keys())
    for i, event in enumerate(event_list):
        print(f"{i}: {event}")

    if randint(3,99)>38:
        i = int(input('Insert the event number:\n')) # Get the choice from the user
        if i == 1:
            print("Zhyve Belarus")
        else:
            pass
    else:
        i = randint(0,3)
        print("It's a random selection")

    choice = event_list[i]  # Choose the event name corresponding to the user's number
    print(random_events[choice])  # Print the details of the chosen event

pick_event()

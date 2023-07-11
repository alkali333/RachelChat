import requests
import json
import random

def draw_cards():
    tarot_cards = [
        "The Fool",
        "The Magician",
        "The High Priestess",
        "The Empress",
        "The Emperor",
        "The Hierophant",
        "The Lovers",
        "The Chariot",
        "Strength",
        "The Hermit",
        "Wheel of Fortune",
        "Justice",
        "The Hanged Man",
        "Death",
        "Temperance",
        "The Devil",
        "The Tower",
        "The Star",
        "The Moon",
        "The Sun",
        "Judgement",
        "The World"
    ]

    # Get random numbers from RANDOM.ORG
    random_org_url = 'https://www.random.org/integers/?num=1&min=0&max=21&col=1&base=10&format=plain&rnd=new'

    try:
        response = requests.get(random_org_url)
        response.raise_for_status()
        seed = int(response.text.strip())
        random.seed(seed)
        random.shuffle(tarot_cards)
        return " ".join(tarot_cards[:3])
    except (requests.exceptions.RequestException, ValueError) as error:
        print(f"Error while fetching random numbers: {error}")
        exit()
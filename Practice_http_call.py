import requests
from pyfiglet2 import figlet
from pyfiglet2 import figlet_color
from random import randint
from random import choice
from termcolor import colored


def dadjokes():

    figlet_color.magenta("Dad Joke 3000")

    url = "https://icanhazdadjoke.com/search"

    search_str = input("What do you want to search for: ")
    # print(search_str)

    response = requests.get(url,
                            headers={"Accept": "application/json"},
                            params={"term": search_str}
                            )

    data = response.json()
    # print(data)

    count = data["total_jokes"]

    if count == 0:
        print("bad luck")

    elif count == 1:
        joke = data["results"][0]["joke"]
        print("I got one joke about {}. Here it is:".format(search_str))
        print(joke)

    else:
        # rand = randint(1,count)
        # joke = data["results"][rand-1]["joke"]
        joke = choice(data["results"])["joke"]
        print("I got {} jokes about {}. Here's one:".format(count, search_str))
        print(joke)


dadjokes()

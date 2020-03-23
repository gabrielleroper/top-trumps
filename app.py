import random
import requests

def random_anime():
    for i in range(1000):
        anime_number = random.randint(1, 100)
        url = 'https://api.jikan.moe/v3/anime/{}/'.format(anime_number)
        response = requests.get(url)
        anime = response.json()
        status = anime['status']
       # print(status, type(status))
        if status != 404:
            break
    #print(anime)

    return {
        'title': anime['title'],
        'episodes': anime['episodes'],
        'rank': anime['rank'],
        'popularity': anime['popularity'],
    }

def run():
    my_anime = random_anime()
    print('You were given {}'.format(my_anime['title']))
    stat_choice = input('Which stat do you want to use? (episodes, rank, popularity) ')

    opponent_anime = random_anime()
    print('The opponent chose {}'.format(opponent_anime['title']))

    my_stat = my_anime[stat_choice]
    opponent_stat = opponent_anime[stat_choice]

    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')

run()
import requests
import random
from datetime import datetime

genres = {
    "action": "28",
    "adventure": "12",
    "animation": "16",
    "comedy": "35",
    "crime": "80",
    "documentary": "99",
    "drama": "18",
    "family": "10751",
    "fantasy": "14",
    "history": "36",
    "horror": "27",
    "music": "10402",
    "mystery": "9648",
    "romance": "10749",
    "sci-fi": "878",
    "TVMovie": "10770",
    "thriller": "53",
    "war": "10752",
    "western": "37",
}


def help():
    print(
        "Existing genre: action, adventure, animation, comedy, crime, documentary, "
        + "drama, family, fantasy, history, horror, music, mystery, romance, sci-fi, TVMovie, thrille, war, western"
    )


def getMovie(genre):
    try:
        url = (
            "https://api.themoviedb.org/3/discover/movie?api_key=f78791ceb108b383a63b0ae1269d0b3a&with_genres="
            + genres[genre]
            + "&sort_by=release_date.desc&primary_release_date.lte="
            + datetime.today().strftime("%Y-%m-%d")
            + "&page="
            + str(random.randint(1, 500))
        )
        response = requests.request("GET", url)
        n = random.randint(0, 19)
        x = 0

        for d in response.json()["results"]:
            if x == n:
                print(d["original_title"])
                id = d["id"]
            x += 1
        url = (
            "http://api.themoviedb.org/3/movie/"
            + str(id)
            + "/videos?api_key=f78791ceb108b383a63b0ae1269d0b3a"
        )
        response = requests.request("GET", url)
        if response.json()["results"] != []:
            for d in response.json()["results"]:
                key = d["key"]
                print("https://www.youtube.com/watch?v=" + str(key))
        else:
            print("No trailer found")

    except:
        help()


def main():
    print("Enter the movie genre")
    genre = input()
    getMovie(genre)
    print("Do you want an other suggestion ?")
    genre = input()
    if genre == "yes" or genre == "y":
        main()


main()

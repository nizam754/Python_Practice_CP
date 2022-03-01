# Let's filter movies with 7+ ratings

our_movies = [("Interstellar", 10), ("Ironman", 8.2), ("It Fllows", 6.0), ("X-Men", 2)]

def rating_filter(movies, max_rating):
    final_movies = []

    for movie in movies:
        if movie[1] >= max_rating:
            final_movies.append(movie[0])
    return final_movies

print(rating_filter(our_movies, 1))

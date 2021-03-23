from imdb import IMDb
from tabulate import tabulate

# create an instance of the IMDb class
ia = IMDb()

best_pictures_nominees = ['Minari', 'Sound of Metal', 'Mank', 'Promising Young Woman', 'The Father', 'Judas and the Black Messiah', 'The Trial of the Chicago 7', 'Nomadland']
movies = []

# Get first
for picture in best_pictures_nominees:
    best_picture = ia.search_movie(picture)
    movie_id = best_picture[0].movieID
    #print(movie_id)
    movie = []
    movie.append(ia.get_movie(movie_id))
    #print(movie[0])

    movie.append(movie[0]['year'])

    movie.append(movie[0]['rating'])

    director_list = []
    for director in movie[0]['directors']:
        director_list.append(director['name'])

    movie.append(director_list)
    movie.append(movie[0]['plot'])

    cast_list = []
    cont = 0
    for cast in movie[0]['cast']:
        if cont < 5:
            cast_list.append(cast['name'])
            cont+= 1
    movie.append(cast_list)
    
    for genre in movie[0]['genres']:
        movie.append(genre)
    """
    print('Year:')
    print(movie[0]['year'])

    print('Rating:')
    print(movie[0]['rating'])

    # print the names of the directors of the movie
    print('Directors:')
    for director in movie[0]['directors']:
        print(director['name'])

    print('Plot:')
    print(movie[0]['plot'])

    print('Cast:')
    cont = 0
    for cast in movie[0]['cast']:
        if cont < 5:
            print(cast)
            cont+= 1

    # print the genres of the movie
    print('Genres:')
    for genre in movie[0]['genres']:
        print(genre)
    """
    movies.append(movie)
    #for element in movie:
        #print(element)

print(tabulate(movies, headers = ["Name", "Year", "Rating", "Director(s)", "Plot", "Cast", "Genre"]))

with open('output.txt', 'w') as archivo_n:
    archivo_n.writelines(tabulate(movies, headers = ["Name", "Year", "Rating", "Director(s)", "Plot", "Cast", "Genre"]))
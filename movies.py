f = open("/home/aradhika/Downloads/movie_metadata.csv", "r")
movies = f.read()

split_movies = movies.split("\n")
print(split_movies[0:5])
movie_data = []
for each in split_movies:
    movie_data.append(each.split(","))

print(movie_data[0:5])



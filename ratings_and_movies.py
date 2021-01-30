import pandas as pd
# movies: https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv
# ratings: https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv"
movies = pd.read_csv(uri) # Data frame
movies.columns = ["filmeId", "titulo", "generos"] # change columns titles

print(movies.head()) # [head()] Show five first datas


uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
ratings = pd.read_csv(uri) # Data frame

ratings.columns = ["usuarioId", "filmeId", "nota", "momento"]

# print(ratings.head())
# print(ratings["rating"].head()) # Series
# print(ratings["rating"].unique())
# print(ratings["rating"].mean())
# print(ratings["rating"].min())
# print(ratings["rating"].max())
# print(ratings["rating"].describe())
print(ratings.head().describe())

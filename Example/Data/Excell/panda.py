import pandas as pd
import matplotlib.pyplot as plt


file = 'movies.xls'
movies = pd.read_excel(file, sheet_name=0)

print(movies.head())

sheets = pd.ExcelFile(file)
movieSheets = []

for sheet in sheets.sheet_names:
    movieSheets.append(sheets.parse(sheet))
    print(sheet)

movies = pd.concat(movieSheets)

sortMovie = movies.sort_values(['Gross Earnings'], ascending=False)
print(sortMovie.head())
print(sortMovie[['Year', 'Title', 'IMDB Score', 'Gross Earnings']].head())

movieSubset = sortMovie[['Title', 'Gross Earnings']]
print(movieSubset.head())
earningByTitle = movieSubset.pivot_table(index=['Title'])
print(earningByTitle.head())
earningByTitle.head(20).plot(kind='bar', figsize=(20,8))
plt.show()

movies['Net Earnings'] = movies["Gross Earnings"] - movies["Budget"]
sortMovie = movies[['Net Earnings']].sort_values(['Net Earnings'], ascending=[False])
sortMovie.head().plot(kind="barh")
plt.show()

print(sortMovie.head())
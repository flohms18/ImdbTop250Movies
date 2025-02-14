import csv 
with open('IMDB_Top_250_Movies.csv',newline='', encoding="latin1") as csvfile:
    MovieReader = csv.reader(csvfile, delimiter=' ',quotechar='|')
    for row in MovieReader:
        print(', '.join(row))
import pandas as pd

df = pd.read_csv("IMDb_Top_250_Movies.csv",encoding="ISO-8859-1", dtype=object)
data = df.Duration
print(data)
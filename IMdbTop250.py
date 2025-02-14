import pandas as pd

df = pd.read_csv("IMDb_Top_250_Movies.csv",encoding="ISO-8859-1")
data = df.nlargest(10,"Rating").set_index("Name")
print(data)
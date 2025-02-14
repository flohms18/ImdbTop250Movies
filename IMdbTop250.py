import pandas as pd
import matplotlib.pyplot as plt

# Lire le fichier CSV
df = pd.read_csv("IMDb_Top_250_Movies.csv", encoding="ISO-8859-1", dtype=object)

df.info()

df['Rating'] = pd.to_numeric(df['Rating'], errors ="coerce")
df['Release_Year'] = pd.to_numeric(df['Release_Year'],errors="coerce")

df = df.dropna()

df['Decade'] = (df['Release_Year'] // 10 * 10)

decade_rating = df.groupby("Decade")["Rating"].mean()

decade_rating.plot(kind="bar",color="green", figsize=(10,6))
plt.show()
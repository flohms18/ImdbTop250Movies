import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("IMDb_Top_250_Movies.csv", encoding="ISO-8859-1", dtype=object)
data = df.head()

data["Duration"] = pd.to_numeric(data["Duration"], errors="coerce")
data["Release_Year"] = pd.to_numeric(data["Release_Year"], errors="coerce")
data.plot(kind="bar",x="Release_Year",y="Duration",color="green")


plt.show()
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("IMDb_Top_250_Movies.csv", encoding="ISO-8859-1", dtype=object)
data = df.head()

df.info()

data["Duration"] = pd.to_numeric(data["Duration"], errors="coerce")
data["Name"] = data['Name'].astype(str)
data.plot(kind="bar",y="Duration",x="Name",color="green")


plt.show()
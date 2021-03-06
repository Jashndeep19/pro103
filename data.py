import pandas as pd
import plotly.express as px

data = pd.read_csv("Copy+of+data+-+data.csv")
figure = px.scatter(data,x="date",y="cases",color="country",title="Covid 19 daily cases through time", size ="cases")

figure.show()
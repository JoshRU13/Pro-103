import pandas as pd
import plotly.express as px
bf=pd.read_csv("data.csv")
fig=px.scatter(bf,x="date",y="cases",color="country")
fig.show()
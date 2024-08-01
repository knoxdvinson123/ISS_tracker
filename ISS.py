
import pandas as pd
import plotly.express as px
 
iss_url = 'http://api.open-notify.org/iss-now.json'

data_frame = pd.read_json(iss_url)
data_frame['latitude'] = data_frame.loc['latitude', 'iss_position']
data_frame['longitude'] = data_frame.loc['longitude', 'iss_position']
data_frame.reset_index(inplace=True)
data_frame = data_frame.drop(['index', 'message'], axis=1)

print(data_frame)

figure = px.scatter_geo(data_frame, lat='latitude', lon='longitude', projection = 'natural earth') #geographic scatter plot overlay
figure.show()
import pandas as pd
df = pd.read_csv('train.csv')


import folium
from folium import plugins

positions = df[['Y', 'X']].values


m = folium.Map(location=[positions[0][0], positions[0][1]], zoom_start=15)
m.add_child(plugins.HeatMap(positions[:50000], radius=15))
m.save('map.html')




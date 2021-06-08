import folium

#18.513704622113835, -70.10808234381392

Gmap = folium.Map(location=[18.513704622113835, -70.10808234381392], tiles="OpenStreetMap", zoom_start=80, control_scale=True)
Gmap.save('index1.html')

from geopy.geocoders import Nominatim
import time
import math

#Creando Objeto de tipo Nominatim
lugar = input("Introduce la Calle, Avenida, Ciudad o Pais")
geo = Nominatim(user_agent="GMap")
localizacion = geo.geocode(lugar)
print(localizacion)
print(localizacion.latitude, localizacion.longitude)
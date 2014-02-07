#-*- coding: utf-8-*-
import requests
import json

ciudad = raw_input("""1. Almeria
2. Cadiz
3. Cordoba
4. Granada
5. Huelva
6. Jaen
7. Malaga
8. Sevilla

¿De que ciudad quieres saber la temperatura actual? """)

lista = {"1":"Almeria","2":"Cadiz","3":"Cordoba","4":"Granada","5":"Huelva","6":"Jaen","7":"Malaga","8":"Sevilla"}

#respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'Malaga,spain'})
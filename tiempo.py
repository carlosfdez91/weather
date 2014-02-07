#coding: utf-8
import requests
import json

lista = {"1":"Almería","2":"Cádiz","3":"Córdoba","4":"Granada","5":"Huelva","6":"Jaén","7":"Málaga","8":"Sevilla"}

ciudades = raw_input("""1. Almería
2. Cádiz
3. Córdoba
4. Granada
5. Huelva
6. Jaén
7. Málaga
8. Sevilla

¿De qué ciudad quieres saber la temperatura actual? """)

print lista[ciudades]

#respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'Malaga,spain'})
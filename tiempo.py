#coding: utf-8
import requests
import json

lista = {"1":"Almeria","2":"Cadiz","3":"Cordoba","4":"Granada","5":"Huelva","6":"Jaen","7":"Malaga","8":"Sevilla"}

ciudades = raw_input("""1. Almería
2. Cádiz
3. Córdoba
4. Granada
5. Huelva
6. Jaén
7. Málaga
8. Sevilla

¿De qué ciudad quieres saber la temperatura actual? """)


respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % lista[ciudades]})

dicc = json.loads(respuesta.text)

tempkelvin = dicc["main"]["temp"]

tempreal = tempkelvin - 273

print "La temparatura actual de %s es %s grados centígrados" % (lista[ciudades],tempreal)
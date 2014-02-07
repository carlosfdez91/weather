#coding: utf-8
import requests
import json

lista = {"1":"Almería","2":"Cádiz","3":"Córdoba","4":"Granada","5":"Huelva","6":"Jaén","7":"Málaga","8":"Sevilla","9":"Utrera"}

ciudades = raw_input("""1. Almería
2. Cádiz
3. Córdoba
4. Granada
5. Huelva
6. Jaén
7. Málaga
8. Sevilla
9. Utrera

¿De qué ciudad quieres saber la temperatura actual? """)


respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % lista[ciudades]})

dicc = json.loads(respuesta.text)

tempkelvin = dicc["main"]["temp"]

tempreal = tempkelvin - 273

print "La temparatura actual de %s es %s grados centígrados" % (lista[ciudades],tempreal)
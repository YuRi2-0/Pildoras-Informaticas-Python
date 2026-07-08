from bs4 import BeautifulSoup
import requests

miDoc = requests.get("https://www.thunderbird.net/es-ES/")


docFinal = BeautifulSoup(miDoc.text,"html.parser")

iconos = docFinal.select(".icon")

tituloGradiente = docFinal.select(".tagline .txt-gradient")

print(iconos[0].text)

print(tituloGradiente[0].text)




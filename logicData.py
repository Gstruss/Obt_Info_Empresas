# Hecho por Geoffrey Struss

import requests,json

#La función obtenerIpDesdeDominio recibe un nombre de dominio, realiza una solicitud a la API de NetworkCalc para obtener
# los registros DNS de tipo A asociados a ese dominio, y luego, para cada dirección IP obtenida, realiza una solicitud a
# la API de IPinfo para determinar su región geográfica; finalmente, imprime la región de cada IP junto con el dominio que
# se está procesando.
def obtenerIpDesdeDominio(dominio):
    print("----------Dominio -> "+str(dominio)+"----------")
    resultadoBusqueda = requests.get("https://networkcalc.com/api/dns/lookup/"+str(dominio))
    if resultadoBusqueda.json()['records'] != None:
        for i in range(len(resultadoBusqueda.json()['records']['A'])):
            ip=resultadoBusqueda.json()['records']['A'][i]['address']
            resultadoRegion = requests.get("https://ipinfo.io/"+str(ip)+"/json")
            print("la region de la ip -> "+str(ip)+" es " +str(resultadoRegion.json()['region']))

# Lista de dominios de empresas colombianas
dominios = [
    "avianca.com",
    "grupoaval.com",
    "ecopetrol.com.co",
    "bancolombia.com",
    "alpina.com.co",
    "carrefour.com.co",
    "corona.co",
    "fenalco.com",
    "exito.com",
    "grupoexito.com",
    "colpatria.com",
    "drogueriascolsubsidio.com",
    "cementosargos.com",
    "cerveceriabavaria.com",
    "bovina.com.co",
    "vanti.com",
    "metrotel.com.co",
    "becolombia.com",
    "movistar.co",
    "claro.com.co",
    "tigo.com.co",
    "telmex.com.co",
]

#La función obtenerEmailsDesdeDominio realiza una solicitud a la API de Hunter.io para buscar direcciones de correo
# electrónico asociadas a un dominio específico utilizando una clave de API para autenticación; si la respuesta contiene
# correos electrónicos, la función itera a través de ellos e imprime cada dirección de correo electrónico encontrada.
def obtenerEmailsDesdeDominio(dominio):
    resultadoEmails = requests.get("https://api.hunter.io/v2/domain-search?domain="+str(dominio)+"&api_key=dd24e332eb1698c16d7348eb73787010a67c7c18")
    if resultadoEmails.json()['data']['emails'] !=None:
        for correo in range (len (resultadoEmails.json()['data']['emails'])):
             print ("correo:" +str(resultadoEmails.json()['data']['emails'][correo]['value']))

for i in dominios:
 obtenerIpDesdeDominio(i)
 obtenerEmailsDesdeDominio(i)
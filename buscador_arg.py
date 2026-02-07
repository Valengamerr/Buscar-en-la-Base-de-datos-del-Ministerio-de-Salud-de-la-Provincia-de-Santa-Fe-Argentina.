# Codigo creado por "t.me/Valen_Qq"
# ------------------------------
#  NO COBRAR POR ESTE ARCHIVO
# ------------------------------


import requests

url = "https://www.santafe.gov.ar/padronsalud/includes/consultas/ajax.functions.php?sub=padron&sajax=1"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "es-ES,es;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "79",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "www.santafe.gov.ar",
    "Origin": "https://www.santafe.gov.ar",
    "Referer": "https://www.santafe.gov.ar/padronsalud/index.php?section=consultas&sub=padron",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

payload = {
    "sub": "padron",
    "sajax": "1",
    "rs": "grilla_padron",
    "rst": "",
    "rsrnd": "1696765871684",
    "rsargs[]": "DNI_AQUI",            # Ejemplo: "20123456"
    "rsargs[]": "SEXO_M_O_F",         # Ejemplo: "M"
    "rsargs[]": "APELLIDO_Y_NOMBRE"   # Ejemplo: "GONZALEZ LUCIANO"
}

response = requests.post(url, headers=headers, data=payload)

print(response.text)

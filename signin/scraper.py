import requests, os
import pandas as pd
from bs4 import BeautifulSoup as bs4
from dotenv import load_dotenv

# SENSIBLE
load_dotenv()
HEADER = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}
URL = os.getenv("URL")

def getQuotation(url=URL, header=HEADER):
    page = requests.get(url, headers=header)
    soup = bs4(page.content, "lxml")
    
    get_quotation_usd = soup.find("table", {"class" : "table cotizacion"})
    get_quotation_date = soup.find("th", {"class" : "fechaCot"})
    get_quotation_time = soup.find("div", {"class" : "legal"})

    for row in get_quotation_usd.tbody.find_all('tr'):    
        columns = row.find_all('td')
        divisa = columns[0].text.strip()
        cotizacion_compra = columns[1].text.strip()
        cotizacion_venta = columns[2].text.strip()
        
        data = {
            "DIVISA": [divisa],
            "COMPRA": [cotizacion_compra],
            "VENTA" : [cotizacion_venta],
            "FECHA" : [get_quotation_date.text],
            "HORA"  : [get_quotation_time.text[20:]]
        }

        df = pd.DataFrame(data)
        return df


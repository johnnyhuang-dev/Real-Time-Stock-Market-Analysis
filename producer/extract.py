import requests
from config import logger, headers, url

def connect_to_api():

    stocks = ['TSLA', 'MSFT', 'GOOGL']

    json_response = []

    for stock in range(0, len(stocks)):

        querystring = {"function":"TIME_SERIES_DAILY",
               "symbol":f"{stocks[stock]}",
               "outputsize":"compact",
               "interval":"5min",
               "datatype":"json"}

        try: 
            response = requests.get(url, headers=headers, params=querystring)

            response.raise_for_status()

            data = response.json()
            
            logger.info("Stocks successfully loaded")

            json_response.append(data)

        except requests.exceptions.RequestException as e:
            logger.error(f"Error on stock {e}")
            break



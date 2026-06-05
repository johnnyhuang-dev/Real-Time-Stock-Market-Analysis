from extract import connect_to_api, extract_json
import time

def main():
    response = connect_to_api()

    print(response)

    data = extract_json(response)

    for stock in data:
        result = {
            'data': stock['date'],
            'symbol': stock['symbol'],
            'open': stock['open'],
            'low': stock['low'],
            'high': stock['high'],
            'close': stock['close']
        }

        print(result)

    return None

if __name__ == "__main__":
    main()
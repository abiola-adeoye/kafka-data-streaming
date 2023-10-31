import os
import json
import websocket

from dotenv import load_dotenv

from log import load_logging

load_dotenv()
token = os.getenv('FINNHUB_API')

def on_message(ws, message):
    data = json.loads(message)
    print(data['data'])
    print(len(data['data']))


def on_error(ws, error):
    print(error)


def on_close(ws):
    print('### closed ###')


def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')


if __name__ == '__main__':
    ws = websocket.WebSocketApp(f"wss://ws.finnhub.io?token={token}", on_message=on_message,
                                on_error=on_error, on_close=on_close)

    ws.on_open = on_open
    ws.run_forever()


class FinnhubTradeAPI:

    def __init__(self, symbols: list = None):
        # setup logger for class
        self.logger = load_logging(__class__.__name__)

        self.token = os.getenv('FINNHUB_API')
        self.symbols = symbols

    def start_stream(self):
        pass

    def on_open(self):
        pass

    def on_message(self):
        pass

    def on_error(self):
        pass

    def on_close(self):
        pass

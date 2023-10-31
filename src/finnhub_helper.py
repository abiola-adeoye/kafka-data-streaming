import os
import json

import websocket
from dotenv import load_dotenv

from src.log import load_logging


class FinnhubTradeAPI:
    _FINNHUB_WS_ADDRESS = "wss://ws.finnhub.io"
    _SUBSCRIPTION_MSG = '{{"type":"subscribe","symbol":"{symbol_abv}"}}'

    def __init__(self, symbols: list = None):
        # setup logger for class
        self.logger = load_logging(__class__.__name__)

        load_dotenv()
        self.token = os.getenv('FINNHUB_API')
        self.symbols = symbols      # the symbols we're getting data for e.g. AMZN

    def start_stream(self):
        finnhub_ws = websocket.WebSocketApp(f"{self._FINNHUB_WS_ADDRESS}?token={self.token}",
                                            on_message=self.on_message,
                                            on_error=self.on_error,
                                            on_close=self.on_close)
        finnhub_ws.on_open = self.on_open
        finnhub_ws.run_forever()

    def on_open(self, ws):
        for name in self.symbols:
            payload = self._SUBSCRIPTION_MSG.format(symbol_abv=name)
            ws.send(payload)

    @staticmethod
    def on_message(ws, message):
        response = json.loads(message)
        response_data = response['data']
        print(response_data)

    def on_error(self, ws, error):
        self.logger.error(msg="Error while streaming", exc_info=error)  # this is not going to work

    def on_close(self, ws, close_status, close_message):
        pass

# add docstrings to the code
import os
import json

import websocket
from dotenv import load_dotenv
from confluent_kafka import Producer

from src.log import load_logging


class FinnhubTradeAPI:
    _FINNHUB_WS_ADDRESS = "wss://ws.finnhub.io"
    _SUBSCRIPTION_MSG = '{{"type":"subscribe","symbol":"{symbol_abv}"}}'

    def __init__(self, symbols: list = None, test_mode=True):
        # setup logger for class
        self.logger = load_logging(__class__.__name__)

        load_dotenv()
        self.test_mode = test_mode
        self.token = os.getenv('FINNHUB_API')
        self.symbols = symbols      # the symbols we're getting data for e.g. AMZN

        self.kafka_producer = Producer({
            'bootstrap.servers': "localhost:9092",
            'client.id': 'finnhub_producer'
        })
        self.kafka_topic =  "FinnhubTrade" #os.getenv('KAFKA_TOPIC')     # needs to be implemented

    def start_stream(self) -> None:
        if self.test_mode:
            websocket.enableTrace(True)
        finnhub_ws = websocket.WebSocketApp(f"{self._FINNHUB_WS_ADDRESS}?token={self.token}",
                                            on_open=self.on_open,
                                            on_message=self.on_message,
                                            on_error=self.on_error,
                                            on_close=self.on_close)
        finnhub_ws.run_forever()

    def on_open(self, ws: websocket) -> None:
        for name in self.symbols:
            payload = self._SUBSCRIPTION_MSG.format(symbol_abv=name)
            ws.send(payload)
            self.logger.info(f"Subscribed to {name} symbol")

    def on_message(self, ws, message: str):
        response = json.loads(message)
        response_data = response['data']

        self.send_to_kafka(response_data)

    def on_error(self, ws, error):
        self.logger.error(msg=f"Error while streaming: {error}", exc_info=1)

    def on_close(self, ws, close_status, close_message):
        self.logger.info(msg=f"Data stream is closing...")

    def send_to_kafka(self, data):
        try:
            # Produce message to Kafka topic
            self.kafka_producer.produce(self.kafka_topic, key=None, value=json.dumps(data))
            self.kafka_producer.poll(0)
        except Exception as e:
            self.logger.error(msg="Error sending message to Kafka", exc_info=True)



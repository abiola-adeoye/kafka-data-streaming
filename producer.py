from src.finnhub_helper import FinnhubTradeAPI

symbols = ['BINANCE:BTCUSDT', 'BINANCE:ETHUSDT', 'BINANCE:XRPUSDT', 'BINANCE:DOGEUSDT']
prod = FinnhubTradeAPI()
prod.on_open()
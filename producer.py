from src.finnhub_helper import FinnhubTradeAPI

# add a feature to collect symbol input or use default symbols
symbols = ['BINANCE:BTCUSDT', 'BINANCE:ETHUSDT', 'BINANCE:XRPUSDT', 'BINANCE:DOGEUSDT']
prod = FinnhubTradeAPI(symbols=symbols, test_mode=False)
prod.start_stream()
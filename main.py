import time
import yaml
from bot.data import fetch_ohlcv
from bot.strategy import generate_signal
from bot.execution import PaperBroker
from bot.logger import TradeLogger
from bot.metrics import Metrics
from bot.visualize import plot_price_with_trades, plot_equity_curve

def main():
    # Load config
    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    # Setup modules
    broker = PaperBroker(balance=10000)
    logger = TradeLogger(config["log_dir"])
    metrics = Metrics()

    print("Bot starting... Press Ctrl+C to stop.")
    while True:
        try:
            # 1. Fetch latest candles
            df = fetch_ohlcv(config["exchange"], config["symbol"], config["timeframe"], limit=200)

            # 2. Generate signal
            signal, sl, tp = generate_signal(df, config)

            # 3. Execute paper trade
            trade = broker.execute(signal, df.iloc[-1]["close"], sl, tp, config)
            if trade:
                logger.log_trade(trade)
                metrics.update(trade)

            # 4. Save equity
            logger.log_equity(broker.balance)

            # 5. Update visuals every N trades
            if len(metrics.trades) % 5 == 0 and len(metrics.trades) > 0:
                plot_price_with_trades(df, logger.trade_log_path, config["plot_dir"])
                plot_equity_curve(logger.equity_log_path, config["plot_dir"])
                metrics.report()

            time.sleep(60)  # wait 1 min before fetching again

        except KeyboardInterrupt:
            print("Bot stopped manually.")
            break
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()

# trading_bot-
# Crypto Trading Bot (Rule-Based)

A modular cryptocurrency trading bot that uses rule-based strategies for
paper trading with logging, performance metrics, and visualization.

## Features

-   Fetch OHLCV data from exchanges (e.g., Binance)
-   Rule-based trading signals (SMA crossover, RSI, ATR-based SL/TP)
-   Paper trading execution (no real money risk)
-   Trade & equity logging
-   Performance metrics (win rate, profit factor, drawdown, etc.)
-   Visualization of price with trades & equity curve

## Project Structure

    crypto-bot-rulebased/
    │── bot/
    │   ├── data.py          # Fetch OHLCV data
    │   ├── strategy.py      # Trading strategy logic
    │   ├── execution.py     # Paper broker for trade execution
    │   ├── logger.py        # Trade & equity logging
    │   ├── metrics.py       # Performance metrics
    │   ├── visualize.py     # Plot trades & equity
    │── config.yaml          # Configurations
    │── main.py              # Entry point to run the bot

## Installation

1.  Clone the repo:

    ``` bash
    git clone https://github.com/yourusername/crypto-bot-rulebased.git
    cd crypto-bot-rulebased
    ```

2.  Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

## Usage

1.  Configure `config.yaml` with your settings (exchange, symbol,
    timeframe, etc.).

2.  Run the bot:

    ``` bash
    python main.py
    ```

## Example Logs

-   Trades will be logged in `logs/trades.csv`
-   Equity updates in `logs/equity.csv`
-   Plots in `plots/`


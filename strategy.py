import pandas as pd
import ta


def add_indicators(df):
    df["EMA20"] = ta.trend.ema_indicator(df["close"], window=20)
    df["EMA50"] = ta.trend.ema_indicator(df["close"], window=50)
    df["EMA200"] = ta.trend.ema_indicator(df["close"], window=200)

    df["ADX"] = ta.trend.adx(
        high=df["high"],
        low=df["low"],
        close=df["close"],
        window=14
    )

    return df


def check_signal(df):
    last = df.iloc[-1]

    buy = (
        last["close"] > last["EMA20"] >
        last["EMA50"] >
        last["EMA200"]
        and last["ADX"] > 25
    )

    sell = (
        last["close"] < last["EMA20"] <
        last["EMA50"] <
        last["EMA200"]
        and last["ADX"] > 25
    )

    if buy:
        return "BUY"

    if sell:
        return "SELL"

    return None

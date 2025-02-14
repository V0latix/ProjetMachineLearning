import pandas

def MA(data, n):
    "Calcule la moyenne mobile d'ordre n"

    return data.rolling(window=n).mean()

def EMA(data, n):
    "Calcule la moyenne mobile exponentielle d'ordre n"

    return data.ewm(span=n, adjust=False).mean()

def RSI(data, n):
    "Calcule le RSI (Relative Strength Index)"
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=n).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=n).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    return rsi

def MACD(data, n_fast, n_slow):
    "Calcule le MACD (Moving Average Convergence Divergence)"
    ema_fast = EMA(data, n_fast)
    ema_slow = EMA(data, n_slow)
    macd = ema_fast - ema_slow
    signal = EMA(macd, 9)

    return macd, signal

def STD(data, n):
    "Calcule l'écart-type"

    return data.rolling(window=n).std()

import pandas as pd

def BollingerBands(data, n, num_std):
    "Calcule les Bandes de Bollinger"
    ma = MA(data, n)
    std = STD(data, n)
    upper_band = ma + (num_std * std)
    lower_band = ma - (num_std * std)

    return upper_band, lower_band






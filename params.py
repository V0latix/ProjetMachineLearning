# Date d'extraction
start_date = '1950-01-01'
end_date = '2025-01-01'

# Liste des indices
indices = {
    "SP500": "^GSPC",
    "Nasdaq100": "^NDX",
    "DowJones": "^DJI",
    "Russell2000": "^RUT",
    "FTSE100": "^FTSE",
    "DAX": "^GDAXI",
    "CAC40": "^FCHI",
    "Nikkei225": "^N225",
    "HangSeng": "^HSI",
    "EuroStoxx50": "^STOXX50E"
}

# Variable de test
isimport = True

params_ma = [5, 15]
params_ema = [5, 15]
params_rsi = [14]
params_macd = [12, 26, 9]
params_std = [10, 20]
params_bollinger = [20, 2]

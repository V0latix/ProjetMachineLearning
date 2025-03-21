import os
# Date d'extraction
start_date = '1982-04-20'
end_date = '2025-01-01'

# Liste des indices
indices = {
    "SP500": "^GSPC",
    # "Nasdaq100": "^NDX",
    # "DowJones": "^DJI",
    # "Russell2000": "^RUT",
    # "FTSE100": "^FTSE",
    # "DAX": "^GDAXI",
    # "CAC40": "^FCHI",
    # "Nikkei225": "^N225",
    # "HangSeng": "^HSI",
    # "EuroStoxx50": "^STOXX50E"
}

# Variable de test
isimport = True

# Paramètres des indicateurs
params_ma = [30]
params_ema = [5]
params_rsi = [14]
params_macd = [12, 26, 9]
params_std = [10, 20]
params_bollinger = [20, 2]

# Paramètres de la stratégie
norm_window = 252
test_size = 0.2
params_ridge = [0.001]
params_lasso = [0.001]
params_elasticnet = [0.001, 0.5]



# Les immuables
base_dir = os.path.join(os.getcwd(), "bases")
plot_dir = os.path.join(os.getcwd(), "plots")
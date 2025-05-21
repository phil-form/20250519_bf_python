import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

btc = pd.read_csv('PandasSeaborn/BTC-USD.csv', index_col='Date', parse_dates=True)

m = btc['Close'].resample('W').agg(['mean', 'std', 'max', 'min'])

m['mean']['2021-06':'2021-08'].plot(label='moyenne par semaine')
plt.fill_between(m.index, m['max'], m['min'], alpha=0.3, label='min max par semaine')
plt.legend()
plt.show()
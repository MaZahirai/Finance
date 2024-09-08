import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Use the TkAgg backend for plotting
import matplotlib.pyplot as plt
#matplotlib.use('Agg')  # or 'Qt5Agg', 'WXAgg'

import pandas as pd
import mplfinance as mpf





pred = np.load('pred.npy')
pred_flattened = pred.reshape(-1)
plt.figure(figsize=(20, 2))
plt.plot(pred_flattened, color='blue', label='Predictions')
plt.title('Predictions vs True Values')
plt.xlabel('Index')
plt.ylabel('Values')
plt.legend()
plt.tight_layout()
plt.show()





csv_file_path = 'output2.csv'

# Read data from CSV file
data = pd.read_csv(csv_file_path, index_col='date', parse_dates=True)

# Ensure the data columns are in the correct format

da = pd.DataFrame()

da['Open'] = data['open']
da['High'] = data['high']
da['Low'] = data['low']
da['Close'] = data['close']
da['MA30'] = data['MA30']
da.index.name = 'date'


apdict = mpf.make_addplot(da['MA30'] )

mpf.plot(da,type='candle',addplot=apdict)






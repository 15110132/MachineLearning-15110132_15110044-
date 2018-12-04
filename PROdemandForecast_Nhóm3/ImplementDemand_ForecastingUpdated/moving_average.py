from fractions import Fraction

import numpy as np
import pandas as pd
import datetime
from statsmodels.tools import eval_measures

def weighted_moving_average(dataframe, window, ahead, file_name):
    # Datetime format
    date_format = '%y-%d'
    # Create ahead-day entries in future
    date_range = pd.date_range(start=dataframe.index[0], periods=dataframe.count() + ahead, freq='MS')
    # Create new dataframe for forecasting
    forecast_full_frame = pd.Series(data=[np.nan] * (len(date_range)), index=date_range)
    # Init weights
    weight_array = []
    for i in range(1, window + 1):
        weight_array.append(Fraction(i * 2, pow(window, 2) + window))
    # Begin forecasting
    for idx in range(window, len(forecast_full_frame.index)):
        # Estimation of actual data
        if idx < len(dataframe.index):
            forecast_full_frame.iloc[idx] = round(
                np.sum([dataframe.iloc[idx - i] * float(weight_array[window - i]) for i in range(1, window + 1)]))
        # Calculation of future data
        else:
            forecast_full_frame.iloc[idx] = round(
                np.sum([forecast_full_frame.iloc[idx - i] * float(weight_array[window - i]) for i in
                        range(1, window + 1)]))

    # Drop all NaN values
    forecast_full_frame.dropna(inplace=True)

    # Future timeframe only
    forecast_partial_frame = forecast_full_frame[~forecast_full_frame.index.isin(dataframe.index)]
    # Root mean squared error
    # rmse = eval_measures.rmse(dataframe[window:dataframe.count()], forecast_full_frame[:dataframe.count() - window])
    # 
    # cm = 100 - (abs(forecast_partial_frame[0] - dataframe[window])/dataframe[window])
    saiso = 0;
    tongdudoan = 0;
    tongthucte = 0;
    for i in range(0, len(forecast_partial_frame)): 
        tongdudoan += forecast_partial_frame[i]
        tongthucte += dataframe[window+i]
    cm = 100 - (100*(abs(tongdudoan - tongthucte))/tongthucte)
    #Weight array
    print('Data Frame')
    for i in range(0, len(dataframe)): 
        print(dataframe[i])
    print('Weight')
    for i in range(0, len(weight_array)):
        print(weight_array[i])
    print('Forecast Pritial Frame')
    for i in range(0, len(forecast_partial_frame)): 
        print(forecast_partial_frame[i])
    # print('RMSE: ', rmse)
    print('Fidelity: %d%%' %cm )
    # Return result
    return forecast_full_frame, forecast_partial_frame, cm, weight_array

# --------------------------------------------------------------------------

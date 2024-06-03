from methods import predict
import pandas as pd


predes = predict.predict(pd.DataFrame({
    'PT08.S2(NMHC)': [1743.000000],
    'PT08.S3(NOx)': [1502.000000],
    'PT08.S4(NO2)': [2299.000000],
    'PT08.S5(O3)': [2032.000000],
    'T': [44.600000],
    'RH': [88.700000],
    'AH': [2.231000],
    'datetimestamp': [309962]
}))
print(predes)

import xgboost as xgb
from sklearn.preprocessing import StandardScaler

models = [
    'PT08.S1(CO)',
    'PT08.S2(NMHC)',
    'PT08.S3(NOx)',
    'PT08.S4(NO2)',
    'PT08.S5(O3)'
]


# data is supposed to store the way
# the first four are the left from the models list
# (ecluding the selected target)
# T RH AH datetimestamp
def predict(data: list, model: int = 0):
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    xgbr = xgb.XGBRegressor()
    xgbr.load_model("./models/" + models[model] + ".ubj")
    return xgbr.predict(data)

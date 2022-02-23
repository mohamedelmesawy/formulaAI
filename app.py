from flask import Flask, render_template, request
from flask_cors import CORS
# from sklearn.externals import joblib 
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model, Model



app = Flask(__name__)
CORS(app, support_credentials=True)




N_FUTURE  = 1
N_PAST    = 4

trainX = pd.read_csv('trainX_to fit_scaler.csv')
train_X_temp = trainX.to_numpy()
train_X_temp[:, 1] /= 100.
scaler_X = StandardScaler()
scaler_X = scaler_X.fit(train_X_temp[:, 3:])
loaded_model = load_model('models/model.h5')



@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")



@app.route('/predict', methods=["POST"])
def predict():
    data = request.get_json()
    print(data)
    X_predict = [
        int(data['opt_m_weather']), 
        float(data['m_rain_percentage']), 
        int(data['opt_m_track_id']), 
        float(data['m_airm_air_temperature']), 
        float(data['m_track_temperature'])
    ]
    X_predict = np.array(X_predict)
    print(X_predict)

    dict_output = {}
    keys = ['5', '10', '15', '30', '60']
    s = scaler_X.transform(X_predict[3:].reshape(1,-1))
    new_record = list(X_predict[:3]) + list(s[0])
    X_predict = np.array([[new_record] * N_PAST])

    for i in range(5, 61, 5):
        y1, y2 = loaded_model.predict(X_predict)
        new_record = np.array([np.argmax(y1), np.round(y2[0][0], 2)] + list(X_predict[2:]))
        if str(i) in keys:
            dict_output[str(i)] = { 'type':str(np.argmax(y1)), str(np.argmax(y1)): str(np.round(y2[0][0], 2)) }

    return str(dict_output)




if __name__ == "__main__":
    app.run()

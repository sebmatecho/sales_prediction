import pickle
import pandas as pd
import os
from flask import Flask, request, Response
from rossmann.Rossmann import Rossmann


#loading model

model = pickle.load(open(r'C:\Users\Windows\Google Drive\DS em produccao\model\model_rossmann.pkl','rb'))
#initialize API 

app = Flask(__name__)

@app.route('/rossmann/predict', methods=['POST'])
def rossmann_predict():
    test_json = request.get_json()
    
    if test_json:
        # se o json for único (ou seja, um dicionário)
        if isinstance(test_json, dict):
            test_raw = pd.DataFrame(test_json, index=[0])
        # se não for único, cria o dataframe considerando as chaves do json
        else:       
            test_raw = pd.DataFrame(test_json, columns = test_json[0].keys())
            
        # instanciar a Rossmann class
        pipeline = Rossmann()
        
        
        # data cleaning
        df1 = pipeline.data_cleaning(test_raw)
        
        # feature engineering
        df2 = pipeline.feature_engineering(df1)
        
        # data preparation
        df3 = pipeline.data_preparation(df2)
        
        # prediction
        df_response = pipeline.get_prediction(model, test_raw, df3)       
       
        return df_response
        
        
    else:
        return Response('{}', status=200, mimetype='application/json')

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run('127.0.0.1', port = port, debug=True)
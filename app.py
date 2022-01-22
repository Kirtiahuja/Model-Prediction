import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
# import pandas as pd
from flask_cors import CORS,cross_origin


app = Flask(__name__)
#status_model = pickle.load(open('status_model.pkl', 'rb'))

@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
@cross_origin()

def predict():
    
    if request.method == "POST": 
        try:
            
                   # Founded At
            founded_at = int(request.form['founded_at'])
            
           
           # Fundng Rounds
            funding_rounds = float(request.form['funding rounds'])
           
           # Funding Total USD
            funding_total_usd = float(request.form['funding total usd'])
           
           # Milestones
            milestones = float(request.form['milestones'])
            
           # Relationship 
            relationships = float(request.form['relationships'])
            
           # Latitude 
            lat = float(request.form['lat'])
           
           # Longitude 
            lng = float(request.form['lng'])
        
           # Category Code 
            category_code = request.form.get('category_code')
            
           # Country Code 
            country_code = request.form.get('country_code')
            # print(country_code)
           
        
            
            input_list = []
            input_list.append(founded_at)
            input_list.append(funding_rounds)
            input_list.append(funding_total_usd)
            input_list.append(milestones)
            input_list.append(relationships)
            input_list.append(lat)
            input_list.append(lng)
            
            category_code_list = ['category_code_biotech', 'category_code_consulting', 'category_code_ecommerce',
                     'category_code_education', 'category_code_enterprise','category_code_games_video',
                     'category_code_hardware', 'category_code_mobile', 'category_code_network_hosting',
                     'category_code_other', 'category_code_public_relations','category_code_search',
                     'category_code_software', 'category_code_web']
            
            category_code = category_code
            category_list = []
            
            for i in category_code_list:
                if i == category_code:
                    i = 1
                    category_list.append(i)
                else:
                    i = 0
                    category_list.append(i)
                # for i in cat_li:
                #     print(i, end=' ')
            
            country_code_list = ['country_code_BRA', 'country_code_CAN', 'country_code_DEU', 
                'country_code_ESP', 'country_code_FRA','country_code_GBR', 'country_code_IND', 
                'country_code_IRL', 'country_code_ISR', 'country_code_NLD', 'country_code_USA',
                'country_code_other']  
            country_code = country_code
            country_list = []
            
            for i in country_code_list:
                if i == country_code:
                    i = 1
                    country_list.append(i)
                    
                #         print(i)
                else:
                    i = 0
                    country_list.append(i)
                #         print(i)
    
            final_list = input_list + category_list + country_list
            status_model = pickle.load(open('new_status_model.pkl', 'rb'))
    
            prediction_model = status_model.predict([final_list])   
    
            prediction_model = status_model.predict([final_list])
            dataset = prediction_model.astype(int)
    
            if dataset == 1:                
                return render_template('result.html', model_output = "Operating")
            elif dataset == 2:
                return render_template('result.html', model_output = "Acquired")
            elif dataset == 3:
                return render_template('result.html', model_output = "Closed")
            elif dataset == 4:
                return render_template('result.html', model_output = "IPO")
    
            return render_template('result.html', model_output = dataset)
            
        except Exception as e:
             print("The Exception is ", e)
             return "Something is going wrong....!"
    
    else:
        return render_template('index.html')
   
if __name__ == '__main__':
    app.run(debug=True) 
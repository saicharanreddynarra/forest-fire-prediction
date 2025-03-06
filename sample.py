from flask import Flask, request, render_template
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Paths to the model and CSV file
model_file_path = "forest_fire_model.pkl"  # Ensure this path is correct
csv_file_path = "C:/Users/saich/charan/fires/mapgrpah/data/Aag.csv"  # Ensure this path is correct

# Load the model
with open(model_file_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Load the CSV file
data = pd.read_csv(csv_file_path)

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/predict', methods=['POST'])
def predict():
    oxygen = float(request.form['oxygen'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])

    input_features = np.array([[oxygen, temperature, humidity]])
    prediction = model.predict(input_features)

    if prediction == 0:
        prediction_result = "FIRE DID NOT OCCUR"
    else:
        prediction_result = "FIRE OCCURRED"

    # Find the matching row in the CSV file
    matched_row = data[(data['Oxygen'] == oxygen) & 
                       (data['Temperature'] == temperature) & 
                       (data['Humidity'] == humidity)]
    
    if not matched_row.empty:
        # Retrieve the additional information
        forest_name = matched_row.iloc[0]['Forest Name']
        state = matched_row.iloc[0]['State']
        region = matched_row.iloc[0]['Region (Zone)']
        city = matched_row.iloc[0]['Area (City)']
    else:
        forest_name = state = region = city = "-.-"

    return render_template("index.html", 
                           prediction_result=prediction_result,
                           forest_name=forest_name,
                           state=state,
                           region=region,
                           city=city)

if __name__ == "__main__":
    app.run()

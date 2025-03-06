# Forest Fire Prediction System 🔥🌲

    This project is a Flask-based web application that predicts whether a forest fire will occur based on oxygen, temperature, and humidity inputs. It uses a 
    machine learning model trained on historical data and maps predictions to real-world locations from a dataset.

# 📂 Project Structure

    mapgraph/
    │── data/
    │   ├── Aag.csv               # Dataset containing fire data
    │   ├── 1.jpg, 2.jpg, ...     # Map images
    │── static/
    │   ├── countrymap.js         # JavaScript for mapping
    │   ├── mapdata.js
    │   ├── style.css             # Styling for the web app
    │── templates/
    │   ├── index.html            # Main frontend template
    │── forest_fire_model.pkl     # Trained ML model (Pickle file)
    │── sample.py                 # Flask app
    │── README.md                 # Documentation
    

# 🚀 Features
    Predicts forest fire occurrence based on environmental conditions.
    Matches predictions to locations using a CSV dataset.
    Flask web interface for user-friendly input and result display.

# 🧩 Dependencies
    pip install flask pandas numpy scikit-learn

# 📌 Usage
    Enter Oxygen, Temperature, and Humidity values.
    The model predicts whether a fire will occur and provides location details.

# 📜 License
    This project is open-source under the MIT License.

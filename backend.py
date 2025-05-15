pip install Flask
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Initialize Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")

# Load and prepare the dataset
data = pd.read_csv("Startups.csv")
x = data[["R&D Spend", "Administration", "Marketing Spend"]]
y = data["Profit"]

x = x.to_numpy()
y = y.to_numpy()
y = y.reshape(-1, 1)

# Train the model
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(xtrain, ytrain)

@app.route('/')
def home():
    # Render the HTML page
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from POST request
        user_input = request.get_json()
        rnd_spend = user_input['rnd_spend']
        admin_cost = user_input['admin_cost']
        marketing_spend = user_input['marketing_spend']

        # Make prediction
        input_data = np.array([[rnd_spend, admin_cost, marketing_spend]])
        predicted_profit = model.predict(input_data)

        # Return prediction
        return jsonify({
            "success": True,
            "predicted_profit": f"${predicted_profit[0][0]:,.2f}"
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

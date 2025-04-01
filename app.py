from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load your trained model
try:
    model = joblib.load('model.pkl')
except Exception as e:
    print(f"Error loading model: {e}")

# Home route to serve the HTML frontend
@app.route('/')
def home():
    return render_template('fake.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    news = request.form.get('news')
    if not news:
        return jsonify({'prediction': 'today is hoilday'})

    try:
        prediction = model.predict([news])[0]
        print(f"Raw model prediction: {prediction}")

        # Adjust prediction interpretation based on model output
        if prediction in [1, 'fake', True]:  
            result = 'Fake News'
        else:
            result = 'Real News'

        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'prediction': f'Error during prediction: {e}'})

if __name__ == '__main__':
    app.run(debug=True)

from django.shortcuts import render, redirect, get_object_or_404
from .models import CoffeeLog
from .forms import CoffeeLogForm
import joblib

# Load the trained model
model_path = "static\espresso_model.pkl"
model = joblib.load(model_path)

def map_sourness_bitterness(value):
    if value < 1.5:
        return "Very Bitter"
    elif 1.5 <= value < 2.5:
        return "Bitter"
    elif 2.5 <= value <= 3.5:
        return "Perfect"
    elif 3.5 < value <= 4.5:
        return "Sour"
    else:
        return "Very Sour"

def map_strength(value):
    if value < 1.5:
        return "Very Weak"
    elif 1.5 <= value < 2.5:
        return "Weak"
    elif 2.5 <= value <= 3.5:
        return "Perfect"
    elif 3.5 < value <= 4.5:
        return "Strong"
    else:
        return "Very Strong"


def coffee_logs(request):
    # Get the coffee logs from the session or an empty list if none are found
    coffee_logs = request.session.get('coffee_logs', [])
    # Create a list of predictions and recommendations for each log
    logs_with_predictions_and_recommendations = [
        (log, *get_recommendation(log)) for log in coffee_logs
    ]
    return render(request, 'coffee_logs.html', {
        'logs_with_predictions_and_recommendations': logs_with_predictions_and_recommendations
    })

def add_coffee_log(request):
    if request.method == 'POST':
        # Create a dictionary from the POST data
        new_log = {
            'bean_name': request.POST.get('bean_name'),
            'roast_level': request.POST.get('roast_level'),
            'dose': request.POST.get('dose'),
            'yield_amt': request.POST.get('yield_amt'),
            'extraction_time': request.POST.get('extraction_time'),
            'grind_size': request.POST.get('grind_size'),
            'water_temperature': request.POST.get('water_temperature'),
            # Assuming sourness_bitterness and strength are not user inputs
            # 'sourness_bitterness': request.POST.get('sourness_bitterness'),
            # 'strength': request.POST.get('strength'),
            'tools_used': request.POST.get('tools_used'),
            'notes': request.POST.get('notes')
        }

        # Append predictions to the log
        new_log['predicted_sourness_bitterness'], new_log['predicted_strength'], new_log['recommendation'] = get_recommendation(new_log)

        # Get the existing logs from the session
        coffee_logs = request.session.get('coffee_logs', [])
        # Append the new log
        coffee_logs.append(new_log)
        # Save back to the session
        request.session['coffee_logs'] = coffee_logs

        # Redirect to the coffee logs page to display the list
        return redirect('coffee_logs')
    else:
        # If not a POST request, just render the add log form
        return render(request, 'add_coffee_log.html')

def delete_coffee_log(request, log_index):
    # Get the existing logs from the session
    coffee_logs = request.session.get('coffee_logs', [])

    # Remove the log at the given index
    if 0 <= log_index < len(coffee_logs):
        coffee_logs.pop(log_index)

    # Save back to the session
    request.session['coffee_logs'] = coffee_logs

    # Redirect to the coffee logs page to display the updated list
    return redirect('coffee_logs')

import random
def get_recommendation(log):
    recommendation = ""

    # Use the model to predict sourness_bitterness and strength
    input_data = [
        [
            float(log.get('dose', 0)),
            float(log.get('yield_amt', 0)),
            float(log.get('extraction_time', 0)),
            float(log.get('grind_size', 0)),
            float(log.get('water_temperature', 0))
        ]
    ]
    predicted_values = model.predict(input_data)
    predicted_sourness_bitterness_value = predicted_values[0][0]
    predicted_strength_value = predicted_values[0][1]

    # Convert predicted values to mapped terms
    predicted_sourness_bitterness = map_sourness_bitterness(predicted_sourness_bitterness_value)
    predicted_strength = map_strength(predicted_strength_value)

    # Generate recommendations based on mapped terms
    if predicted_sourness_bitterness in ["Very Bitter", "Bitter"]:
        recommendation = random.choice(["Grind Coarser", "Lower water temp", "Increase dose"])
    elif predicted_sourness_bitterness in ["Very Sour", "Sour"]:
        recommendation = random.choice(["Grind Finer", "Raise water temp", "Decrease dose"])

    if not recommendation:
        if predicted_strength in ["Very Weak", "Weak"]:
            recommendation = random.choice(["Increase dose", "Grind Finer"])
        elif predicted_strength in ["Very Strong", "Strong"]:
            recommendation = random.choice(["Decrease dose", "Grind Coarser"])

    return predicted_sourness_bitterness, predicted_strength, recommendation



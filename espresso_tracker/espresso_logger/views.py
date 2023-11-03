from django.shortcuts import render, redirect, get_object_or_404
from .models import CoffeeLog
from .forms import CoffeeLogForm
import joblib

# Load the trained model
model_path = "ml_models/espresso_model.pkl"
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
    logs = CoffeeLog.objects.all()
    logs_with_predictions_and_recommendations = [(log, *get_recommendation(log)) for log in logs]
    return render(request, 'coffee_logs.html', {'logs_with_predictions_and_recommendations': logs_with_predictions_and_recommendations})



def add_coffee_log(request):
    if request.method == 'POST':
        form = CoffeeLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coffee_logs')
    else:
        form = CoffeeLogForm()
    return render(request, 'add_coffee_log.html', {'form': form})

def delete_coffee_log(request, log_id):
    log = get_object_or_404(CoffeeLog, id=log_id)
    if request.method == 'POST':
        log.delete()
        return redirect('coffee_logs')
    return render(request, 'delete_coffee_log.html', {'log': log})

import random
def get_recommendation(log):
    recommendation = ""

    # Use the model to predict sourness_bitterness and strength
    input_data = [
        [
            float(log.dose or 0),
            float(log.yield_amt or 0),
            float(log.extraction_time or 0),
            float(log.grind_size or 0),
            float(log.water_temperature or 0)
        ]
    ]
    predicted_sourness_bitterness_value, predicted_strength_value = model.predict(input_data)[0]

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


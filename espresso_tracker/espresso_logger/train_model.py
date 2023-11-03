import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
import joblib

# Assuming data.csv contains your data
data = pd.read_csv('data.csv')

# Splitting data into input and output
X = data[['dose', 'yield_amt', 'extraction_time', 'grind_size', 'water_temperature']]
y = data[['sourness_bitterness', 'strength']]

# Train a multi-output model
model = MultiOutputRegressor(RandomForestRegressor())
model.fit(X, y)

# Save the trained model for later use
joblib.dump(model, 'espresso_model.pkl')
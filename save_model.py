from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import os

# Make sure the folder exists
os.makedirs("Stock_Price_Prediction_Project/models", exist_ok=True)

# Create dummy LSTM model
model = Sequential([
    LSTM(10, input_shape=(24, 10)),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# Save the model to the models folder
model.save("Stock_Price_Prediction_Project/models/lstm_model.h5")

print("✅ Model saved successfully as lstm_model.h5")

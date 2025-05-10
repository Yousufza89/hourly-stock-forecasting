from tensorflow.keras.models import load_model

# Load the model
model = load_model("Stock_Price_Prediction_Project/models/lstm_model.h5")

# Print architecture summary
model.summary()

# (Optional) Access weights
weights = model.get_weights()
print("\nFirst layer weights:\n", weights[0])  # Just as an example

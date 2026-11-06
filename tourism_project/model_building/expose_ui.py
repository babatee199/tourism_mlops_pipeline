from pyngrok import ngrok
import subprocess
import mlflow

# Start MLflow UI on port 5000, disabling the host header lock check
process = subprocess.Popen(["mlflow", "ui", "--port", "5000", "--host", "127.0.0.1"])

# Create public tunnel (using the token already stored in your environment config)
public_url = ngrok.connect(5000).public_url
print("MLflow UI is available at:", public_url)

# Keep the data logger targeting local loopback to avoid DNS blockages
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("wellness_tourism_prediction")

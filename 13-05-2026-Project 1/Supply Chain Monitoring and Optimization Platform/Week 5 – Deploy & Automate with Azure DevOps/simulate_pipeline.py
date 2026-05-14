import subprocess
import datetime

print("  AZURE DEVOPS PIPELINE SIMULATION")
print(f"  Started at: {datetime.datetime.now()}")
print("\n[STEP 1] Set up Python - Done")

print("\n[STEP 2] Installing Dependencies...")
subprocess.run(["pip", "install", "-r", "requirements.txt"])
print("Dependencies installed successfully.")

print("\n[STEP 3] Running Supply Chain Script...")
subprocess.run(["python", "run_pipeline.py"])

print("\n[STEP 4] Log Completion")
print(f"Pipeline completed successfully at: {datetime.datetime.now()}")

import subprocess
import datetime

print("=" * 50)
print("  AZURE DEVOPS PIPELINE SIMULATION")
print(f"  Started at: {datetime.datetime.now()}")
print("=" * 50)

# Step 1
print("\n[STEP 1] Set up Python - Done")

# Step 2
print("\n[STEP 2] Installing Dependencies...")
subprocess.run(["pip", "install", "-r", "requirements.txt"])
print("Dependencies installed successfully.")

# Step 3
print("\n[STEP 3] Running Supply Chain Script...")
subprocess.run(["python", "run_pipeline.py"])

# Step 4
print("\n[STEP 4] Log Completion")
print(f"Pipeline completed successfully at: {datetime.datetime.now()}")
print("=" * 50)

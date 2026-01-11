import psutil
import time

THRESHOLD = 80

print("Monitoring CPU usage...")

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)

        if cpu > THRESHOLD:
            print(f"Alert! CPU usage exceeds threshold: {cpu}%")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
except Exception as e:
    print("Error occurred:", e)

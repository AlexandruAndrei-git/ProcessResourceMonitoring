# anomaly_detector.py

def detect_memory_leak(metrics, threshold=1024):
    anomalies = []
    for i in range(1, len(metrics)):
        prev_memory = metrics[i - 1]['memory']
        current_memory = metrics[i]['memory']

        if current_memory - prev_memory > threshold:
            timestamp = metrics[i]['timestamp']
            anomalies.append(f"Memory leak detected at timestamp {timestamp}")

    return anomalies


def detect_cpu_overload(metrics, threshold=90):
    anomalies = []
    for i in range(len(metrics)):
        cpu_percent = metrics[i]['cpu_percent']

        if cpu_percent > threshold:
            timestamp = metrics[i]['timestamp']
            anomalies.append(f"CPU overload detected at timestamp {timestamp}")

    return anomalies


def detect_handle_increase(metrics, threshold=10):
    anomalies = []
    for i in range(1, len(metrics)):
        prev_handles = metrics[i - 1]['handles']
        current_handles = metrics[i]['handles']

        if current_handles - prev_handles > threshold:
            timestamp = metrics[i]['timestamp']
            anomalies.append(f"Possible handle increase detected at timestamp {timestamp}")

    return anomalies

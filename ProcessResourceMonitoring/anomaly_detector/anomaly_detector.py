def detect_memory_leak(metrics, threshold=1024):
    """
    Detects memory leaks based on a given threshold.

    Args:
        metrics (list of dict): List of dictionaries containing metrics data.
        threshold (int, optional): Threshold for detecting memory leaks. Defaults to 1024.

    Returns:
        list of str: List of anomaly messages indicating memory leaks.

    Example:
        ['Memory leak detected at timestamp 2']
    """
    # Initialize an empty list to store anomaly messages
    anomalies = []

    # Iterate over the range of metrics starting from the second item
    for i in range(1, len(metrics)):
        # Extract memory values from the current and previous metrics
        prev_memory = metrics[i - 1]['memory']
        current_memory = metrics[i]['memory']

        # Check if the difference between current and previous memory exceeds the threshold
        if current_memory - prev_memory > threshold:
            # If true, create an anomaly message and append it to the list
            timestamp = metrics[i]['timestamp']
            anomalies.append(f"Memory leak detected at timestamp {timestamp}")

    # Return the list of anomaly messages
    return anomalies


def detect_cpu_overload(metrics, threshold=90):
    """
    Detects CPU overload based on a given threshold.

    Args:
        metrics (list of dict): List of dictionaries containing metrics data.
        threshold (float, optional): Threshold for detecting CPU overload. Defaults to 90.

    Returns:
        list of str: List of anomaly messages indicating CPU overload.

    Example:
        ['CPU overload detected at timestamp 2']
    """
    # Initialize an empty list to store anomaly messages
    anomalies = []

    # Iterate over the range of metrics
    for i in range(len(metrics)):
        # Extract CPU percent value from the current metric
        cpu_percent = metrics[i]['cpu_percent']

        # Check if CPU percent exceeds the threshold
        if cpu_percent > threshold:
            # If true, create an anomaly message and append it to the list
            timestamp = metrics[i]['timestamp']
            anomalies.append(f"CPU overload detected at timestamp {timestamp}")

    # Return the list of anomaly messages
    return anomalies


def detect_handle_increase(metrics, threshold=10):
    """
    Detects possible handle increase based on a given threshold.

    Args:
        metrics (list of dict): List of dictionaries containing metrics data.
        threshold (int, optional): Threshold for detecting handle increase. Defaults to 10.

    Returns:
        list of str: List of anomaly messages indicating possible handle increase.

    Example:
        ['Possible handle increase detected at timestamp 2']
    """
    # Initialize an empty list to store anomaly messages
    anomalies = []

    # Iterate over the range of metrics starting from the second item
    for i in range(1, len(metrics)):
        # Extract handle values from the current and previous metrics
        prev_handles = metrics[i - 1]['handles']
        current_handles = metrics[i]['handles']

        # Check if the difference between current and previous handles exceeds the threshold
        if current_handles - prev_handles > threshold:
            # If true, create an anomaly message and append it to the list
            timestamp = metrics[i]['timestamp']
            anomalies.append(f"Possible handle increase detected at timestamp {timestamp}")

    # Return the list of anomaly messages
    return anomalies

import psutil
import time


def monitor_process(process_name, duration, interval=5):
    """
    Monitors the specified process for a given duration, collecting metrics at regular intervals.

    Args:
        process_name (str): The name of the process to monitor.
        duration (int): The total duration of the monitoring in seconds.
        interval (float, optional): The sampling interval in seconds. Defaults to 5 seconds.

    Returns:
        list of dict: List of dictionaries containing metrics data for each sample.

    Example:
        [
            {'timestamp': 1641045600.123, 'cpu_percent': 20.1, 'memory': 1048576, 'handles': 15},
            {'timestamp': 1641045602.456, 'cpu_percent': 22.3, 'memory': 2097152, 'handles': 18},
            # ...
        ]

    Raises:
        StopIteration: If the specified process is not found.

    Note:
        The 'timestamp' key represents the time of each metric sample.
        'cpu_percent' is the CPU usage percentage.
        'memory' is the private memory usage in bytes.
        'handles' is the number of open handles or file descriptors.
    """
    # Try to find the process with the specified name
    try:
        process = next(
            p for p in psutil.process_iter(['pid', 'name']) if process_name.lower() in p.info['name'].lower())
        process_pid = process.info['pid']
    except StopIteration:
        # If the process is not found, raise an exception and print an error message
        print(f"Process '{process_name}' not found.")
        return

    # Initialize an empty list to store metrics data
    metrics = []

    # Record the start time of monitoring
    start_time = time.time()

    # Calculate the end time of monitoring based on the specified duration
    end_time = start_time + duration

    # Continue monitoring until the end time is reached
    while time.time() < end_time:
        # Collect CPU percent, memory info, and handles data
        cpu_percent = psutil.cpu_percent(interval=None if interval < 1 else interval)
        memory_info = psutil.Process(process_pid).memory_info()
        handles = psutil.Process(process_pid).num_handles()

        # Append the collected metrics to the list
        metrics.append(
            {'timestamp': time.time(), 'cpu_percent': cpu_percent, 'memory': memory_info.rss, 'handles': handles})

        # Sleep for the specified interval (adjusted if less than 1 second)
        time.sleep(interval if interval >= 1 else 1)

    # Return the list of collected metrics
    return metrics

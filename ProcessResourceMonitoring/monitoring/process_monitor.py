# process_monitor.py
import psutil
import time


def monitor_process(process_name, duration, interval=5):
    try:
        process = next(
            p for p in psutil.process_iter(['pid', 'name']) if process_name.lower() in p.info['name'].lower())
        process_pid = process.info['pid']
    except StopIteration:
        print(f"Process '{process_name}' not found.")
        return

    metrics = []
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        cpu_percent = psutil.cpu_percent(interval=interval)
        memory_info = psutil.Process(process_pid).memory_info()
        handles = psutil.Process(process_pid).num_handles()

        metrics.append(
            {'timestamp': time.time(), 'cpu_percent': cpu_percent, 'memory': memory_info.rss, 'handles': handles})
        time.sleep(interval)

    return metrics

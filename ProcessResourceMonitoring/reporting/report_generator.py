# report_generator.py
import csv
from datetime import datetime


def generate_report(process_name, metrics, anomalies=None):
    headers = ['Timestamp', 'CPU (%)', 'Private Memory (MB)', 'Handles']
    filename = f'{process_name}_metrics.csv'

    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(headers)

        for metric in metrics:
            timestamp = metric['timestamp']
            formatted_timestamp = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            cpu_percent = metric['cpu_percent']
            memory_mb = metric['memory'] / (1024 * 1024)
            handles = metric['handles']

            csv_writer.writerow([formatted_timestamp, cpu_percent, memory_mb, handles])

    print(f"Report generated: {filename}")

    if anomalies is not None and len(anomalies) > 0:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        anomaly_filename = f'{process_name}_anomalies_{current_time}.csv'
        with open(anomaly_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Anomaly'])
            csv_writer.writerows([[anomaly] for anomaly in anomalies])

        print(f"Anomalies report generated: {anomaly_filename}")

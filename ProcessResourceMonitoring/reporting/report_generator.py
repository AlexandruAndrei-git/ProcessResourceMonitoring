# report_generator.py
import csv
from datetime import datetime


def generate_report(process_name, metrics, anomalies=None):
    """
      Generates a CSV report for the specified process metrics and an anomalies report if anomalies are present.

      Args:
          process_name (str): The name of the monitored process.
          metrics (List[Dict[str, float]]): List of dictionaries containing metrics data.
          anomalies (List[str], optional): List of anomaly messages. Defaults to None.

      Returns:
          None

      Example:
          Report generated: example_process_metrics.csv

      Raises:
          ValueError: If the metrics or anomalies parameter has an invalid format.

      Note:
          The 'timestamp' key represents the time of each metric sample.
          'cpu_percent' is the CPU usage percentage.
          'memory' is the private memory usage in bytes.
          'handles' is the number of open handles or file descriptors.
      """
    # Define headers for the CSV file
    headers = ['Timestamp', 'CPU (%)', 'Private Memory (MB)', 'Handles']

    # Create a filename for the metrics CSV file based on the process name
    filename = f'{process_name}_metrics.csv'

    # Open the metrics CSV file in write mode
    with open(filename, 'w', newline='') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write the headers to the CSV file
        csv_writer.writerow(headers)

        # Iterate over each metric in the list of metrics
        for metric in metrics:
            # Extract individual metric components
            timestamp = metric['timestamp']
            formatted_timestamp = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            cpu_percent = metric['cpu_percent']
            memory_mb = metric['memory'] / (1024 * 1024)
            handles = metric['handles']

            # Write a row with formatted data to the CSV file
            csv_writer.writerow([formatted_timestamp, cpu_percent, memory_mb, handles])

    # Print a message indicating that the metrics report has been generated
    print(f"Report generated: {filename}")

    # Check if anomalies exist and if the count is greater than 0
    if anomalies is not None and len(anomalies) > 0:
        # Get the current time in a specific format for anomaly report filename
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        # Create a filename for the anomalies CSV file based on the process name and current time
        anomaly_filename = f'{process_name}_anomalies_{current_time}.csv'

        # Open the anomalies CSV file in write mode
        with open(anomaly_filename, 'w', newline='') as csvfile:
            # Create a CSV writer object
            csv_writer = csv.writer(csvfile)

            # Write the 'Anomaly' header to the anomalies CSV file
            csv_writer.writerow(['Anomaly'])

            # Write rows for each anomaly to the anomalies CSV file
            csv_writer.writerows([[anomaly] for anomaly in anomalies])

        # Print a message indicating that the anomalies report has been generated
        print(f"Anomalies report generated: {anomaly_filename}")

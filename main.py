# main.py
from ProcessResourceMonitoring.anomaly_detector.anomaly_detector import detect_memory_leak, detect_cpu_overload, \
    detect_handle_increase
from ProcessResourceMonitoring.monitoring.process_monitor import monitor_process
from ProcessResourceMonitoring.reporting.report_generator import generate_report


def main():
    """
       Main function to monitor a process, detect anomalies, and generate reports.

       The user is prompted to enter the process name, monitoring duration, and sampling interval.
       Default sampling interval is 5 seconds if not specified.

       Args:
           None

       Returns:
           None

       Example:
           Enter the process name: python
           Enter the monitoring duration in seconds: 10
           Enter the sampling interval in seconds (default: 5):
           Monitoring process 'python' for 10 seconds with a sampling interval of 5 seconds...
           Report generated: python_metrics.csv

       Note:
           Anomalies, if detected, will be printed during the execution.
       """
    # Prompt the user to input the process name
    process_name = input("Enter the process name: ")

    # Prompt the user to input the monitoring duration in seconds
    duration = int(input("Enter the monitoring duration in seconds: "))

    # Prompt the user to input the sampling interval in seconds (default: 5 seconds)
    interval_input = input("Enter the sampling interval in seconds (default: 5): ")

    # If the user provided an interval, convert it to an integer; otherwise, use the default of 5 seconds
    interval = int(interval_input) if interval_input else 5

    # Call the monitor_process function to collect metrics for the specified process
    metrics = monitor_process(process_name, duration, interval)

    # Detect anomalies in the collected metrics
    memory_leak_anomalies = detect_memory_leak(metrics)
    cpu_overload_anomalies = detect_cpu_overload(metrics)
    handle_increase_anomalies = detect_handle_increase(metrics)

    # Generate a report using the collected metrics and anomalies
    generate_report(process_name, metrics, memory_leak_anomalies + cpu_overload_anomalies + handle_increase_anomalies)


# Check if the script is being executed as the main module
if __name__ == '__main__':
    # Call the main function to initiate the monitoring and reporting process
    main()

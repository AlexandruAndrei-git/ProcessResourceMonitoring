# main.py
from ProcessResourceMonitoring.anomaly_detector.anomaly_detector import detect_memory_leak, detect_cpu_overload, \
    detect_handle_increase
from ProcessResourceMonitoring.monitoring.process_monitor import monitor_process
from ProcessResourceMonitoring.reporting.report_generator import generate_report


def main():
    process_name = input("Enter the process name: ")
    duration = int(input("Enter the monitoring duration in seconds: "))
    interval = int(input("Enter the sampling interval in seconds (default: 5): ") or 5)

    metrics = monitor_process(process_name, duration, interval)

    # Detect anomalies
    detect_memory_leak(metrics)
    detect_cpu_overload(metrics)
    detect_handle_increase(metrics)

    # Additional CSV for raw metrics
    generate_report(process_name, metrics)


if __name__ == '__main__':
    main()

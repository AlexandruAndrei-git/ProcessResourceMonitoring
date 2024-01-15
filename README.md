# Process Resource Monitoring and Reporting

## Description
This Python project is designed for monitoring and reporting process resource metrics, such as CPU usage, memory usage, and the number of open handles/file descriptors. It includes anomaly detection for potential issues like memory leaks, CPU overload, and handle increases.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Anomaly Detection](#anomaly-detection)
- [Reports](#reports)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
- Python 3.x installed
- Required Python packages: psutil (install using `pip install psutil`)

## Installation
1. Clone the repository: `git clone https://github.com/yourusername/your-repository.git`
2. Navigate to the project directory: `cd your-repository`

## Usage
1. Run the main script: `python main.py`
2. Follow the prompts to enter the process name, monitoring duration, and sampling interval.

## Folder Structure
ProcessResourceMonitoring/
 |-> ProcessResourceMonitoring
   |-> anomaly_detector
     |-> __init__.py
     |-> anomaly_detector.py
   |-> monitoring
     |-> __init__.py
     |-> process_monitoring.py
   |->reporting
     |-> __init__.py
     |-> report_generator.py
|-> main.py

## Anomaly Detection
- The anomaly detection module (`anomaly_detector.py`) contains functions for detecting memory leaks, CPU overload, and handle increases.
- Anomalies, if detected, will be included in the generated reports.

## Reports
- The `report_generator.py` script generates CSV reports for regular metrics and, if anomalies are detected, a separate CSV report for anomalies.

## Contributing
Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and improvements are welcome!


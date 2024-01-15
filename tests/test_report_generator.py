from ProcessResourceMonitoring.reporting.report_generator import generate_report
import pytest
from unittest.mock import patch, mock_open
from freezegun import freeze_time
from datetime import datetime


@pytest.fixture
def mock_csv_writer(mocker):
    return mocker.patch('csv.writer')


@pytest.fixture
def mock_open(mocker):
    return mocker.patch('builtins.open', mocker.mock_open())


@freeze_time("2022-01-01 12:00:00")
def test_generate_report(mock_csv_writer, mock_open):
    process_name = 'test_process'
    metrics = [
        {'timestamp': 1641045600, 'cpu_percent': 50, 'memory': 1048576, 'handles': 10},
        {'timestamp': 1641045660, 'cpu_percent': 60, 'memory': 2097152, 'handles': 15},
    ]
    anomalies = ["Anomaly 1", "Anomaly 2"]

    with patch('csv.writer') as mock_csv_writer, patch('builtins.open', mock_open):
        generate_report(process_name, metrics, anomalies)

    # Assertions
    mock_open.assert_called_once_with(f'{process_name}_metrics.csv', 'w', newline='')
    mock_csv_writer.assert_called_once_with(mock_open())
    expected_headers = ['Timestamp', 'CPU (%)', 'Private Memory (MB)', 'Handles']
    mock_csv_writer().writerow.assert_any_call(expected_headers)
    expected_rows = [
        ['2022-01-01 12:00:00', 50, 1.0, 10],
        ['2022-01-01 12:01:00', 60, 2.0, 15],
    ]
    for row in expected_rows:
        mock_csv_writer().writerow.assert_any_call(row)

    mock_open.reset_mock()

    with patch('csv.writer') as mock_csv_writer, patch('builtins.open', mock_open):
        generate_report(process_name, metrics, [])

    # Assertions for no anomalies
    mock_open.assert_called_once_with(f'{process_name}_metrics.csv', 'w', newline='')
    mock_csv_writer.assert_called_once_with(mock_open())
    mock_csv_writer().writerow.assert_any_call(expected_headers)
    for row in expected_rows:
        mock_csv_writer().writerow.assert_any_call(row)

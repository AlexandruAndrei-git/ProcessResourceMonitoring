import unittest
from unittest.mock import patch, MagicMock

import pytest

from ProcessResourceMonitoring.monitoring.process_monitor import monitor_process
import psutil


@pytest.fixture
def mock_psutil(mocker):
    mocker.patch('psutil.process_iter')
    mocker.patch('psutil.cpu_percent')
    mocker.patch('psutil.Process.memory_info')
    mocker.patch('psutil.Process.num_handles')


@pytest.fixture
def mock_process():
    return MagicMock(spec=psutil.Process)


def test_monitor_process(mock_psutil, mock_process):
    # Mock the psutil process information for testing
    mock_process_iter = patch('psutil.process_iter', return_value=iter([mock_process]))
    mock_cpu_percent = patch('psutil.cpu_percent', return_value=20.0)  # Mock CPU percentage for testing
    mock_memory_info = patch('psutil.Process.memory_info',
                             return_value=MagicMock(rss=1024))  # Mock memory info for testing
    mock_num_handles = patch('psutil.Process.num_handles', return_value=10)  # Mock number of handles for testing

    with mock_process_iter, mock_cpu_percent, mock_memory_info, mock_num_handles:
        # Call the monitor_process function
        duration = 5
        interval = 2
        metrics = monitor_process('test_process', duration, interval)

        # Assertions based on the mock data
        assert len(metrics) == duration // interval + 1
        assert all(isinstance(metric['timestamp'], float) for metric in metrics)
        assert all('cpu_percent' in metric and 'memory' in metric and 'handles' in metric for metric in metrics)

from ProcessResourceMonitoring.anomaly_detector.anomaly_detector import detect_memory_leak, detect_cpu_overload, \
    detect_handle_increase


def test_detect_memory_leak():
    metrics = [
        {'timestamp': 1, 'memory': 100},
        {'timestamp': 2, 'memory': 300},
        {'timestamp': 3, 'memory': 600},
    ]
    threshold = 200
    result = detect_memory_leak(metrics, threshold)
    assert result == ["Memory leak detected at timestamp 3"]


def test_detect_cpu_overload():
    metrics = [
        {'timestamp': 1, 'cpu_percent': 80},
        {'timestamp': 2, 'cpu_percent': 95},
        {'timestamp': 3, 'cpu_percent': 70},
    ]
    threshold = 90
    result = detect_cpu_overload(metrics, threshold)
    assert result == ["CPU overload detected at timestamp 2"]


def test_detect_handle_increase():
    metrics = [
        {'timestamp': 1, 'handles': 10},
        {'timestamp': 2, 'handles': 20},
        {'timestamp': 3, 'handles': 35},
    ]
    threshold = 30
    result = detect_handle_increase(metrics, threshold)
    assert result == ["Possible handle increase detected at timestamp 3"]

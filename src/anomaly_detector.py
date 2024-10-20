import numpy as np
from typing import List, Tuple

class AnomalyDetector:
    """
    A class to detect anomalies in a data stream using a sliding window and Z-score method.
    """

    def __init__(self, window_size: int = 100, threshold: float = 2):
        """
        Initialize the anomaly detector with a window size and threshold.

        :param window_size: The number of recent data points to consider.
        :param threshold: The Z-score threshold for detecting anomalies.
        """
        self.window_size = window_size
        self.threshold = threshold
        self.buffer: List[float] = []
        self.mean = 0
        self.std = 0

    def update(self, value: float) -> Tuple[bool, float]:
        """
        Update the detector with a new data point and check for anomalies.

        :param value: The new data point to be added.
        :return: A tuple indicating if the point is an anomaly and its Z-score.
        """
        self.buffer.append(value)

        if len(self.buffer) > self.window_size:
            self.buffer.pop(0)

        if len(self.buffer) == self.window_size:
            self.mean = np.mean(self.buffer)
            self.std = np.std(self.buffer)

        if self.std == 0:
            return False, 0

        z_score = abs((value - self.mean) / self.std)
        is_anomaly = z_score > self.threshold

        return is_anomaly, z_score

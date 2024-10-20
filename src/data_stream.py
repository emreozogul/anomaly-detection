import random
import math
from typing import Generator, Tuple

class DataStream:
    """
    A class to simulate a data stream with seasonal patterns, noise, and anomalies.
    """

    def __init__(self, base_value: float = 100, noise_level: float = 15, seasonal_amplitude: float = 10, anomaly_probability: float = 0.01):
        """
        Initialize the data stream with given parameters.

        :param base_value: The base value around which data fluctuates.
        :param noise_level: The level of random noise added to the data.
        :param seasonal_amplitude: The amplitude of the seasonal component.
        :param anomaly_probability: The probability of an anomaly occurring.
        """
        self.base_value = base_value
        self.noise_level = noise_level
        self.seasonal_amplitude = seasonal_amplitude
        self.anomaly_probability = anomaly_probability
        self.time = 0

    def generate(self) -> Generator[Tuple[int, float], None, None]:
        """
        Generate an infinite stream of data points with time and value.

        :yield: A tuple containing the current time and the generated value.
        """
        while True:
            # Calculate seasonal component
            seasonal = self.seasonal_amplitude * math.sin(2 * math.pi * self.time / 100)
            value = self.base_value + seasonal

            # Add random noise
            value += random.uniform(-self.noise_level, self.noise_level)

            # Introduce anomalies with a certain probability
            if random.random() < self.anomaly_probability:
                value *= random.uniform(1.5, 3)

            yield self.time, value
            self.time += 1

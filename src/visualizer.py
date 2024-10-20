import matplotlib.pyplot as plt
import numpy as np
from collections import deque

class Visualizer:
    """
    A class to visualize data streams and detected anomalies in real-time.
    """

    def __init__(self, max_points=100):
        """
        Initialize the visualizer with a maximum number of points to display.

        :param max_points: The maximum number of data points to display at once.
        """
        self.max_points = max_points
        self.times = deque(maxlen=max_points)
        self.values = deque(maxlen=max_points)
        self.anomalies = deque(maxlen=max_points)
        
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], 'b-')
        self.scatter = self.ax.scatter([], [], c='r', s=50)
        
        self.ax.set_ylim(-100, 300)  
        
    def update(self, time, value, is_anomaly):
        """
        Update the plot with a new data point and check for anomalies.

        :param time: The current time step.
        :param value: The value of the data point.
        :param is_anomaly: Boolean indicating if the point is an anomaly.
        """
        print(f"Time: {time}, Value: {value}, Is Anomaly: {is_anomaly}")  
        self.times.append(time)
        self.values.append(value)
        self.anomalies.append(value if is_anomaly else None)
        
        self.line.set_data(self.times, self.values)
        
        anomaly_times = [t for t, a in zip(self.times, self.anomalies) if a is not None]
        anomaly_values = [a for a in self.anomalies if a is not None]
        if anomaly_times and anomaly_values:
            self.scatter.set_offsets(np.column_stack((anomaly_times, anomaly_values)))
            self.scatter.set_color('r') 
        else:
            self.scatter.set_offsets(np.empty((0, 2)))
        
        self.ax.set_xlim(max(0, time - self.max_points), time)
        
        self.ax.relim()
        self.ax.autoscale_view()
        
        plt.draw()
        plt.pause(0.1)  
    
    def animate(self, data_generator, anomaly_detector, max_time=1000):
        """
        Animate the data stream and visualize anomalies.

        :param data_generator: The generator providing data points.
        :param anomaly_detector: The anomaly detector instance.
        :param max_time: The maximum time step to display.
        """
        for time, value in data_generator:
            is_anomaly, _ = anomaly_detector.update(value)
            self.update(time, value, is_anomaly)
            if time > max_time:
                break
        plt.show()

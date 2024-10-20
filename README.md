# Efficient Data Stream Anomaly Detection

This project implements a real-time anomaly detection system for continuous data streams. It uses a sliding window approach with Z-score calculation to identify anomalies in the data.

## Features

- Data stream simulation with seasonal patterns and random anomalies
- Real-time anomaly detection using Z-score method
- Live visualization of the data stream and detected anomalies

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

## Usage

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the main script:
   ```
   python src/main.py
   ```

## Algorithm Explanation

The anomaly detection algorithm uses a sliding window approach to calculate the Z-score for each new data point. If the Z-score exceeds a predefined threshold, the point is flagged as an anomaly. This method adapts to concept drift and seasonal variations by continuously updating the mean and standard deviation of the recent data points.

The algorithm is efficient and suitable for real-time processing, as it only needs to maintain a fixed-size buffer of recent values and perform simple statistical calculations for each new data point.

## Customization

- Adjust the `noise_level` in `DataStream` to change the randomness of the data.
- Modify the `max_time` parameter in the `Visualizer`'s `animate` method to control the duration of the visualization.

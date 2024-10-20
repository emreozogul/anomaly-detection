from data_stream import DataStream
from anomaly_detector import AnomalyDetector
from visualizer import Visualizer

def main():
    data_stream = DataStream()
    anomaly_detector = AnomalyDetector()
    visualizer = Visualizer()

    data_generator = data_stream.generate()
    visualizer.animate(data_generator, anomaly_detector, max_time=1000)

if __name__ == "__main__":
    main()


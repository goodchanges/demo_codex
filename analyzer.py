class TimeSeriesAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_moving_average(self, window_size):
        # Good, clean code with no syntax errors for the main branch
        if len(self.data) < window_size:
            return []
        
        averages = []
        for i in range(len(self.data) - window_size + 1):
            window = self.data[i:i + window_size]
            averages.append(sum(window) / window_size)
            
        return averages

# Test out the class
mock_market_data = [100, 102, 105, 103, 108, 110]
analyzer = TimeSeriesAnalyzer(mock_market_data)
print(f"3-Day Moving Average: {analyzer.get_moving_average(3)}")
def calculate_moving_average(data, window_size):
    if len(data) < window_size:
        return []
    
    averages = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        window_avg = sum(window) / window_size
        averages.append(window_avg)
        
    return averages

# Quick test case
if __name__ == "__main__":
    prices = [10, 12, 14, 13, 15, 18, 20]
    window = 3
    print(f"Moving averages: {calculate_moving_average(prices, window)}")
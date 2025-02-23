from functools import cached_property
import time

class DataAnalyzer:
    def __init__(self, dataset):
        self.dataset = dataset

    @cached_property
    def complex_analysis(self):
        print("Running expensive analysis...")
        time.sleep(2)  # Simulating heavy computation
        return sum(x**2 for x in self.dataset)

# Usage
analyzer = DataAnalyzer(range(1000000))
print("First access:")
t1 = time.time()
result1 = analyzer.complex_analysis
t2 = time.time()
print(f"Result: {result1}, Time: {t2-t1:.2f}s")

print("\nSecond access:")
t1 = time.time()
result2 = analyzer.complex_analysis
t2 = time.time()
print(f"Result: {result2}, Time: {t2-t1:.2f}s")

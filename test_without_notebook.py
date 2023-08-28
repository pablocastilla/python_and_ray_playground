import ray
ray.shutdown()
ray.init()

import time
start_time = time.time()

# calculate the average of a list of numbers with type checking
@ray.remote
def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

# generate a few lists of random numbers with different lengths and temperatures using ray
import random
random.seed(0)
@ray.remote
def generate_floor_data() -> list[float]:
    return [random.random()*20+1 for _ in range(10000000)]

floor_data_futures = [generate_floor_data.remote() for _ in range(10)]

print(f"Generating data time: {time.time() - start_time}")

averages = [average.remote(data) for data in floor_data_futures]
print(ray.get(averages))
print(f"Total time: {time.time() - start_time}")
import heapq
import random


def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost


random.seed(33)

values = range(1, 50)
cables = random.sample(values, 5)

print("Cables:", cables)
print("Min cables connecting cost:", min_cost_to_connect_cables(cables))

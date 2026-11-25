import time
import random

# 1. GREEDY APPROACH: Fractional Knapsack (Items can be broken into fractions)
# Time Complexity: O(N log N) | Space Complexity: O(N)
def fractional_knapsack(items, capacity):
    start_time = time.perf_counter()
    
    # Sort items by Profit/Weight ratio in descending order
    sorted_items = sorted(items, key=lambda x: x['profit'] / x['weight'], reverse=True)
    
    total_profit = 0.0
    remaining_capacity = capacity
    selected = []

    for item in sorted_items:
        if remaining_capacity == 0:
            break
        if item['weight'] <= remaining_capacity:
            remaining_capacity -= item['weight']
            total_profit += item['profit']
            selected.append((item['name'], "100%", item['profit']))
        else:
            fraction = remaining_capacity / item['weight']
            earned_profit = item['profit'] * fraction
            total_profit += earned_profit
            selected.append((item['name'], f"{fraction*100:.1f}%", round(earned_profit, 2)))
            remaining_capacity = 0

    exec_time = (time.perf_counter() - start_time) * 1000
    return round(total_profit, 2), selected, exec_time


# 2. DYNAMIC PROGRAMMING APPROACH: 0/1 Knapsack (Take full item or leave it)
# Time Complexity: O(N * W) | Space Complexity: O(N * W)
def zero_one_knapsack(items, capacity):
    start_time = time.perf_counter()
    n = len(items)
    
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        wt = items[i - 1]['weight']
        val = items[i - 1]['profit']
        for w in range(1, capacity + 1):
            if wt <= w:
                dp[i][w] = max(val + dp[i - 1][w - wt], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item = items[i - 1]
            selected.append((item['name'], "100%", item['profit']))
            w -= item['weight']

    selected.reverse()
    exec_time = (time.perf_counter() - start_time) * 1000
    return dp[n][capacity], selected, exec_time


# 3. PERFORMANCE BENCHMARK ON DIFFERENT INPUT SIZES
def run_benchmark():
    print("\n--- PERFORMANCE COMPARISON (GREEDY vs DYNAMIC PROGRAMMING) ---")
    print(f"{'Items (N)':<12} {'Capacity (W)':<15} {'Greedy Time (ms)':<20} {'DP Time (ms)':<18}")
    print("-" * 65)
    
    for n in [10, 50, 200, 500]:
        cap = n * 10
        test_items = [
            {"name": f"Item-{i}", "weight": random.randint(1, 20), "profit": random.randint(10, 100)}
            for i in range(n)
        ]
        _, _, t_greedy = fractional_knapsack(test_items, cap)
        _, _, t_dp = zero_one_knapsack(test_items, cap)
        print(f"{n:<12} {cap:<15} {t_greedy:<20.4f} {t_dp:<18.4f}")


if __name__ == "__main__":
    warehouse_items = [
        {"name": "Laptop Box", "weight": 10, "profit": 60},
        {"name": "Gaming Monitor", "weight": 20, "profit": 100},
        {"name": "Mechanical Keyboard", "weight": 30, "profit": 120},
        {"name": "Smartphone Crate", "weight": 15, "profit": 90},
        {"name": "Router Bundle", "weight": 25, "profit": 110}
    ]
    max_capacity = 50

    print("=== INTELLIGENT INVENTORY MANAGEMENT (KNAPSACK OPTIMIZATION) ===")
    print(f"Warehouse Storage Capacity: {max_capacity} kg\n")

    g_profit, g_items, g_time = fractional_knapsack(warehouse_items, max_capacity)
    print(f"[1] Fractional Knapsack (Greedy) -> Max Profit: ₹{g_profit} | Time: {g_time:.4f} ms")
    for name, qty, prof in g_items:
        print(f"    - {name} ({qty}) -> Profit: ₹{prof}")

    print()

    dp_profit, dp_items, dp_time = zero_one_knapsack(warehouse_items, max_capacity)
    print(f"[2] 0/1 Knapsack (Dynamic Programming) -> Max Profit: ₹{dp_profit} | Time: {dp_time:.4f} ms")
    for name, qty, prof in dp_items:
        print(f"    - {name} ({qty}) -> Profit: ₹{prof}")

    run_benchmark()
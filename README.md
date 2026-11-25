# Intelligent Inventory Management Using Knapsack Optimization

A Design and Analysis of Algorithms (DAA) project that solves warehouse inventory selection to maximize profit within a fixed storage capacity using **Greedy (Fractional Knapsack)** and **Dynamic Programming (0/1 Knapsack)** approaches.

## Algorithms Implemented
- **Fractional Knapsack (Greedy Approach):** Sorts items by Profit-to-Weight ratio (`profit / weight`) and allows partial item selection.
  - **Time Complexity:** `O(N log N)`
  - **Space Complexity:** `O(N)`
- **0/1 Knapsack (Dynamic Programming):** Uses a 2D DP table (`dp[N+1][W+1]`) to evaluate take-or-leave decisions for indivisible items.
  - **Time Complexity:** `O(N * W)`
  - **Space Complexity:** `O(N * W)`

## How to Run
```bash
python3 main.py
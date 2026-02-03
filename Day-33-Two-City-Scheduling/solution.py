class Solution(object):
    def twoCitySchedCost(self, costs):
        # Sort by the difference between cost to A and cost to B
        costs.sort(key=lambda x: x[0] - x[1])

        total_cost = 0
        n = len(costs) // 2

        # First n people go to city A
        for i in range(n):
            total_cost += costs[i][0]

        # Remaining n people go to city B
        for i in range(n, len(costs)):
            total_cost += costs[i][1]

        return total_cost

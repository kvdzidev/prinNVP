import numpy as np
import matplotlib.pyplot as plt

num_simulations = 1000
discount_rate = 0.10
years = 5

investment_cost_range = (150000, 300000)
marketing_cost_range = (30000, 80000)
maintenance_cost_range = (100000, 100000)
administration_cost_range = (50000, 50000)
num_users_mean = 30000
num_users_std = 10000
subscription_fee = 200
weekly_commission = 1000
weeks_per_year = 52
development_time_range = (0.5, 2)

np.random.seed(42)

npv_values = []

for _ in range(num_simulations):
    investment_cost = np.random.uniform(*investment_cost_range)
    marketing_cost = np.random.uniform(*marketing_cost_range)
    maintenance_cost = np.random.uniform(*maintenance_cost_range)
    administration_cost = np.random.uniform(*administration_cost_range)
    num_users = np.random.normal(num_users_mean, num_users_std)
    revenue_from_subscriptions = num_users * subscription_fee
    revenue_from_lessons = weekly_commission * weeks_per_year
    development_time = np.random.uniform(*development_time_range)

    total_revenue = revenue_from_subscriptions + revenue_from_lessons
    total_annual_costs = maintenance_cost + administration_cost

    npv = 0
    for t in range(1, years + 1):
        npv += (total_revenue - total_annual_costs) / (1 + discount_rate)**t

    npv -= (investment_cost + marketing_cost)

    npv_values.append(npv)

npv_values = np.array(npv_values)
mean_npv = np.mean(npv_values)
std_npv = np.std(npv_values)
probability_loss = np.mean(npv_values < 0)

print(f"Średnia wartość NPV: {mean_npv:.2f} zł")
print(f"Odchylenie standardowe NPV: {std_npv:.2f} zł")
print(f"Prawdopodobieństwo straty (NPV < 0): {probability_loss * 100:.2f}%")

plt.hist(npv_values, bins=50, edgecolor='black')
plt.axvline(x=mean_npv, color='red', linestyle='dashed', linewidth=2)
plt.title('Rozkład NPV w symulacji Monte Carlo')
plt.xlabel('Wartość NPV (zł)')
plt.ylabel('Liczba prób')
plt.show()

# Mikhail Arias
# CMP 131
# Week 8
# Lab 1
# Sales Bar Chart
# 10/28/2026

print("Sales Bar Chart")

# Get the Sales for the Stores

sales = []
for store in range(1, 6):
    amount = float(input(f"Enter today's sales for Store {store}: $"))

    while amount < 0:
        print("Error: Sales cannot be negative.")
        amount = float(input(f"Enter today's sales for Store {store}: $"))
    sales.append(amount)

    
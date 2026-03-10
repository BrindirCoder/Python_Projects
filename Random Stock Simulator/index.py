import random
import time

price = 100.00  # starting stock price

print("📈 Stock Market Simulator\n")

for i in range(50):
    change = random.uniform(-2, 2)   # price change
    price += change
    price = round(price, 2)

    if change >= 0:
        print(f"📈 Price: ${price} (+{round(change,2)})")
    else:
        print(f"📉 Price: ${price} ({round(change,2)})")

    time.sleep(0.5)

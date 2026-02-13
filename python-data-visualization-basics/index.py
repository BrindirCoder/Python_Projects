import matplotlib.pyplot as plt   # First install => pip install matplotlib

# Data
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [120, 150, 90, 200, 170]

# Create chart
plt.plot(days, sales)

# Labels
plt.title("Weekly Sales")
plt.xlabel("Days")
plt.ylabel("Sales")

# Show chart
plt.show()

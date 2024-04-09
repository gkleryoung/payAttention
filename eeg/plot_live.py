import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.dates as mdates
from datetime import datetime

# Initialize the plot
plt.figure(figsize=(10, 6))
plt.title("Live Wave Signal")
plt.xlabel("Time")
plt.ylabel("Reading")


def animate(i):
    try:
        # Assuming 'wave_data.txt' is in the same directory
        data = pd.read_csv(
            "wave_data.txt",
            sep=" ",
            names=["Timestamp", "Reading"],
            parse_dates=["Timestamp"],
            date_parser=lambda x: datetime.strptime(x, "%H:%M:%S"),
        )
        data = data.tail(20)  # Keep only the last 20 readings

        # Clear the plot to avoid the MAXTICKS error (rabbit hole)
        plt.cla()

        # Setting the date format for the x-axis
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
        plt.gca().xaxis.set_major_locator(
            mdates.AutoDateLocator(maxticks=5)
        )  # Adjust the number of ticks on the x-axis

        # Plotting the data
        plt.plot(data["Timestamp"], data["Reading"])
        plt.gcf().autofmt_xdate()  # Auto-format the date labels

        plt.title("Live Wave Signal")
        plt.xlabel("Time")
        plt.ylabel("Reading")
    except Exception as e:
        print(e)


# Animate mate
ani = FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False)

plt.tight_layout()
plt.show()

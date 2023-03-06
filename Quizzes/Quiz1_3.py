"""Plot High prices for IBM"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/IBM.csv")
    # TODO: Your code here
    plt.plot(df['High'])
    plt.ylabel("High price")
    plt.xlabel("Data point")
    plt.title("Plot of High prices for IBM")
    plt.grid(True)
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    test_run()

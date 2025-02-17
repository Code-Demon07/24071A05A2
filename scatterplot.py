import matplotlib.pyplot as plt

plt.scatter(df["Confirmed"], df["Deaths"])
plt.xlabel("Confirmed Cases")
plt.ylabel("Deaths")
plt.title("Confirmed Cases vs Deaths")
plt.show()

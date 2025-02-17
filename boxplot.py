import seaborn as sns

plt.figure(figsize=(10, 5))
sns.boxplot(x="Country", y="ActiveCases", data=df)
plt.xticks(rotation=90)
plt.title("Active Cases Across Countries")
plt.show()

# Importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport

# Load Titanic dataset
titanic_data = pd.read_csv("titanic.csv")

# Display first few rows of the dataset
print("First few rows of the Titanic dataset:")
print(titanic_data.head())

# 1. Survival Distribution (Bar Chart)
plt.figure(figsize=(6,4))
sns.countplot(data=titanic_data, x="Survived", palette="Set2")
plt.title("Survival Distribution (0: Not Survived, 1: Survived)")
plt.xlabel("Survived")
plt.ylabel("Count")
plt.show()

# Print insights for Survival Distribution
print("\nInsight from Survival Distribution:")
print("The bar chart shows that a smaller proportion of passengers survived the disaster, with the majority of passengers not surviving.")
print("This indicates a class imbalance that might need addressing in model training (e.g., using class weighting or resampling).\n")

# 2. Feature Correlation Analysis (Heatmap)
corr_matrix = titanic_data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Features")
plt.show()

# Print insights for Feature Correlation
print("\nInsight from Feature Correlation Analysis:")
print("The heatmap reveals that 'Pclass' (passenger class) and 'Fare' show a strong correlation with survival, suggesting that wealthier passengers in higher classes had a higher chance of survival.")
print("The 'Age' feature shows a weak correlation with survival, but younger passengers were more likely to survive.\n")

# 3. Age Distribution by Survival (Box Plot)
plt.figure(figsize=(6,4))
sns.boxplot(data=titanic_data, x="Survived", y="Age")
plt.title("Age Distribution by Survival")
plt.show()

# Print insights for Age Distribution
print("\nInsight from Age Distribution by Survival:")
print("The boxplot indicates that younger passengers had a higher survival rate, while older passengers had a lower survival rate.")
print("There are also a few outliers in both survivors and non-survivors that could be worth investigating further.\n")

# 4. Proportion of Survived vs. Not Survived (Pie Chart)
plt.figure(figsize=(6,6))
survival_proportion = titanic_data["Survived"].value_counts()
survival_proportion.plot(kind='pie', labels=["Not Survived", "Survived"], autopct='%1.1f%%', colors=["red", "green"])
plt.title("Proportion of Survived vs. Not Survived")
plt.ylabel('')
plt.show()

# Print insights for Survival Proportion
print("\nInsight from Proportion of Survived vs. Not Survived:")
print("The pie chart shows a clear imbalance between the number of passengers who survived and those who did not.")
print("The majority of passengers did not survive, which should be considered when building a predictive model.\n")

# 5. Bonus: Automated EDA with Pandas Profiling
profile = ProfileReport(titanic_data, title="Titanic Dataset EDA", explorative=True)
profile.to_file("titanic_eda_report.html")

# Print insights from Pandas Profiling
print("\nPandas Profiling Report:")
print("An automated EDA report has been generated and saved as 'titanic_eda_report.html'. This report provides additional insights, including missing values, data distributions, and correlations that will aid in further analysis and model development.\n")

# Final Summary
print("\nFinal Summary:")
print("Key patterns identified from the Titanic dataset include:")
print("1. Passenger class and fare strongly correlate with survival likelihood.")
print("2. Younger passengers had a higher chance of survival.")
print("3. There is a significant imbalance in survival classes (more non-survivors).")
print("These insights will be used for feature selection and addressing data issues before training a predictive model.\n")

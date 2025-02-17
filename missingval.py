df = pd.read_csv("your_dataset.csv") 
df.fillna(method='ffill', inplace=True)  
print("Missing values filled")

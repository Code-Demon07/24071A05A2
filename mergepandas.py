df1 = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Alice", "Bob", "Charlie"]})
df2 = pd.DataFrame({"ID": [4, 5, 6], "Name": ["David", "Eve", "Frank"]})

concat_df = pd.concat([df1, df2], ignore_index=True)
print("Concatenated DataFrame:\n", concat_df)

df3 = pd.DataFrame({"ID": [1, 2, 3], "Score": [90, 85, 95]})
merged_df = pd.merge(df1, df3, on="ID")
print("Merged DataFrame:\n", merged_df)

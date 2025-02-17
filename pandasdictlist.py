import pandas as pd

data_dict = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
df_dict = pd.DataFrame(data_dict)
print("DataFrame from Dictionary:\n", df_dict)

data_list = [["Alice", 25], ["Bob", 30], ["Charlie", 35]]
df_list = pd.DataFrame(data_list, columns=["Name", "Age"])
print("DataFrame from List:\n", df_list)

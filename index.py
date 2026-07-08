import pandas as pd
data = {
    "Name": ["Ashwin", "Rahul", "Priya"],
    "Age": [21, 30, 20],
    "city": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df.index)
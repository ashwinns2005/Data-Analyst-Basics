import pandas as pd

data = {
    "Name": ["Ashwin", "Rahul", "Priya"],
    "Age": [21, 30, 20]
}

df = pd.DataFrame(data)

print(df.info())

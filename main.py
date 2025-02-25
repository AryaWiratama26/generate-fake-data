from faker import Faker
import pandas as pd

fake = Faker()

data = [{"No":i+1, "Name" : fake.name()} for i in range(100)]


df = pd.DataFrame(data)
filename = 'test.csv'
df.to_csv(filename, index=False, encoding="utf-8")


from faker import Faker

fake = Faker()

def generate_data(*args, long_data):
    print(f"{args}{long_data}")
    # data = [{"No":i+1, "Name" : fake.name()} for i in range(100)]
    
generate_data((1,2,3,4,5),long_data=6)

import pandas as pd





# df = pd.DataFrame(data)
filename = 'test.csv'
# df.to_csv(filename, index=False, encoding="utf-8")


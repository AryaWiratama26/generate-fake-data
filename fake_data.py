from faker import Faker
import pandas as pd


fake = Faker()

def generate_data(data, long):
    
    new_data = []
    
    for i in range(int(long)):
        row = {}
        if "name" in data:
            row["Name"] = fake.name()
        if "email" in data:
            row["Email"] = fake.email()
        if "address" in data:
            row["Addres"] = fake.address()
        if "phone" in data:
            row["Phone"] = fake.phone_number()
        if "company" in data:
            row["Company"] = fake.company()
        if "country" in data:
            row["Country"] = fake.country()
        if "text" in data:
            row["Text"] = fake.text()
        if "url" in data:
            row["URL"] = fake.url()
            
        new_data.append(row)
    
    filename = 'static/hasil.csv'    
    df = pd.DataFrame(new_data)
    df.to_csv(filename, index=False)
        
    return filename
    
    
    


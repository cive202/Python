import pandas as pd

'''
Random sampling
'''
file_path = ""
contents = pd.read_csv()
sample = contents.sample(n=10,random_state=42)
'''with percentage'''
sample_per = contents.sample(frac = 0.2, random_state = 42)
print(sample)

'''
Stratified sampling
'''

form sklearn.preprocessing import train_test_split

train,test = train_test_split(
        df,
        test_size = 0.2,
        stratify = df['category'],
        random_state = 42
        )

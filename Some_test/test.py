import pandas as pd

df = pd.DataFrame({
    'name': ["Grzegorz", "Marek", "Sianek"],
    'age': [1,2,3]})

df.to_csv('out.csv',index=False,sep=';')
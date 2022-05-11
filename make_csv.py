import pandas as pd

#script to transform dictionary into df
#then save to csv to test pushing csv
#to github

my_data = {'a' : [1,2,3], 'b': [4,5,6]}
print("my data is {0}".format(my_data))
df = pd.DataFrame.from_dict(my_data)
print("my df is {0}".format(df))
df.to_csv('./output.csv')



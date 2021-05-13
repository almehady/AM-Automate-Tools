import pandas as pd
# read the csv file
data = pd.read_csv("bcs.csv")
'''
drop the duplicated value based one question and option_1.
we might have multiple same question as কোন বানানটি সঠিক ? 
if and only if the question and option_1 have same value drop it
'''
data_purified = data.drop_duplicates(['question', 'option_1'])
df = pd.DataFrame(data_purified,)

# save data in new file
df.to_csv('bcs_purified.csv', index=False, encoding='utf-8')

# show a msg after finish the task
print('We have done it')

import pandas as pd
users = pd.read_json('https://stats.foldingathome.org/api/team/3103')['donors']
data = pd.DataFrame(users.to_list())
rank = data[data['name'] == 'dylannelson'].index[0]
print('Current Rank is: {}'.format(rank))
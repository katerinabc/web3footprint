import pandas as pd
import json
import glob
import os

# Private social capital
# this is about the number of people you DM
# The info for this is in 
        
# extract users I DMed from account['relationships']
with open("discordumb/account/user.json", "r") as read_file:
    account = json.load(read_file)
    
    name = account['username']
    relationships = account['relationships'] # friends with their ID and username

    #relationships is a list of nested dictionary

def get_vals(nested, key):
    # get values from a nested dictionary inside a list
    result = []
    if isinstance(nested, list) and nested != []:   #non-empty list
        for lis in nested:
            result.extend(get_vals(lis, key))
    elif isinstance(nested, dict) and nested != {}:   #non-empty dict
        for val in nested.values():
            if isinstance(val, (list, dict)):   #(list or dict) in dict
                result.extend(get_vals(val, key))
        if key in nested.keys():   #key found in dict
            result.append(nested[key])
    return result

DMFriends = get_vals(relationships, 'username')

# extract users I mentioned inside guilds.
# the data in messages is per channel
# ASSUMPTION: channel_ids are unique in Discord. 
# Two guilds will not have the same channel id
# this will be a list of ids. 
# I need the user id and the guild id and the text

# loop through folders in messages, open file called channel.json and store data
files = glob.glob('discordumb/messages/*/*.json')
dfs = []
for fp in files:
    with open(fp) as data_file:
        data = json.load(data_file)
        dfs.append(pd.json_normalize(data))
guilds = pd.concat(dfs, ignore_index = True)

#guilds.id is a string...
guilds['id'] = guilds['id'].apply(lambda x: int(x) if x.isdigit() else x)

# check if correct
print(len(next(os.walk('discordumb/messages'))[1]) == len(guilds))

# loop through folders in messages, open file called messages.csv, extract data
files = glob.glob('discordumb/messages/*/*.csv')
dfs = []
for fp in files:
    tst = pd.read_csv(fp)
    tmp = fp.replace('discordumb/messages/c', '')
    tmp = tmp.replace('/messages.csv', '')
    tst = tst.assign(channel = tmp)
    dfs.append(tst)
msg = pd.concat(dfs, ignore_index = True)

# most active guild
# new dataset with guild.id, channel.id from guilds and id from msg

guildactivity = msg[['ID', 'channel']].groupby('channel').count()


# the index for msg and guilds are the channel ids
guildactivity = pd.merge(msg, guilds, left_on='channel', right_on='id', how='left')
# still no matches....
# ok, that's stupid. channel ids in messages.csv do not match ids in guilds. 
# ids in messages are message ids... 




guildactivity = msg.ID.map(guilds.set_index('id')['guild.name'])
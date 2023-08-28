# web3footprint

*Note: This is a brand new project. The idea is to let people calculate their web3footprint, by combining on-chain and off-chain data. I'm beginning with off-chain data, namely Discord. The data dumb Discord gives you is useless, unless you know how data analysis and how to code. I'm unsure about the end-result. It will either be a score you can cast or a NFT you can mint. *

## Web3 Footprint
Some years ago I joined a paid community. I trusted the company behind it, and was from day 1 sourrunded by great people. We were part of a cohort and learned together. The schedule was intense. The program started on a high, but ended very low. So low that I was grateful for the planned solo hike to disconnect from everything. The complete world. 

Since then I was weary joining new communities. So I'm finding myself between a rock and a hard place: Knowing how important community is, not just for web3, but at an individual level, and knowing how much damage a community can do to a person. 

While I'm entering and exiting Discord servers I was wondering what footprint I left behind: How did I impacted the community, and is there a way to measure this impact? The vision I'm having is for interested members to be able to check out how welcoming a community is, and, potentially its members (if they agreed to it) and their reputation.

## The math behind the number

*WIP*
Combination of growth of social capital, complexity of messages, depth and breath of discussed topics (breath = Blau index of keywords, depth = # of posts on topic x; breath could also just be number of topics), sentiment.


### Variables for reputation score
- Number of contributions (activity)
- Validation of contributions: Ratio of how many posts got a reply (not possible with discord dumb)
- Sentiment of contributions (-1 to +1)
- Number of connections (dm, guilds)

### Generalist vs specialist score
- Diversity of expertise (Blau Index)
- 



- Closure positive impact (# of closed triangles) --> but given I have an ego-network this will be hard
- Reciprocal 

## Installation

## TODO
DONE extract number of people from messages 
*I got the list of names, but not saving IDs. this will be necessary for matching messages in guilds to people if I want to do that* 
DONE extract number of servers from discord dumb 
- create a file: guild, channel, number msg in channel
- explore: messages X time, messages X people, LDA
- not sure if necessary but might be funny fact: used emojis. I think it's stored in account. i saw it when scanning one of hte json files..

https://support.discord.com/hc/en-us/articles/360004957991-Your-Discord-Data-Package


## Questions
- DM text not stored ?? --> yes it's stored in message folder
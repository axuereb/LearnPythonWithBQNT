
tickers = ['7203', '1398', 'WMT']
exchs = ['JT', 'HK', 'US']
yks = ['Equity']

# Given the above you may try this: 
for index in range(len(tickers)):
    print('{} {} {}'.format(tickers[index], exchs[index], yks[min(index,len(yks)-1)]))

# It is better to use this: 
for ticker, exchange, yellow_key in zip(tickers, exchs, len(tickers)*yks):
    print('{} {} {}'.format(ticker, exchange, yellow_key))
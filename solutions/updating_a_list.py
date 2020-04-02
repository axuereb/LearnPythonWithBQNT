# 1 
ccy = ['EUR', 'JPY', 'GBP', 'CAD', 'USD']
ccy[-1] = 'USd'

# 2
ccy[2:4] = ['GBp', 'CAd'] 

# 3
ccy[::-1]

# 4 
ccy.pop()

# 5 
ccy.append('AUD')

# 6 
ccy.extend(('RUB', 'CNY',))

# 7
# ccy.append(('RUB', 'CNY',)) >> [...,['RUB', 'CNY']] 
# ccy.extend(('RUB', 'CNY',)) >> [...,'RUB', 'CNY'] 
# see doc string for further info. 
(help(ccy.append), help(ccy.extend))

ccy = 'EUR' # 'USD' # CNY 

if ccy == 'EUR': 
    print('EU')
elif ccy == 'USD': 
    print('US')
elif ccy == 'CNY':
    print('CN')
else:
    print('Other Country')
    
# Consider this alternative that does not use any if statements. 

mapping = {'EUR' : 'EU', 'USD' : 'US', 'CNY' : CN}

mapping.get(ccy, 'Other Country')
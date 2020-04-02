# 1 
"Govt" in "T 5 05/05/2025 Govt"

# 2
"GOVT" in "T 5 05/05/2025 Govt".upper()

# 3 
"GOVT" in "GOVT US Equity".upper()[-4:]

## Compare using %timeit with:
## "GOVT" == "GOVT US Equity".upper()[-4:]

# 4 
"T 5 05/05/2025 Govt".upper().endswith('GOVT')

# 5 
"GOVT US Equity".upper().endswith("GOVT")

# 6 
# suboptimal 
ticker[:7] + 'BGN' + ticker[10:]

# 7 
# Better solution. 
ticker = 'EURJPY EBS Curncy'
split = ticker.split(" ")
split[1] = 'BGN'
split.join()
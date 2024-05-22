import re 

# Using lookbehind 
example1 = re.findall(r'\d+(?!.*[(])', 
					"80'er salat med iceberg, tomat, løg, agurk, ærter, majs og tomat (15,7)") 
print(example1) 
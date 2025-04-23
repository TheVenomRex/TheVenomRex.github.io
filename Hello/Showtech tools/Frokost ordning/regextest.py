import re

i = "80'ernes hit salat"
matches = re.findall(r'\d+(?!.*[(])', i)
print(matches)  # Expected output: ['80']

# regular expressions / regex - are a powerful tool for working with strings and text data in python. 
# they allow you to match and manipulate strings based on patterns, 
# making it easy to perform complex string operations with just few lines of code


import re

# pattern = "Iron"
pattern = r"[A-Z]+ron"

text = '''
Iron Man is the superhero persona of Anthony Edward Tony Stark, a businessman and engineer who runs the weapons 
manufacturing company Stark Industries. When Stark was captured in a war zone and sustained a severe heart wound, 
he built his Iron Man armor and escaped his captors. Iron Man's suits of armor grant him 
superhuman strength, flight, energy projection, and other abilities. 
The character was created in response to the Vietnam War as Lee's attempt to create a likeable pro-war character. 
Since his creation, Iron Man has been used to explore political themes, with early Iron Man stories being set in the Cold War. 
The character's role as a weapons manufacturer proved controversial, and Marvel moved away from geopolitics by the 1970s. 
Instead, the stories began exploring themes such as civil unrest, technological advancement, corporate espionage, alcoholism, and governmental authority.
'''

# match = re.search(pattern,text)
# print(match)

matches = re.finditer(pattern, text)
for match in matches:
    print(match)



# Learn about METACHARACTERS
# EXPLORE https://regexr.com/
import re

text = "Hi, my name is Aarnav Kothawade. Aarnav was brought up in Nashik, Maharashtra"
match = re.search("aarnav", text, re.IGNORECASE)

if match :
    print("Match found")
    print("Start Index: ",match.start())
    print("Stop Index:",match.end())
    print("Span of Word",match.span())

#Returns the first appearance of the text mentioned

match = re.findall("Aarnav", text)
print(match)


new = re.sub("Aarnav", "Sumay", text)
print(new)
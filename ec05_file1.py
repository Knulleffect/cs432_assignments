"""
This is a placeholder file.
"""
s = "Hello World!"
s = s.rstrip("!.,")
words = s.split()
new_s = f"{words[1].capitalize()}, {words[0].lower()}!"
print(new_s)
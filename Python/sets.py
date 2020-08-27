# Create an empyt set
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)    # no elements appean more than once in set
print(s)

s.remove(2)
print(s)

print(f"The set has {len(s)} elements.")

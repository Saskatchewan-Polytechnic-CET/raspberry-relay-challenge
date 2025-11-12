# Exercise 2
def encode_character(x):
   y = format(ord(x), '08b')
   z = f"{y[:4]} {y[4:]}"
   return f"{x} =>\t {z}"

# Edit me!
print(encode_character("h"))
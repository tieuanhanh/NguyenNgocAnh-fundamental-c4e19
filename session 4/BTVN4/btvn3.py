import re
import string

name = input ("Your full name: ")

r = " ".join(name.split())

print (r.title())
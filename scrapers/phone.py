import urllib,re

from urllib import urlopen
f =urlopen("https://www.justdial.com/Delhi/Baby-Sitters-in-Rohini/nct-10031239")
s = f.read()
print(re.findAll(r"\+\d{2}\s?0?\d{10}",s))
print(re.findAll(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s))

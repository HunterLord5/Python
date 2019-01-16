#   DICTIONARIES ARE NOTHING BUT KEY VALUE PAIR

d1 = {}
print(type(d1))

d2 = {"harry":"Burger",
      "Sarfi":"Biryani",
      "tani":"kebab",
      "Ankit":{"B":"Roti", "L":"Rice","D":"Rolls"}}
print(d2)
d2["Rohan"] = "Junk food"
print(d2)
d2[420] = "lollipop"
print(d2)
del d2["harry"]
print(d2)
print(d2["Sarfi"])
# d3 = d2           # Here pyton is not creating new dictionary, d3 is just a new
# del d3["tani"]    #pointer referring to the same dictionary, so if we delete from d3
# print(d2)         #it will reflect the original one
d3 = d2.copy()
del d3["tani"]      #Always use copy method if you want to create a new dictionary of same element
print(d3, "\n", d2)
d2.update({"Leena":"toffee"})  #same as line no. 11. Its better way to use update method
print(d2)
print(d2.keys())
print(d2.values())
print(d2.items())
# A DICTIONARY WHICH WILL RETURN THE USER REQUESTED WORD

dict = {"Abandoned":"having been deserted or left",
        "Entrepreneur":"a person who sets up a business or businesses, taking on financial risks in the hope of profit.",
        "Miscellaneous":"of items or people gathered or considered together) of various types or from different sources",
        "Monitor":"a device used for observing, checking, or keeping a continuous record of something"}

print("Abandoned\nEntrepreneur\nMiscellaneous\nMonitor")
print("Enter the word from above list in order to see the meaning:", end= " ")
var1 = input()
print(var1, " = ", dict[var1])
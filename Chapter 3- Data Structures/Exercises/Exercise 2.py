'''Start with the list you used in Exercise 1, but instead of just

printing each person’s name, print a message to them. The text of each message should be the same, but each message should be 

personalized with the person’s name.'''



names = ['Ronnie, 'Tyler', 'Dani']

msg = f"Hello, {names[0].title()}!"
print(msg)

msg = f"HI, {names[1].title()}!"
print(msg)

msg = f"Hello! How are you?, {names[2].title()}!"
print(msg)

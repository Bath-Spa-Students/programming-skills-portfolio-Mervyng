#If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, invitingthem to dinner.




# Invite some people to dinner.
guests = ['Guido van Rossum, 'Jack Turner', 'Lynn Hill']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, Hi sir, please come sit with us and have dinner.")

name = guests[2].title()
print(f"{name}, please come and eat.")

name = guests[1].title()
print(f"\nSorry, {name} sorry I can't make it to dinner.")

# Jack can't make it! Let's invite Gary instead.
del(guests[1])
guests.insert(1, 'Gary Snyder')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, sorry I can't come home for dinner.")

name = guests[1].title()
print(f"{name}, please come to the party dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

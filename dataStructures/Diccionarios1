#Let’s say we have two lists that we want to combine into a 
#dictionary, like a list of students and a list of their heights, 
#in inches:

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

#Python allows you to create a dictionary using 
# a dict comprehension, with this syntax:

zipStudents = zip(names, heights)
print("zipStudents: ", zipStudents)

students = {key:value for key, value in zip(names, heights)}
students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
 print(students)

#zip() combines two lists into an iterator of tuples with the list elements paired together. This dict comprehension:

 drinks = ["espresso", "chai", "decaf", "drip"]
 caffeine = [64, 40, 0, 120]

 zipped_drinks = zip(drinks, caffeine)
 print(zipped_drinks)

 drinks_to_caffeine = {key:value for key, value in zipped_drinks}
 print(drinks_to_caffeine)

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
 print(plays)
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
 print("After: ", plays)
library = {"The Best Songs": plays, "Sunday Feelings": {}}
 print(library)

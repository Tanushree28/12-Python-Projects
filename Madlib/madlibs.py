#string concatenation(put strings together)
#suppose we want to create string that says "subscribe to __"

#youtuber = "Coder" #some string variable

#a few ways to do this
#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber)) #in the curly braces the value of youtuber is placed
#print(f"subscribe to {youtuber}")  #app string

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")
madlib = f"Computer programming is so {adj}! It makes me so excited all the times because I love to {verb1}. Stay hydrarted and {verb2} like you are {famous_person}!"

print(madlib)
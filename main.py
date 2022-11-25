# ###CSV files are more convenient and efficient in python as it stores numbers and data in large amounts and lets us do analitics such as avrage , mode and mean .

# MyNumberString = (input("Please enter 5 numbers separeted by commas: "))

# file = open("numList.csv", "w")
# file.write(MyNumberString)
# file.close()
# file = open("numList.csv","r")
# dataIn = file.read()
# file.close()
# print(dataIn)
# MyList = dataIn.split(",")
# print(MyList)
# MyList = [int(item) for item in MyList]

# MyList.sort()
# print(MyList)

# print("min Value: ", min(MyList))
# print("max Value: ", max(MyList))

# import statistics
# Average=statistics.mean(MyList)
# print(Average)


##Anagrams are words that contain the same letters. Eg. car and arc are anagrams of each other 

 

def is_anagram(w1, w2):
  if sorted(w1) == sorted(w2): 

    return True 

  else: 

    return False 

 

word1 = input("Enter the first word:") 

word2 = input("enter the second word:") 

 

##Test whether the sorted strings are the same as each other 

##If the sorted strings are the same as each other then they must be anagrams 

 

if(sorted(word1) == (sorted(word2))):
  print("YES") 

if(sorted(word1))== (sorted (word2)));
  print(word1)"is an anagram of")































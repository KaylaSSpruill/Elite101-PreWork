#Kayla Spruill
#Elite101 prework

#Intro to the user
print("I am a chatbot and I would love to chat with you.")

user = input("Hi would like to know your name, please enter your name: \n")

print("Nice to meet you, " + user + "!" )


while True:
  goodDay = input("Did you have a good day " + user + "? Please use yes or no \n")
  if goodDay == 'yes':
    print("good to hear "+ user)
    break
  elif goodDay == 'no':
    print("I am sorry to hear that " + user)
    break
  else :
    print("Please answer with yes or no, I am still learning :)")

hobbies = input("Well " + user + " what do you like to do for fun? \n")

print(hobbies + " sounds really fun")



while True:
  planForToday = input("Do you have any plans for today? Please use yes or no: \n ")
  if planForToday == 'yes':
    plans = input("What are your plans: \n")
    print(plans + " sounds like a lot of fun")
    break
  elif planForToday == 'no':
    print("well I guess you can spend the day " + hobbies )
    break
  else :
    print("Please answer with yes or no, I am still learning :)")
  

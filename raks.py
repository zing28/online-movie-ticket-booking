def city():
  print("HELLO !! WELCOME TO MOVIE TICKET BOOKING")
  print("Where do you want to watch the movie ?")
  print("\t\tCities\n1.Chennai\n2.Mumbai\n3.Delhi")
  ch=int(input("choose your option: "))
  if ch == 1:
    theatre_type()
  elif ch == 2:
    theatre_type()
  elif ch == 3:
    theatre_type()
  else:
    print("Invalid choice")
def theatre_type():
  print("\t\twhich theater do you wish to see movie? ")
  print("1.Inox")
  print("2.Pvr")
  print("3.back to city")
  a = int(input("choose your option: "))
  movie(a)
  return 0
def movie(theatre):
  if theatre == 1:
    t_movie()
  elif theatre == 2:
    t_movie()
  elif theatre == 3:
    t_movie()
  elif theatre == 4:
    city()
  else:
    print("Invalid choice")
def t_movie():
    print("which movie do you want to watch?")
    print("1.Leo ")
    print("2.Killer of the Flower Moon ")
    print("3.Rdx")
    print("4.The Marvels")
    print("5.Back to Theatre type")
    movie = int(input("choose your movie: "))
    if movie==1:
      timing()
    elif movie==2:
      timing()
    elif movie==3:
      timing()
    elif movie==4:
      timing()
    elif movie == 5:
      theatre_type()
    else:
      print("Invalid choice!")
def timing():
  time1 = {"1": "10.00-1.00","2": "1.10-4.10","3": "4.20-7.20","4": "7.30-10.30"}
  time2 = {"1": "10.15-1.15","2": "1.25-4.25","3": "4.35-7.35","4": "7.45-10.45"}
  time3 = {"1": "10.30-1.30","2": "1.40-4.40","3": "4.50-7.50","4": "8.00-10.45"}
  print("\t\tHere are the show timings!!")
  print("1.",time1)
  print("2.",time2)
  print("3.",time3)
  print("4.Go back to Movie selection!")
  time=int(input("Enter your time slot:"))
  if time==1:
    t=input("Enter your timing option:")
    x=time1[t]
    print("\tSUCCESSFUL!\tEnjoy your movie @ ",x)
  elif time==2:
    t=input("Enter your timing option2:")
    x=time2[t]
    print("\tSUCCESSFUL!\tEnjoy your movie @ ",x)
  elif time==3:
    t=input("Enter your timing option:")
    x=time3[t]
    print("\tSUCCESSFUL!\tEnjoy your movie @ ",x)
  elif time==4:
    t_movie()
  else:
    print("Opps Sorry there is no show for this time")




city()

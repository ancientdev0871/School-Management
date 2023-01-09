import time
def wish():
  t = time.strftime('%H:%M:%S') 
  hour = int(time.strftime('%H'))
  # hour = int(input("Enter hour: "))
  # print(hour)

  if(hour>=0 and hour<12):
    return "Good morning Sir!"
  elif(hour>=12 and hour<17):
    return "Good afternoon Sir!"
  elif(hour>=17 and hour<0):
    return "Good evening Sir!"

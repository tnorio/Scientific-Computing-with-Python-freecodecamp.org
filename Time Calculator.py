def add_time(start, duration,weekday=None):
  WEEKDAYS = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]

  #sumtime
  starthour = start.split(":")[0]
  durationhour =  duration.split(":")[0]
  startmin = start.split(":")[1][0:2]
  durationmin = duration.split(":")[1][0:2]
  ampmstart = start.split()[1]
  ampmflip = {"AM":"PM","PM":"AM"}

  endhour = str(int(starthour) + int(durationhour))
  endmin = str(int(startmin) + int(durationmin))

  #sumin 0 before
  if int(endmin) >= 60 :
    endhour = str(int(endhour) + (int(endmin) // 60))
    endmin = str(int(endmin) % 60)
  if len(endmin) < 2:
    endmin = "0"+ endmin
  
  ndays = int(endhour) // 24

  if (ampmstart == "PM") and int(endhour) >= 12:
    ndays += 1


  flipcount = (int(endhour)) // 12
  if flipcount % 2 == 1:
    ampm = ampmflip[ampmstart]
  else:
    ampm = ampmstart

  # AMPMtime
  endhour = int(endhour) % 12
  if endhour == 0:
    endhour = 12

  if int(ndays) == 1:
    ndayslater = "(next day)"
  elif int(ndays) > 1:
    ndayslater = f"({int(ndays)} days later)"

  #wichday?
  if weekday != None:
    for days in range(0,7):
      if weekday.upper() == WEEKDAYS[days]:
        today = WEEKDAYS[days]
        if ndays < 1:
          returnday = today
        else:
          weekdaysext= WEEKDAYS * (1+int(ndays))
          returnday = weekdaysext[WEEKDAYS.index(today) + int(ndays)]
  

  if weekday != None:
    if ndays >=1:
      new_time = f"{endhour}:{endmin} {ampm}, {returnday.capitalize()} {ndayslater}"
    else:
      new_time = f"{endhour}:{endmin} {ampm}, {returnday.capitalize()}"
  if weekday == None:
    if ndays >=1:
      new_time = f"{endhour}:{endmin} {ampm} {ndayslater}"
    else:
      new_time = f"{endhour}:{endmin} {ampm}"


  return new_time

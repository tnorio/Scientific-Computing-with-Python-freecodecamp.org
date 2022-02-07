def arithmetic_arranger(problems, resultshow=False):
  if len(problems) >5:
    return "Error: Too many problems."

  for digits in problems:
    for i in digits:
      if i not in ("1","2","3","4","5","6","7","8","9","0","+","-"," ","*","/"):
        return "Error: Numbers must only contain digits."
      elif i == "*" or i == "/":
        return "Error: Operator must be '+' or '-'."

    for size in digits.split():
      if int(len(size)) > 4:
        return "Error: Numbers cannot be more than four digits."

  #results
  firstnum = ""
  secondnum= ""
  sumx = ""
  dashline = ""

  for num in problems:
    num1 = num.split(" ")[0]
    operator = num.split(" ")[1]
    num2 = num.split(" ")[2]

    if (operator == "+"):
      answer = str(int(num1) + int(num2))
    elif (operator == "-"):
      answer = str(int(num1) - int(num2))
    
    length = max( len(num1), len(num2) ) + 2 # will be used for dashline
    topnum = str(num1).rjust(length)
    botnum = operator + str(num2).rjust((length -1))
    result = str(answer).rjust(length)
    line = ""
    for dash in range(length):
      line += "-"
    # last problem cant have spaces after
    if num != problems[-1]:
      firstnum += topnum + "    "
      secondnum += botnum + "    "
      dashline += line + "    "
      sumx += result + "    "
    else:
      firstnum += topnum
      secondnum += botnum
      dashline += line
      sumx += result

  if resultshow == True:
    arranged_problems = firstnum+"\n"+secondnum+"\n"+dashline+"\n"+sumx
  else:
    arranged_problems = firstnum+"\n"+secondnum+"\n"+dashline
    
  return arranged_problems

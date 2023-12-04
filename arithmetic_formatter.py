def arithmetic_arranger(problems, display=None):
  # checking number of problmes
  if len(problems) > 5:
    return "Error: Too many problems."
  #defining a dic for storing data
  arranged_problems = {"line1": "", "line2": "", "line3": "", "line4": ""}

  #looping through problmes
  for problem in problems:

    #checking for valid operator
    if '+' not in problem and "-" not in problem:
      return "Error: Operator must be '+' or '-'."

    #getting operator and digits
    operator = "+" if "+" in problem else "-"
    digits = problem.split("+" if "+" in problem else "-")
    #applying map function on digits list to remove empty spaces
    digit1,digit2 = map(str.strip,digits)

    # checking length of each digit
    if len(digit1) > 4 or len(digit2) > 4:
      return "Error: Numbers cannot be more than four digits."

    #calculate digits
    addition = str(int(digit1) + int(digit2)) if operator == "+" else  str(int(digit1) - int(digit2))

    #geetting length of digits
    len1,len2,len3 = len(digit1), len(digit2),max(len(digit1),len(digit2))

    # defining each line data
    line1=f"{digit1:>{len3+2}}"
    line2=f"{operator} {digit2:>{len3}}"
    line3=(len3 + 2) * "-"
    line4= f"{addition:>{len3 + 2}}"
    
    # storing data in dic
    arranged_problems["line1"] += line1 + "    "
    arranged_problems["line2"] += line2 + "    "
    arranged_problems["line3"] += line3 + "    "
    # checking second parameter inorder to print the result
    if display:
      arranged_problems["line4"] += line4 + "    "
  #joining the values to return as single value
  result = "\n".join(arranged_problems.values())

  #returning result with removing right empty spaces of the vale
  return result.rstrip()

result = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "654 + 765",],True)
print(result)
  
  
   
    
   
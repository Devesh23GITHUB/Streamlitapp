def Current_User(string,delimiters):
  for delimiter in delimiters:
     string = " ".join(string.split(delimiter))

  result = string.split()
  result=result[0]

  return result

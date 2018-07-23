def RomanToInt(year):
 result = 0
  boom = []
for i in range(len(year)):
  for letter, value in values:
   if year[i] == letter:
     boom.append(value)
 boom.append(0)
  for i in range(len(year)):
  if boom[i] >= boom[i+1]:
    result = result + boom[i]
       else:
      result = result - boom[i]
    return result

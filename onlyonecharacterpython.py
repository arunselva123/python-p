def match(s1, s2):
 pos = -1
 for i, (c1, c2) in enumerate(zip(s1, s2)):
if c1 != c2:
  if pos != -1:
  return -1
 else:
  pos = i
  return pos

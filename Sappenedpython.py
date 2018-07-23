def truncate(s_tuples, max_length):
def stop_iterator(s_tuples):
tot_len = 0
for s,num in s_tuples:
  yield s
  tot_len += get_words_number(s
 if tot_len >= max_length:
   break
return ' '.join(stop_iterator(s_tuples))
print truncate(s_tuples,3)

import re
word_regex_pattern = re.compile("[^A-Za-z]+")
def camel(chars):
words = word_regex_pattern.split(chars)
return "".join(w.lower() if i is 0 else w.title() for i, w in enumerate(words))


x = "Happy birthday"
print(x)

# basic slice format: variable[start:end:step]

answer = x[::-1]
print(answer)

word = "Alexander the Great"
word[-1]
# 't'
print( word[word.index("Great")] )
# 'G'
print(word.index("Great") )
# 14
print(word[word.index("Alex"):word.index("the")])
# 'Alexander '
print(word[word.index("Alex"):word.index("eat")])
# 'Alexander the Gr'
print(word[ :word.index("the")])
# Alexander
print(word)
# 'Alexander the Great'
 

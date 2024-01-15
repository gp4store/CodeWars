# Gordon Ramsay shouts. He shouts and swears. There may be something wrong with him.
# Anyway, you will be given a string of four words. Your job is to turn them in to Gordon language.
# Rules:
# Obviously the words should be Caps, Every word should end with '!!!!'. 
# Any letter 'a' or 'A' should become '@', Any other vowel should become '*'.

def gordon(a):
    
    vowels = "EIOUeiou"
    just_a = "Aa"
    k = "*"
    l = "@"
  
    for char in vowels:
        a = a.replace(char, k)
        for ele in just_a:
            a = a.replace(ele, l)
            b = a.split()
    
    b = [item + "!!!"  for item in b]
    c = " ".join(b)

    return print(c.upper())



gordon("i am chef")
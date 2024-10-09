my_text = "hello, world"
my_text = my_text.upper()  # adding the upper allows there to be an overwrite to the original text
print (my_text)

my_text1 = "I have apple, you have an apple"
my_text1 = my_text1.replace("apple", "banana")
print (my_text1)


txt = "          i have an apple, you have an apple.         "
txt = txt.strip("   ")
print(txt)

txt1 = "python     java    C++"
txt1 = txt1.split("  ")
print (txt1)


txt2 = "bananas are greate scource of potassium"
txt2 = txt2.count("a")
print (txt2)
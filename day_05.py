# Day 05 with programming paglu 🎀 

# strings 
# strings are immutable - operations return new strings
name = "shiva"
print(name.upper())    
print(name.lower()) 
print(len(name))      
print(name[0])         
print(name[-1])       
print("hi" in name)     

translation = str.maketrans("aeiou", "12345")
"apple".translate(translation)  # '1ppl2'

"hello.world".partition(".")  # ('hello', '.', 'world')

"test.py".removesuffix(".py")  # 'test'
"Mr. Smith".removeprefix("Mr. ")  # 'Smith'


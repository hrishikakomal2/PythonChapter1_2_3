story = "hrishika is good .\n komal"
print(story)

# a = input("enter your name : ")
# b = "Good morning, "
# print( b + a)

letter = ''' dear <|Name|>
you r selected!!

Date: <|Date|>
'''
name = input("Enter your name : ")
date = input("Enter date : ")
letter = letter.replace("<|Name|>",name)
letter =letter.replace("<|Date|>",date)
print(letter)
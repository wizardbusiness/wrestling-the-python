# dot notation for string mods
f_name = "John".upper()
l_name = "Wick".upper()
age = "35"

# capitalize booleans
is_a_pacifist = False 

story = "The name's " + f_name + ". " + f_name + " " + l_name + "."


question = "Are you a pacifist?"
answer = "Yes" if is_a_pacifist else "They killed my dog. What kind of man doesn't avenge their dog."

print(story)
print(question)
print(answer)

escape_char_ex = "\" The backslash is escaped, and so you can\'t see it "

char_len_question = "You seem very linguistically savvy. But not savvy enough John Wick. Tell me how many characters are in your previous answer, or you DIE."
print(char_len_question)

story_char_len = len(story)
answer_story_char_len = "There are " + str(story_char_len) + " characters in my previous answer. Your move."
print(answer_story_char_len)

more_expo = "Oh, but John. you said " + "'" + str(story_char_len) + "'...  But you forgot that sometimes the most insignificant detail can be the most signficant."
print(more_expo)
blah_blah = "..."
print(blah_blah)
bbb = "You forgot about zero based indexing john. The correct answer? It's" + " " + str(story_char_len - 1) + "."
print(bbb)

# remainder using modulus
print("whaaa")
# remainder of dividing 10 by 3 is 1
modulus_10_3 = 10 % 3

print(modulus_10_3)



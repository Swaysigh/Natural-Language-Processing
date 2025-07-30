#Q2. Convert text into tokens and print the tokens in the sentence.

sentence_1 = "Hello, my name is Swayam Singh. I am a student at the CSVTU and I love programming and exploring new technologies."
sentence_2 = "myself Swayam Singh, a student at CSVTU, loves programming and exploring new technologies."

tokens = sentence_1.split()
list = [char for char in sentence_2]

print("Tokens in the sentence:", tokens)
print("Another token:", list)  
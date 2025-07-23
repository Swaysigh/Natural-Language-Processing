Q1.  To design and implement a nlp based system that automatically detect and translate hindi natural language text within source into english language.....


import googletrans 
from googletrans import Translator

# Initialize translator
translator = Translator()

# Enter the text to be translated
Input_text = input("Enter the Text to be translated: \n")

# Translate Hindi to English
Translated_text = translator.translate(Input_text, src= "hi", dest= "en")

# Print the translated text
print("Translated Text: \n", Translated_text.text)

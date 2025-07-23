Q1.  To design and implement a nlp based system that automatically detect and translate hindi natural language text within source into english language.....

    
import re
from googletrans import Translator

# Initialize translator
translator = Translator()

# Detect if text is in Hindi (Devanagari)
def is_hindi(text):
    return bool(re.search('[\u0900-\u097F]', text))

# Translate Hindi to English
def translate_text(text):
    try:
        translated = translator.translate(text, src="hi", dest="en")
        return translated.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text

# Main function to translate Hindi in comments and print statements
def translate_hindi_program(program_text):
    # Translate comments
    def replace_comment(match):
        comment = match.group(0)
        hindi_part = comment.lstrip('#').strip()
        if is_hindi(hindi_part):
            translated = translate_text(hindi_part)
            return "# " + translated
        return comment

    program_text = re.sub(r'#.*', replace_comment, program_text)

    # Translate print statements
    def replace_print(match):
        quote = match.group(1)
        content = match.group(2)
        if is_hindi(content):
            translated = translate_text(content)
            return f'print({quote}{translated}{quote})'
        return match.group(0)

    program_text = re.sub(r'print\((["\'])(.*?)\1\)', replace_print, program_text)

    return program_text

code = '''
# यह एक उदाहरण है
print("नमस्ते दुनिया")
x = 5  # मान सेट करें
print("Value is", x)
'''
translated_code = translate_hindi_program(code)
print(translated_code)

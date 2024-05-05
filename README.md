
Simple DeepL Translator

This Python script uses the DeepL API to translate text between different languages. The script provides a graphical user interface (GUI) for users to input text, select the target language, and select the source language for translation.

Usage:
Prior to exectuting, ensure the relevant dependencies are installed. Also required is a DeepL account is together with a DeepL API key. The key can be copied into a .txt file which is kept in the same location as the .py file. The name of the file must be entered into the 'with open("<filename>.txt", "r") as file:' line of the script. 

Run the script using python main.py. The GUI will open, allowing you to input text and select the target and source languages for translation. Currently, there are 26 languages available, additional two-letter language codes (as per the DeepL list - https://developers.deepl.com/docs/resources/supported-languages) may be added. 

To translate, input the text you want to translate into the text box.
Select the target language from the first dropdown box.
Select the source language from the second dropdown box.
Click the "Translate" button to see the translated text in the output box.

Dependencies:
Python 3.x
deepl Python package (for DeepL API interaction)
wx Python package (for GUI creation)

Author
Tim 
GitHub: Correlian
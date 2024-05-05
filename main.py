import deepl

import wx

import logging


logging.basicConfig(level=logging.DEBUG)

# Map language codes to their corresponding full names (taken from https://developers.deepl.com/docs/resources/supported-languages)
LANG_CODES = {
    "EN": "English",
    "DE": "German",
    "FR": "French",
    "ES": "Spanish",
    "SV": "Swedish",
    "ID": "Indonesian",
    "IT": "Italian",
    "PT-BR": "Portuguese (Brazilian)",
    "PT-PT": "Portuguese (Non-Brazilian",
    "RO": "Romanian",
    "SK": "Slovak",
    "TR": "Turkish",
    "RU": "Russian",
    "JA": "Japanese",
    "NL": "Dutch",
    "HU": "Hungarian",
    "ET": "Estonian",
    "PL": "Polish",
    "NB": "Norwegian (Bokmål)",
    "FI": "Finnish",
    "KO": "Korean",
    "CS": "Czech",
    "BG": "Bulgarian",
    "DA": "Danish",
    "LV": "Latvian",
    "LT": "Lithuanian"

}

# Load and read the API key saved into a .txt file in the same location as the .py file
def load_api_key():
    with open("<filename>.txt", "r") as file:
        return file.readline().strip()


# Translates the given text from the 'source_lang' to the 'target_lang' using the DeepL API and returns the translated text.
def translate_text(text, target_lang, source_lang):
    api_key = load_api_key()
    translator = deepl.Translator(api_key)
    try:
        # Map the language codes to full names
        source_lang_full = LANG_CODES.get(source_lang.upper())
        target_lang_full = LANG_CODES.get(target_lang.upper())
        if not source_lang_full or not target_lang_full:
            return "Invalid language code"

        result = translator.translate_text(text, target_lang=target_lang, source_lang=source_lang)
        return result
    except deepl.DeepLException as e:
        return str(e)


# Creates the wxPython application, GUI frame, and dropdown boxes.
def main():
    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "Tim's Translator: Choose a target language (box 1) and then a source language (box 2)")
    panel = wx.Panel(frame, wx.ID_ANY)

    input_text = wx.TextCtrl(panel, wx.ID_ANY, style=wx.TE_MULTILINE)

    # Drop-down menu for target language selection
    target_lang_choices = list(LANG_CODES.values())
    target_lang_choice = wx.Choice(panel, wx.ID_ANY, choices=target_lang_choices)
    target_lang_choice.SetSelection(0)  # Set the default selection



    # Drop-down menu for source language selection
    source_lang_choices = list(LANG_CODES.values())
    source_lang_choice = wx.Choice(panel, wx.ID_ANY, choices=source_lang_choices)
    source_lang_choice.SetSelection(0)  # Set the default selection



    result_text = wx.TextCtrl(panel, wx.ID_ANY, style=wx.TE_MULTILINE | wx.TE_READONLY)

# Handle the translation process when the "Translate" button is clicked. It gets the input text, target language, and source language, and calls 'translate_text'
    def on_translate(event):
        text = input_text.GetValue()
        target = list(LANG_CODES.keys())[target_lang_choice.GetSelection()]
        source = list(LANG_CODES.keys())[source_lang_choice.GetSelection()]
        result = translate_text(text, target, source)
        logging.debug("Translation result: %s", result)
        if not isinstance(result, str):
            result = str(result)
        result_text.SetValue(result)
        result_text.Refresh()

    translate_button = wx.Button(panel, wx.ID_ANY, "Translate")
    translate_button.Bind(wx.EVT_BUTTON, on_translate)

    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(input_text, 1, wx.EXPAND | wx.ALL, 5)
    sizer.Add(target_lang_choice, 0, wx.EXPAND | wx.ALL, 5)
    sizer.Add(source_lang_choice, 0, wx.EXPAND | wx.ALL, 5)
    sizer.Add(translate_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)
    sizer.Add(result_text, 1, wx.EXPAND | wx.ALL, 5)

    panel.SetSizer(sizer)
    frame.SetSize(650, 500)
    frame.Show(True)
    app.MainLoop()


# Checks if the script is being run directly and calls the function to start the GUI application
if __name__ == "__main__":
    main()

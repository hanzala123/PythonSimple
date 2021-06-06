import webbrowser
from googletrans import Translator
lang = "en"
translator = Translator()
# ... construct your list of search terms ...

while True:
    try:
        a = input('> ')
        url = "https://www.google.com.tr/search?q={}".format(a.replace(' ', '+'))
        url1 = "https://www.google.com.tr/search?q={}".format(translator.translate(a).text.replace(' ', '+'))
        webbrowser.open_new_tab(url)
        webbrowser.open_new_tab(url1)
    except  KeyboardInterrupt:
        break

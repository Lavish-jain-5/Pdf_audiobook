import pyttsx3
import PyPDF2

converter = pyttsx3.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# Use female voice
converter.setProperty('voice', voice_id)


book = open('op.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)

pages = pdf_reader.numPages
print(pages)

for i in range(8,pages):
    page = pdf_reader.getPage(i)
    text = page.extractText()
    converter.say(text)
    converter.runAndWait()

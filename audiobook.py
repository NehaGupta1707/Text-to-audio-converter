import pyttsx3
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('Quant 2022 handout.pdf', 'rb'))
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(1, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

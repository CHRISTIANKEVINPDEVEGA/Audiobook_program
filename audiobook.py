import pyttsx3
import PyPDF2

pdf_book = open("Overlord_Vol1.pdf")
pdf_reader=PyPDF2.PdfFileReader("Overlord_Vol1.pdf")
content_pages=pdf_reader.numPages
print(content_pages)

Auto_reader = pyttsx3.init()
Auto_reader.say("Hello, Everyone!")
Auto_reader.runAndWait() 
print("Audio book")
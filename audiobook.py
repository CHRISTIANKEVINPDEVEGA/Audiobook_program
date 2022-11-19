import pyttsx3
import PyPDF2

print("Welcome to the Audio book program")

pdf_book = open("Overlord_Vol1.pdf")
pdf_reader=PyPDF2.PdfFileReader("Overlord_Vol1.pdf")
content_pages=pdf_reader.numPages
print(f"Number of Pages of the pdf book: {content_pages}")

Auto_reader = pyttsx3.init()
pdf_page=pdf_reader.getPage(10)
text_page=pdf_page.extractText()
Auto_reader.say(text_page)
Auto_reader.runAndWait() 

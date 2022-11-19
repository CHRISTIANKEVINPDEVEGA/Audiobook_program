import pyttsx3
import PyPDF2

print("Welcome to the Audio book program")

book_name=input("Enter the pdf file you want to use: ")
pdf_book = open(book_name)
pdf_reader=PyPDF2.PdfFileReader("Overlord_Vol1.pdf")
content_pages=pdf_reader.numPages
print(f"Number of Pages of the pdf book: {content_pages}")
print("Enter the range of pages you want to be read")
user_input=int(input("From page: "))
user_input2=int(input("Until page(but not included): "))

for each_page in range(user_input, user_input2):
    Auto_reader = pyttsx3.init()
    pdf_page=pdf_reader.getPage(each_page)
    text_page=pdf_page.extractText()
    Auto_reader.say(text_page)
    Auto_reader.runAndWait() 

import PyPDF2
import os
from EmailScraper import get_email


def delete_file():
    fil = "./pdfs"
    files_path = [x for x in os.listdir(fil)]
    for f in files_path:
        os.remove(os.path.join(fil, f))


def extract_from_pdf():
    email_regex = r"[\w\.-]+@[\w\.-]+"
    fil = "./pdfs"
    files_path = [x for x in os.listdir(fil)]
    print(files_path)
    email = []
    for i in files_path:
        # creating a pdf file object
        pdfFileObj = open(fil + "/" + i, 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # printing number of pages in pdf file
        for j in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(j)

            # extracting text from page
            text = pageObj.extractText()
            elist = get_email(email_regex, text)
            if len(elist) > 0:
                for i in elist:
                    email.append(i)

        # closing the pdf file object
        pdfFileObj.close()
    return email


if __name__ == "__main__":
    emails = extract_from_pdf()
    print(emails)
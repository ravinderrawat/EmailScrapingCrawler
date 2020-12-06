from time import sleep

from EmailScraper import *
# import requests
from bs4 import BeautifulSoup
import tldextract
from pdfDataExtractor import extract_from_pdf


def link_crawler():

    url = input("Enter url : ")
    info = tldextract.extract(url)
    domain = info.domain

    if not os.path.exists('pdfs'):
        os.makedirs('pdfs')

    urls = [url]
    data = create_conn(url)
    soup = BeautifulSoup(data, "html.parser")
    links = [a.attrs.get('href') for a in soup.select('a[href]')]

    for link in links:
        if not link.startswith('http'):
            link = url.split('//')[0] + '//' + domain + "." + info.suffix + link
            urls.append(link)
        if domain in link and link not in urls:
            urls.append(link)

    with open('email_list.csv', 'w+', newline='') as file:
        file.write("")

    count = 0
    while count < len(urls) and count<200 :
        try:
            lin = urls[count]
            print("Crawling : ", lin)
            if count > 0:
                response = create_conn(lin)  # request.get(
                soup = BeautifulSoup(response, 'html.parser')
                links = [a.attrs.get('href') for a in soup.select('a[href]')]

                for link in links:
                    if not link.startswith('http'):
                        if link.startswith("?") and "?" not in lin:
                            link = lin + "/" + link
                        else:
                            link = url.split('//')[0] + '//' + domain + "." + info.suffix + link
                    if domain in link:
                        if link in urls:
                            pass
                        else:
                            urls.append(link)

                email = email_extractor(lin)
                write_in_csv(email)
            else:
                email = email_extractor(lin)
                write_in_csv(email)

        except Exception as e:
            print(e)

        finally:
            print("link no. : ", count)
            print(len(urls))
            count = count + 1

    sleep(20)

    email = extract_from_pdf()
    write_in_csv(email)

    print("......Completed")
    print("Removing Duplicates.....")
    remove_duplicates()

    driver.close()


#link_crawler()

# reading birla website completely

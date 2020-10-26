from EmailScraper import *
import requests
from bs4 import BeautifulSoup
import tldextract


def link_crawler():
    keywords = ('home', 'index', 'director', 'vice', 'placement', 'chancellor', 'vc', 'contact', 'about',
                'staff', 'ofc', 'faculty', 'member', 'ovc')

    crawled_url = set()

    url = input("Enter url : ")
    info = tldextract.extract(url)
    domain = info.domain

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
    while count < len(urls):
        try:
            lin = urls[count]
            print("Crawling : ", lin)
            if count > 0:
                for i in keywords:
                    if i in lin:
                        response = create_conn(lin)  # request.get(
                        soup = BeautifulSoup(response, 'html.parser')
                        links = [a.attrs.get('href') for a in soup.select('a[href]')]

                        for link in links:
                            if not link.startswith('http'):
                                link = url.split('//')[0] + '//' + domain + "." + info.suffix + link
                            if domain in link and link not in urls:
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

    print("......Completed")
    print("Removing Duplicates.....")
    remove_duplicates()

    driver.close()

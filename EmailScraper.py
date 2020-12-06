import re
from selenium import webdriver
import os
import csv
import platform
from headers import *


# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the

system = ""
if platform.system() == "Windows":
    system = "\\chromedriver.exe"
if platform.system() == "Linux" or platform.system() == "Darwin":
    system = "\\chromedriver"

print(platform.system())

chrome_driver = os.getcwd() + system
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), options=chrome_options)


def create_conn(urls):
    driver.get(urls)
    data = driver.page_source
    return data


def get_email(regex, text):
    emails = []
    em = re.findall(regex, text)
    for i in em:
        emails.append([i])
    return emails


def email_extractor(url):
    conn = create_conn(url)
    email = get_email(email_regex, conn)
    return email


def write_in_csv(row_list):
    print("Writing Data ..... ")
    with open('email_list.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)


def remove_duplicates():
    lines_seen = set()  # holds lines already seen
    outfile = open("emails.csv", "w")
    for line in open("email_list.csv", "r"):
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

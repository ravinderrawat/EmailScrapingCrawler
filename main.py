import LinkCrawler
import scrap_from_all
import  EmailScraper

if __name__ == "__main__":
    try:
        print(" press 1 for selected type of links of website\n press 2 for all links of a website\n press 3 for exit\n")
        ch = input("Enter Choice : ")
        if ch == "1":
            LinkCrawler.link_crawler()
        elif ch == "2":
            scrap_from_all.link_crawler()
        elif ch == "3":
            SystemExit
        else:
            print("Wrong input")
    except (KeyboardInterrupt, SystemExit):
        EmailScraper.remove_duplicates()
        print("Terminated......")
        raise

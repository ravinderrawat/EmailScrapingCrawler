from selenium.webdriver.chrome.options import Options
import os

email_regex = r"[\w\.-]+@[\w\.-]+"
download_dir = os.getcwd()+"\\pdfs"  # for linux/*nix, download_dir="/usr/Public"
profile = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    }

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--enable-javascript")
chrome_options.add_argument("--window-size=1360x720")
chrome_options.add_experimental_option("prefs", profile)

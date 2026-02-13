import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# wrote these functions with the help of AI, it checks if any of common browsers are installed
def is_chrome_installed() -> bool:
    names = ["google-chrome", "chrome", "chromium", "chromium-browser"]
    return any(shutil.which(name) for name in names)

def is_firefox_installed() -> bool:
    names = ["firefox", "firefox-developer-edition", "firefox-nightly"]
    return any(shutil.which(name) for name in names)

def is_edge_installed() -> bool:
    names = ["microsoft-edge", "edge", "microsoft-edge-dev", "microsoft-edge-beta", "microsoft-edge-canary"]
    return any(shutil.which(name) for name in names)


# Check for installed browsers and set up the WebDriver accordingly, with fallback to mirror URLs for ChromeDriver if installation fails

chrome_mirrors = [
    "https://registry.npmmirror.com/-/binary/chromedriver", 
    "https://npmmirror.com/mirrors/chromedriver",
    "https://cdn.npmmirror.com/binaries/chromedriver",
    "https://registry.npmmirror.com/-/binary/chrome-for-testing", 
]

driver = None
if is_chrome_installed():
    for mirror_url in chrome_mirrors:
        # install the driver via the default method first, if it fails, try the mirror urls
        try:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            break  # Stop on first success
        except Exception:
            service = ChromeService(ChromeDriverManager(url=mirror_url).install())
            driver = webdriver.Chrome(service=service)
            break 
        except Exception:
            continue  # Try the next mirror if this one fails

driver.get("https://www.google.com")
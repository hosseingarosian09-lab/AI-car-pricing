import shutil
  
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

def is_opera_installed() -> bool:
    names = ["opera", "opera-browser", "opera-developer", "opera-beta", "opera-nightly"]
    return any(shutil.which(name) for name in names)
from selenium import webdriver

# Download appropriate Geckodriver version from https://github.com/mozilla/geckodriver/releases

#driver = webdriver.Firefox(executable_path="/home/daniel/git/ba-thesis-resources/scripts/geckodriver-v0.24.0-linux64/geckodriver")
driver = webdriver.Firefox(executable_path="/home/daniel/git/ba-thesis-resources/scripts/geckodriver-v0.24.0-linux64/geckodriver", firefox_binary="/home/daniel/firefox70.0/firefox")
driver.get("http://localhost:8000")

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys

if len(sys.argv) == 4:
    pin = sys.argv[1]
    name = sys.argv[2]
    num = sys.argv[3]
else:
    pin = int(input("Game PIN: "))
    name = input("Name: ")
    num = int(input("# of Bots: "))

def newGame(x):
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Firefox(firefox_options=options)

    browser.get("https://kahoot.it")

    try:
        gamePin = browser.find_element_by_id("game-input")
        gamePin.send_keys(pin)

        enter = browser.find_element_by_tag_name("button")
        enter.click()
    except:
        print("Could not find game")

    try:
        gameName = browser.find_element_by_id("nickname")
        gameName.send_keys("uni" + str(x))

        enter = browser.find_element_by_tag_name("button")
        enter.click()
    except:
        print("Could not set name")

def main():
    for i in range(num):
        newGame(i)

if __name__ == "__main__":
    main()
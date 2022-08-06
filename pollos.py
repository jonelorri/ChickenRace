from fileinput import close
from bs4 import BeautifulSoup
import time
import datetime
import telebot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

TOKEN = "<<---- YOUR TOKEN ----->>"
chat_id = "<<--- YOUR CHAT ID ---->>"
bot = telebot.TeleBot(TOKEN)

chrome_options = ChromeOptions()
chrome_options.add_extension('<< PATH TO YOUR MetaMask.crx FILE >>')

driver = webdriver.Chrome('<< PATH TO YOUR Chromedriver FILE >>', options=chrome_options)

nothingNumber = 1


def entrando(number):

    # OPEN TOOGLE
    try:
        boton6 = driver.find_element_by_xpath(f"/html/body/div/div[3]/div/div/div[2]/div/table/tbody/tr[{number + 1}]").click()
        time.sleep(1)
        boton_enter = driver.find_element_by_xpath(f"/html/body/div/div[3]/div/div/div[2]/div/table/tbody/tr[{number + 2}]/td/div/div/div/div/div/div").click()
        time.sleep(1)
    except:
        boton6 = driver.find_element_by_xpath(f"/html/body/div/div[2]/div/div/div[2]/div/table/tbody/tr[{number + 1}]").click()
        time.sleep(1)
        boton_enter = driver.find_element_by_xpath(f"/html/body/div/div[2]/div/div/div[2]/div/table/tbody/tr[{number + 2}]/td/div/div/div/div/div/div").click()
        time.sleep(1)


    # SELECT THE CHICKEN
    try:
        seleccionar_pollo = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/table/tbody/tr[2]/td[9]/a").click()
        time.sleep(1)
        confirmar_pollo = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/button[2]").click()
        time.sleep(5)
    except:
        cerrar_ventana = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/button").click()
        time.sleep(2)

    # CLOSE WINDOW
    try:
        cerrar_ventana = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/button").click()
        time.sleep(2)
    except:
        nothingNumber = 2

    # CLOSE TOOGLE
    try:
        boton6 = driver.find_element_by_xpath(f"/html/body/div/div[3]/div/div/div[2]/div/table/tbody/tr[{number + 1}]").click()
    except:
        nothingNumber = 1

    try:
        boton6 = driver.find_element_by_xpath(f"/html/body/div/div[2]/div/div/div[2]/div/table/tbody/tr[{number + 1}]").click()
    except:
        nothingNumber = 1


intentos = 1

while (1):
    try:
        if (intentos == 1):
            driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase')
            time.sleep(1)
            frase = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/form/div[4]/div[1]/div/input").send_keys("<<--- YOUR SEED PHRASE HERE ---->>")
            frase2 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/form/div[5]/div/input").send_keys("Borracho4.0")
            frase3 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/form/div[6]/div/input").send_keys("Borracho4.0")
            time.sleep(1)
            boton1 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/form/div[7]/div").click()
            time.sleep(1)
            boton2 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/form/button").click()
            time.sleep(2)
            boton3 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/button").click()
            time.sleep(1)

            driver.get('https://dev.chickenderby.com/races/enter')
            time.sleep(30)

            # LOGIN
            login = driver.find_element_by_xpath("/html/body/div[1]/nav/div/div/ul/li[5]/a").click()
            time.sleep(2)
            driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#connect/cJ6iHsfNuYxEhEkw_3RyC')
            time.sleep(2)
            siguiente = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div[2]/button[2]").click()
            time.sleep(2)
            conectar = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]").click()
            time.sleep(3)

            driver.get('https://dev.chickenderby.com/races/enter')
            time.sleep(5)

            login2 = driver.find_element_by_xpath("/html/body/div[1]/nav/div/div/ul/li[5]/a").click()
            time.sleep(2)
            metamaskClick = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div").click()
            time.sleep(5)

        driver.get('https://dev.chickenderby.com/races/enter')
        time.sleep(5)

        try:
            login = driver.find_element_by_xpath("/html/body/div[1]/nav/div/div/ul/li[5]/a").click()
            time.sleep(4)
        except:
            print("Error")

        # FILTERS
        try:
            boton_filter = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/div[1]/div[1]/div[2]/button[2]").click()
            time.sleep(2)
            filtros = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[1]/div[4]/div/input").send_keys("0.01")
            boton5 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/button[2]").click()
            time.sleep(2)
        except:
            boton_filter = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[1]/div[1]/div[2]/button[2]").click()
            time.sleep(2)
            filtros = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[1]/div[4]/div/input").send_keys("0.01")
            boton5 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/button[2]").click()
            time.sleep(2)

        while(1):
            e = datetime.datetime.now()
            if e.hour >= 0:
                try:
                    refresh = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[1]/div[1]/div[2]/button[1]").click()
                except:
                    refresh = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/div[1]/div[1]/div[2]/button[1]").click()
                time.sleep(1)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                entry = soup.find_all('span', class_='price-green')
                time.sleep(1)

                elements_entry = list()
                
                i = 1
                while(i < len(entry)):
                    word = entry[i].text
                    newWord = word[1:]
                    elements_entry.append(float(newWord))
                    i += 2

                i = 0

                if(len(elements_entry) != 0):
                    while(i < len(elements_entry)):
                        if(elements_entry[i] >= 0):
                            entrando(i)
                            time.sleep(3)
                        i += 1
                time.sleep(10)
            else:
                print('Out of time - Sleeping Zzzzz')  # This is made to simulate a real human been playing. We can't play 24/7
                time.sleep(1800)
    except:
        intentos = 2
        bot.send_message(chat_id, "Error")

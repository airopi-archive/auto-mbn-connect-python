from selenium import webdriver
import os
import sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('info.txt', 'r') as f:
    lines = f.read().split()
    name = lines[0].split('=')[1]
    mdp = lines[1].split('=')[1]

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

driver = webdriver.Chrome(resource_path('./chromedriver.exe'))
driver.get(r"https://monbureaunumerique.fr") # on va sur MBN
driver.find_element_by_xpath(r"/html/body/div/div/div/div[2]/a[2]").click() # on clique sur connexion
driver.find_element_by_xpath(r"/html/body/main/div/div/div[1]/div/div/form/fieldset[1]/legend/button").click() # on clique sur élève
driver.find_element_by_xpath(r"/html/body/main/div/div/div[1]/div/div/form/fieldset[1]/ul/li[3]/div/label").click() # on clique sur Strasbourg
driver.find_element_by_xpath(r'//*[@id="button-submit"]').click() # on valide
driver.find_element_by_xpath(r'//*[@id="user"]').send_keys(name) # on met l'identifiant
driver.find_element_by_xpath(r'//*[@id="password"]').send_keys(mdp) # on met le mdb
driver.find_element_by_xpath(r'//*[@id="bouton_connexion"]').click() # on clique sur connection
driver.find_element_by_xpath(r'/html/body/div[1]/div[2]/button').click() # on clique sur protail
driver.find_element_by_xpath(r'/html/body/div[1]/div[2]/div/ul/li[1]/a').click() # on clique sur Couffignal

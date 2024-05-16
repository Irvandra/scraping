from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

USERNAME_SINTA = os.getenv("USERNAME_SINTA")
PASSWORD_SINTA = os.getenv("PASSWORD_SINTA")

driver = webdriver.Chrome()

driver.get("https://sinta.kemdikbud.go.id/logins")

username = driver.find_element(By.NAME, "username")
username.send_keys(USERNAME_SINTA)

password = driver.find_element(By.NAME, "password")
password.send_keys(PASSWORD_SINTA)

submit = driver.find_element(By.XPATH, "//button[@type='submit']")
submit.click()

driver.implicitly_wait(30)

title = []
pub = []
year = []

for page in range(1, 11):
    driver.get("https://sinta.kemdikbud.go.id/affiliations/profile/384?page=" + str(page) + "&view=scopus")
    articles = driver.find_elements(By.CLASS_NAME, "ar-list-item")

    for article in articles:
        title.append(article.find_element(By.CLASS_NAME, "ar-title").text)
        pub.append(article.find_element(By.CLASS_NAME, "ar-pub").text)
        year.append(article.find_element(By.CLASS_NAME, "ar-year").text)

df = pd.DataFrame(data={'title': title, 'pub': pub, 'year': year})
df.to_excel("output/data.xlsx")
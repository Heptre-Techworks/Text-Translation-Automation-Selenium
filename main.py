from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver= webdriver.Chrome(ChromeDriverManager().install())
lines=[]
with open("patient.txt","r",encoding="utf-8") as fp:
    lines=fp.readlines()

with open("patient_translater.txt","w",encoding="utf-8") as fp:pass

search_url="https://translate.google.co.in/?sl=en&tl=hi&text={q}&op=translate"
for line in lines:
    line=line.strip()
    line=line.replace("</string>","")
    line= line.split(">")
    print(line[0],line[1])

    driver.get(search_url.format(q=line[1]))
    time.sleep(2)
    for elements in driver.find_elements_by_xpath('//span[@jsname="W297wb"]'):
        print(line[0]+">"+elements.text+"</string>")
        with open("patient_translater.txt", "a",encoding="utf-8") as fp:
            fp.writelines((line[0]+">"+elements.text+"</string>\n"))
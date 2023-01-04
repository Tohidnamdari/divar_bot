from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
input1=input("احتیاج به کدام شهر داری؟")#We get city input from the user
if input1=="saveh":#If Saveh entered
    driver.get("https://divar.ir/s/saveh/buy-apartment?q=%D8%A7%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86")#Enter the wall of Saveh
    print(driver.title)
    all=driver.find_elements_by_xpath('/html/body/div/div[1]/main/div[2]/div')
    for i in all:
        locition=driver.find_elements_by_xpath('//h2[@class="kt-post-card__title"]')#Find the location
        mony=driver.find_elements_by_xpath('/html/body/div/div[1]/main/div[2]/div/div/div[1]/a/article/div[1]/div[1]')#find the mony
        # print(locition)
        print(mony)
if input1=="tehran":#If tehran entered
    driver.get("https://divar.ir/s/tehran/buy-apartment?q=%D8%A7%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86")
    locition2=driver.find_element_by_xpath('//*[@id="app"]/div[1]/main/div[2]/div/div/div[1]/a/article/div[1]/h2')
    mony2=driver.find_element_by_xpath('//*[@id="app"]/div[1]/main/div[2]/div/div/div[1]/a/article/div[1]/div[1]')
    print("locitin:",locition2.text)
    print("mony:",mony2.text)

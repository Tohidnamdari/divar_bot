from flask import Flask,render_template,request,redirect
from selenium import webdriver
from time import sleep
from database import db
import sys
import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
db.create_all()
from database import home
from database import app

lk=[]
lol1=[]
lol2=[]
lol3=[]
first_names=[]
n=[]
pages_banck=[]
pages_banck1=[]
pages_banck2=[]
pages_banck3=[]
pages_banck4=[]
cl=[]
Number_ph=0
js=[]
# @app.route('/chart',methods=['GET','POST'])
# def chart():
#     x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
#     y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
#     plt.title("Sports Watch Data", loc='left')
#     plt.xlabel("Average Pulse")
#     plt.ylabel("Calorie Burnage")
#
#     plt.plot(x, y)
#     plt.show()
#     return render_template('chart.html')

@app.route('/sort_all',methods=['GET','POST'])
def sort_all():
    for iii in range(len(home.query.all())):
        x = home.query.all()[iii].allmony
        zz = x.split(" ")
        print(zz[0])
        aa = zz[0].split("٬")
        print(aa)
        tt = ""
        for ie in range(len(aa)):
            tt += aa[ie]
        print(int(tt))
        h = home.query.all()[iii]
        h.all_int = tt
        db.session.commit()

    l = home.query.order_by(home.all_int).all()
    for pa in l:
        print(pa)

    return render_template('sortall.html',items=len(home.query.all()),pages_banck1=l)
@app.route('/sort',methods=['GET','POST'])
def sort():
    for ii in range(len(home.query.all())):
        b = home.query.all()[ii].mony
        z = b.split(" ")
        print(z[0])
        a = z[0].split("٬")
        print(a)
        t = ""
        for e in range(len(a)):
            t += a[e]
        print(int(t))
        hm = home.query.all()[ii]
        hm.mony_int = t
        db.session.commit()

    list = home.query.order_by(home.mony_int).all()
    for pa in list:
        print(pa)

    return render_template('sort.html',items=len(home.query.all()),pages_banck1=list)
@app.route('/result',methods=['GET','POST'])
def result():
    return render_template('result.html',pages_banck1=home.query.all(),items=len(home.query.all()))
@app.route('/',methods=['GET','POST'])
def city():
    global Number_ph

    if request.method == 'POST':
        driver = webdriver.Chrome('./chromedriver.exe')
        metr1 = request.form.get('metr')
        metr2 = request.form.get('metr1')
        mony1= request.form.get('mony1')
        mony2= request.form.get('mony2')
        city = request.form.get('city')
        driver.get("https://divar.ir/s/saveh/buy-apartment?price="+mony1+"-"+mony2+"&"+"size="+metr1+"-"+metr2)
        #login=driver.find_element_by_xpath('/html/body/div/div/header/nav/div/div[3]/div/button').click()
        #sleep(2)
        #login_w=driver.find_element_by_xpath('/html/body/div/div/header/nav/div/div[3]/div/div/div/button').click()
        #sleep(30)
        j = driver.find_elements_by_class_name("kt-post-card__title")  # تمام المنت ها رو باز توی متغیر میزیزیم تا روش کلیک بشه
        for i in range(len(j)):
            name=j[i].text

            j[i].click()
            print(driver.title)
            sleep(2)
            d = driver.find_elements_by_class_name("kt-unexpandable-row__value")
            if d[0]:
                metr=d[0].text


            if d[1]:
                allmony=d[1].text


            if d[2]:
               mony=d[2].text


            if d[3]:
               karbar=d[3].text



            sleep(2)
            s=driver.find_elements_by_class_name("kt-group-row-item__value")
            if s:
                tabage=s[0].text


                salsakht=s[1].text


                room=s[2].text


            sleep(3)

           # kk=driver.find_element_by_xpath('//*[@id="INERT-CONTAINER"]/div[1]/div/div/div[1]/div[2]/button[1]').click()
            #sleep(5)
            #if Number_ph < 1:
                #bn = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/footer/button[2]').click()
                #Number_ph = Number_ph + 1
            #sleep(5)
            #xk=driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[1]/div[3]/div[1]/div/div[2]/a')
            #sleep(3)
            #if xk:
                #lk.append(xk.text)
            #sleep(3)
            sleep(3)
            tabage = d[3].text

            salsakht = s[1].text

            room = s[2].text
            metr =s[0].text
            allmony = d[0].text
            mony = d[1].text
            karbar = d[2].text
            admin = home(name=name, metr=metr, allmony=allmony, mony=mony, karbar=karbar, tabage=tabage,
                         salsakht=salsakht, room=room)
            db.session.add(admin)
            db.session.commit()
            sleep(1)
            driver.back()

            j = driver.find_elements_by_class_name("kt-post-card__title")  # تمام المنت ها رو باز توی متغیر میزیزیم تا روش کلیک بشه
            sleep(1)

        return render_template('city.html')
    return render_template('city.html')

if __name__=='__main__':
    app.run()
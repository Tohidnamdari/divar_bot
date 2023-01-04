from flask import Flask,render_template,request,redirect,make_response
from selenium import webdriver
from time import sleep
from database import db
db.create_all()
from database import home,Users
from database import app


labels = [
]

values = [

]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]
@app.route('/chart',methods=['GET','POST'])
def chart():
    if request.cookies.get("user"):
        line_labels= home.query.all()
        line_values= home.query.all()
        return render_template('chart.html',user=request.cookies.get("user"), title='Bitcoin Monthly Price in USD', labels=line_labels, values=line_values)
    else:
        return redirect('/login')
@app.route("/logout")
def logout():
    response = make_response(redirect('/login'))
    response.delete_cookie("user")
    return response
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user = request.form.get('user')
        pas = request.form.get('pas')
        found=False
        for u in range(len(Users.query.all())):
            if user==Users.query.all()[u].username and pas==Users.query.all()[u].password:
                response=make_response(redirect('/'))
                response.set_cookie("user",user)
                found = True
                return response
        if found==False:
                return render_template('login.html',user=request.cookies.get("user"))
    return render_template('login.html',user=request.cookies.get("user"))
@app.route('/register',methods=['POST','GET'])
def Register():
    if request.method=='POST':
        user_name1 = request.form.get('user')
        password1 = request.form.get('pas')
        re_password = request.form.get('pass')
        if password1==re_password:
            admin1=Users(username=user_name1,password=password1)
            db.session.add(admin1)
            db.session.commit()
            return redirect('/add')
        else:
            return render_template('Register.html',user=request.cookies.get("user"))
    else:
        return render_template('Register.html',user=request.cookies.get("user"))

@app.route('/sort_all',methods=['GET','POST'])
def sort_all():
    if request.cookies.get("user"):
        for az in range(len(home.query.all())):
            x = home.query.all()[az].allmony
            zz = x.split(" ")
            print(zz[0])
            aa = zz[0].split("٬")
            print(aa)
            tt = ""
            for ie in range(len(aa)):
                tt += aa[ie]
            print(int(tt))
            h = home.query.all()[az]
            h.all_int = tt
            db.session.commit()

        l = home.query.order_by(home.all_int).all()
        for pa in l:
            print(pa)
            values.append(pa)
            labels.append(home.name)

        return render_template('sortall.html',user=request.cookies.get("user"),items=len(home.query.all()),pages_banck1=l)
    else:
        return redirect('/login')
@app.route('/sort',methods=['GET','POST'])
def sort():
    if request.cookies.get("user"):
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

        return render_template('sort.html',user=request.cookies.get("user"),items=len(home.query.all()),pages_banck1=list)
    else:
        return redirect('/login')
@app.route('/result',methods=['GET','POST'])
def result():
    if request.cookies.get("user"):
        return render_template('result.html',user=request.cookies.get("user"),pages_banck1=home.query.all(),items=len(home.query.all()))
    else:
        return redirect('/login')
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html',user=request.cookies.get("user"))
@app.route('/add',methods=['GET','POST'])
def city():
    global Number_ph
    if request.cookies.get("user"):
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

                return render_template('city.html',user=request.cookies.get("user"))
        return render_template('city.html',user=request.cookies.get("user"))
    else:
        return redirect('/login')
if __name__=='__main__':
    app.run()
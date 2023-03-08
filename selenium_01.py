from flask import Flask,render_template,request,redirect,make_response,flash
from selenium import webdriver
from time import sleep
from database import db
db.create_all()
from database import home,Users
from database import app

# @app.route('/chart',methods=['GET','POST'])
# def chart():
#     if request.cookies.get("user"):
#         line_labels= labels
#         line_values= values
#         return render_template('chart.html',user=request.cookies.get("user"), title='Bitcoin Monthly Price in USD', labels=line_labels, values=line_values)
#     else:
#         return redirect('/login')
@app.route('/Relationship',methods=['GET','POST'])
def Relationship():
        return render_template('Relationship.html',user=request.cookies.get("user"))
@app.route("/logout")
def logout():
    flash("کاربر خارج شد", "danger")
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
                flash("کاربر وارد شد", "success")
                response=make_response(redirect('/'))
                response.set_cookie("user",user)
                found = True
                return response
        if found==False:
                flash("نام کاربری یا رمز عبور اشتباه است", "danger")
                return render_template('login.html',user=request.cookies.get("user"))
    return render_template('login.html',user=request.cookies.get("user"))
@app.route('/register',methods=['POST','GET'])
def Register():
    if request.method=='POST':
        user_name1 = request.form.get('user')
        password1 = request.form.get('pas')
        re_password = request.form.get('pass')
        if password1==re_password and len(password1)==8:
            flash("کاربر ثبت نام شد", "success")
            admin1=Users(username=user_name1,password=password1)
            print(admin1)
            db.session.add(admin1)
            db.session.commit()

            return redirect('/add')
        else:
            flash("رمز عبور با تکرار ان همخوانی ندارد یا تعداد ارقام  رمز عبور کمتر از 8 میباشد ", "danger")

            return redirect('/register')
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
def ind():
    return render_template('ind.html',user=request.cookies.get("user"))
@app.route('/add',methods=['GET','POST'])
def add():
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
                title = driver.find_elements_by_class_name("kt-post-card__title")  # تمام المنت ها رو باز توی متغیر میزیزیم تا روش کلیک بشه
                for i in range(len(title)):
                    name=title[i].text

                    title[i].click()
                    print(driver.title)
                    sleep(2)
                    Information = driver.find_elements_by_class_name("kt-unexpandable-row__value")
                    if Information[0]:

                        metr=Information[0].text


                    if Information[1]:
                        allmony=Information[1].text


                    if Information[2]:
                       mony=Information[2].text


                    if Information[3]:
                       karbar=Information[3].text



                    sleep(2)
                    Information2=driver.find_elements_by_class_name("kt-group-row-item__value")
                    if Information2:
                        tabage=Information2[0].text


                        salsakht=Information2[1].text


                        room=Information2[2].text


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
                    if Information[3].text=="همکف":
                        tabage = Information[3].text
                    else:
                        e= Information[3].text.split("از")
                        tabage=e[0]
                    salsakht = Information2[1].text

                    room = Information2[2].text
                    metr =Information2[0].text
                    allmony = Information[0].text
                    mony = Information[1].text
                    karbar = Information[2].text
                    admin = home(name=name, metr=metr, allmony=allmony, mony=mony, karbar=karbar, tabage=tabage,
                                 salsakht=salsakht, room=room)
                    db.session.add(admin)
                    db.session.commit()
                    sleep(1)
                    driver.back()
                    title = driver.find_elements_by_class_name("kt-post-card__title")  # تمام المنت ها رو باز توی متغیر میزیزیم تا روش کلیک بشه
                    sleep(1)

                return render_template('city.html',user=request.cookies.get("user"))
        return render_template('city.html',user=request.cookies.get("user"))
    else:
        return redirect('/login')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error-404.html'), 404
if __name__=='__main__':
    app.run(host='0.0.0.0',port=80)
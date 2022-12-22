from database import db
db.create_all()
from database import home

for ii in range(len(home.query.all())):
    a = home.query.all()[ii].mony
    b = a.split(" ")
    print(b[0])
    c = b[0].split("٬")
    print(c)
    total = ""
    for i in range(len(c)):
        total += c[i]
    print(int(total))
    help = home.query.all()[ii]
    help.mony_int = total
    db.session.commit()

list=home.query.order_by(home.mony_int).all()
for ap in list:
    print(ap)


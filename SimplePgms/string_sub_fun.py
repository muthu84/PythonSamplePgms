import datetime

message = "Hi there {name}, thank you for purchase on {date}. we hope, you are excited to using it.Remider to purchase total as ${total}. Have a greate one.."

names = ['muthu','nithya','magathi','sharvan','velu','divya','samy']
amounts = [224,225.5,100,142.1,565,667,332]
new_msg = []

def make_msg(mynames,myaccts):
    today = datetime.date.today()
    print(today)
    text = '{today.year}/{today.month}/{today.day}'.format(today=today)
    i = 0
    if len(mynames) == len(myaccts):
        for name in mynames:
            acc = "%.1f" %(myaccts[i])
            my_n = name.capitalize()
            new_msg = message.format(name=my_n,date=text,total=acc)
            i+=1
            print(new_msg)
make_msg(names,amounts)

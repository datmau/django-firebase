from django.shortcuts import render
import pyrebase
from django.contrib import auth
config = {
    'apiKey': "AIzaSyCz4s8EKnHRN3XNM3FAXzOBj909uq6cago",
    'authDomain': "ddl-meeewa.firebaseapp.com",
    'databaseURL': "https://ddl-meeewa.firebaseio.com",
    'storageBucket': "ddl-meeewa.appspot.com",
    'serviceAccount': "/ddl-meeewa-firebase-adminsdk-wwrep-4c0fd07ace.json"
  }

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database=firebase.database()
def signIn(request):

    return render(request, "signin.html")

def postsign(request):  
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message="credenciales invalidas"
        return render(request,"signin.html",{"messg":message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request, "welcome.html",{"e":email})
def logout(request):
    auth.logout(request)
    return render(request,'signin.html')


def signUp(request):

    return render(request,"signup.html")
def postsignup(request):

    name=request.POST.get('name')
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw)
    except:
        message="Unable to create account try again"
        return render(request,"signup.html",{"messg":message})
    uid = user['localId']

    data={"name":name,"status":"1"}

    database.child("users").child(uid).child("details").set(data)
    return render(request,"signin.html")

def create(request):

    return render(request,'create.html')


def post_create(request):

    import time
    from datetime import datetime, timezone
    import pytz

    tz= pytz.timezone('America/Guayaquil')
    time_now= datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    print("mili"+str(millis))
    work = request.POST.get('work')
    progress =request.POST.get('progress')

    idtoken= request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    print("info"+str(a))
    data = {
        "work":work,
        'progress':progress
    }
    database.child('users').child(a).child('reports').child(millis).set(data)
    name = database.child('users').child(a).child('details').child('name').get().val()
    return render(request,'welcome.html', {'e':name})

def check(request):
    import datetime
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']

    timestamps = database.child('users').child(a).child('reports').shallow().get().val()
    lis_time=[]
    for i in timestamps:

        lis_time.append(i)

    lis_time.sort(reverse=True)

    print(lis_time)
    work = []

    for i in lis_time:

        wor=database.child('users').child(a).child('reports').child(i).child('work').get().val()
        work.append(wor)
    print(work)

    date=[]
    for i in lis_time:
        i = float(i)
        dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
        date.append(dat)

    print(date)

    comb_lis = zip(lis_time,date,work)
    name = database.child('users').child(a).child('details').child('name').get().val()

    return render(request,'check.html',{'comb_lis':comb_lis,'e':name})

def post_check(request):

    import datetime

    time = request.GET.get('z')

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']

    work =database.child('users').child(a).child('reports').child(time).child('work').get().val()
    progress =database.child('users').child(a).child('reports').child(time).child('progress').get().val()
    i = float(time)
    dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
    name = database.child('users').child(a).child('details').child('name').get().val()

    return render(request,'post_check.html',{'w':work,'p':progress,'d':dat,'e':name})

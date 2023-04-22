from django.core.files.storage import FileSystemStorage
from django.core.serializers import json
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
import datetime
# from engineio import json
from sklearn.ensemble import RandomForestClassifier


from diabetes_moule.models import *

# Create your views here.
def log(request):
    if request.method=="POST":
        u=request.POST['textfield']
        p=request.POST['textfield3']
        qry=login.objects.get(username=u,password=p)
        try:
            if qry.usertype == 'admin':
                return redirect('/home')
            elif qry.usertype=='doctor':
                request.session['lid']=qry.id
                return redirect('/dhome')
            else:
                return HttpResponse("usernotfound")
        except Exception as e:
            return HttpResponse("usernotfound")

    else:
        qry1=doctor.objects.filter(doctorid__usertype='doctor')
        # if qry1.exists():
            # qry1[0]=qry1
        return render(request,"login_index.html",{"data":qry1})


def complaint(requet):
    qry=complaints.objects.all()
    return render(requet,"admin_temp/COMPLAINT.html",{"data":qry})


def doctors(request):
    qry=doctor.objects.filter(doctorid__usertype='pending')
    return render(request,"admin_temp/DOCTOR.html",{"data":qry})


def home(request):
    return render(request,"admin_temp/index.html")


def approve_doctors(request,id):
    login.objects.filter(id=id).update(usertype='doctor')
    return HttpResponse('''<script>alert("Refistered");window.location="/doctor" </script>''')

def reject_doctors(request,id):
    login.objects.filter(id=id).delete()
    return  HttpResponse("Rejected")


def blockk(request,id):
    login.objects.filter(id=id).update(usertype='blocked')
    return HttpResponse("Blocked succesfully")

def unblock(request,id):
    doctor.objects.filter(id=id).update(usertype='doctor')
    return HttpResponse("Unblocked succesfully")


def approver(request):
    qry=doctor.objects.all()
    return render(request,"admin_temp/approveddr.html",{"data":qry})

def ratings(request):
    qry = rating.objects.all()
    return render(request,"admin_temp/RATING.html",{"data":qry})

def replys(request,id):
    if request.method=="POST":
        r=request.POST['textarea']
        date=datetime.datetime.now().strftime("%Y-%m-%d")
        print(date)
        complaints.objects.filter(id=id).update(reply=r,reply_date=str(date))
        return HttpResponse("Succesful")

    else:
        return render(request,"admin_temp/REPLY.html")

def users(request):
    qry=user.objects.all()
    return render(request,"admin_temp/USER.html",{"data":qry})


# ===========================DOCTOR MODULE===============================================

def registration(request):
    if request.method=="POST":

        name=request.POST['textfield']
        place=request.POST['textfield2']
        post = request.POST['textfield3']
        pin = request.POST['textfield4']
        category= request.POST['textfield5']
        qualification = request.POST['textfield6']
        phone_No = request.POST['textfield7']
        email= request.POST['textfield8']
        password = request.POST['textfield9']
        # confirmpassword= request.POST['textfield10']

        l=login()
        l.username=email
        l.password=password
        l.usertype='pending'
        l.save()
        print(l.id)

        d=doctor()
        d.doctorname=name
        d.doctorplace=place
        d.doctorpost=post
        d.doctorpin=pin
        d.email=email
        d.pho_no=phone_No
        d.qualification=qualification
        d.category=category
        d.doctorid=login.objects.get(id=l.id)
        d.save()
        return HttpResponse('''<script>alert("Refistered");window.location="/" </script>''')




    else:

        return render(request,"doctor_temp/REGISTRATION.html")



def view_profile(request):
    if request.method=="POST":

        name=request.POST['textfield']
        place=request.POST['textfield2']
        post = request.POST['textfield3']
        pin = request.POST['textfield4']
        category= request.POST['textfield5']
        qualification = request.POST['textfield6']
        phone_No = request.POST['textfield7']
        email= request.POST['textfield8']
        did = request.session['lid']
        doctor.objects.filter(doctorid=did).update(doctorname=name,doctorplace=place,doctorpost=post,doctorpin=pin,pho_no=phone_No,qualification=qualification,category=category)
        return HttpResponse('''<script>alert("Refistered");window.location="/dhome" </script>''')



    else:

        did = request.session['lid']
        qry=doctor.objects.get(doctorid=did)
        return render(request,"doctor_temp/PROFILE.html",{"data":qry})


def add_schedule(request):
    if request.method=="POST":
        sd=request.POST['textfield']
        st=request.POST['textfield2']
        tc=request.POST['textfield3']
        did=request.session['lid']
        obj=schedule()
        obj.tocken_count=tc
        obj.schedulingtime=st
        obj.schedulingdate=sd
        obj.doctorid_id=did
        obj.save()
        return HttpResponse('''<script>alert("Refistered");window.location="/schedule" </script>''')
    else:
        return render(request,"doctor_temp/ADD_SCHEDULE.html")



def view_schedule(request):
    did = request.session['lid']
    qry=schedule.objects.filter(doctorid=did)
    return render(request,"doctor_temp/VIEW_SCHEDULE.html",{'data':qry})


def view_booking(request):
    did = request.session['lid']

    qry =booking.objects.filter(schedule_id__doctorid=did)
    return render(request,"doctor_temp/VIEW_BOOKING.html",{'data':qry})

def doctor_home(request):
    return render(request,"doctor_temp/doctor_index.html")


def delete_schedule(request,id):
    obj=schedule.objects.get(id=id)
    obj.delete()
    return redirect('/schedule_view')

def view_rating(request):
    qry=rating.objects.filter(doctorid=request.session['lid'])
    # qry = rating.objects.all()
    ar_rt = []
    data = []
    for i in qry:
        d = {}
        val = str(i.rating)
        ar_rt.append(val)
        d['uname'] = i.userid.username
        # d['rdate']=i.rdate
        data.append(d)

    fs = "/static/star/full.jpg"
    hs = "/static/star/half.jpg"
    es = "/static/star/empty.jpg"
    arr = []
    for i in range(len(ar_rt)):
        rt = ar_rt[i]
        dd = data[i]
        print(rt)
        a = float(rt)

        if a >= 0.0 and a < 0.4:
            print("eeeee")
            ar = [es, es, es, es, es]
            arr.append(ar)

        elif a >= 0.4 and a < 0.8:
            print("heeee")
            ar = [hs, es, es, es, es]
            arr.append(ar)

        elif a >= 0.8 and a < 1.4:
            print("feeee")
            ar = [fs, es, es, es, es]
            arr.append(ar)

        elif a >= 1.4 and a < 1.8:
            print("fheee")
            ar = [fs, hs, es, es, es]
            arr.append(ar)

        elif a >= 1.8 and a < 2.4:
            print("ffeee")
            ar = [fs, fs, es, es, es]
            arr.append(ar)

        elif a >= 2.4 and a < 2.8:
            print("ffhee")
            ar = [fs, fs, hs, es, es]
            arr.append(ar)

        elif a >= 2.8 and a < 3.4:
            print("fffee")
            ar = [fs, fs, fs, es, es]
            arr.append(ar)

        elif a >= 3.4 and a < 3.8:
            print("fffhe")
            ar = [fs, fs, fs, hs, es]
            arr.append(ar)

        elif a >= 3.8 and a < 4.4:
            print("ffffe")
            ar = [fs, fs, fs, fs, es]
            arr.append(ar)

        elif a >= 4.4 and a < 4.8:
            print("ffffh")
            ar = [fs, fs, fs, fs, hs]
            arr.append(ar)

        elif a >= 4.8 and a <= 5.0:
            print("fffff")
            ar = [fs, fs, fs, fs, fs]
            arr.append(ar)
        print(arr)
        dd['rating'] = ar
    # return render(request, 'admin/view_rating.html', {'resu': data, 'r1': arr, 'ln': len(arr)})
    return render(request,"doctor_temp/VIEW_RATING.html",{'resu': data, 'r1': arr, 'ln': len(arr)})

# ==============================================USER MODULE=============================================================

def and_log(request):
        u=request.POST['u']
        p=request.POST['p']
        qry=login.objects.filter(username=u,password=p)
        if qry.exists():
            qry=qry[0]
            ob=user.objects.get(userid=qry)
            return JsonResponse({"status":"ok","type":qry.usertype,"lid":qry.id,"name":ob.username,'em':ob.email})
        else:
            return JsonResponse({"status":"no"})


def and_complaint(request):
        c=request.POST['comp']
        uid=request.POST['id']
        u=user.objects.get(userid=uid)
        uu=u.id
        date=datetime.datetime.now().strftime("%Y-%m-%d")
        print(date)
        obj=complaints()
        obj.complaints=c
        obj.complaint_date=str(date)
        obj.reply='pending'
        obj.reply_date='pending'
        obj.userid_id=uu
        obj.save()
        return JsonResponse({"status": "ok"})


def and_views(request):
    uid = request.POST['id']
    u = user.objects.get(userid=uid)
    uu = u.id

    qry=complaints.objects.filter(userid=uu)
    ar = []
    for i in qry:
        ar.append({"complaints":i.complaints,"complaint_date":i.complaint_date,"reply":i.reply_date,"reply_date":i.reply_date})
    return JsonResponse({"status":"ok","data":ar})


def and_doctor(request):
    qry=doctor.objects.filter(doctorid__usertype='doctor')
    ar = []
    for i in qry:
        ar.append({"id":i.id,"doctorname":i.doctorname,"doctorplace":i.doctorplace,"doctorpin":i.doctorpin,"doctorpost":i.doctorpost,"email":i.email,"ph_no":i.pho_no,"qualification":i.qualification,"category":i.category})
    return JsonResponse({"status":"ok","data":ar})



def and_viewprofile(request):
    lid=request.POST['id']
    qry=user.objects.get(userid=lid)
    return JsonResponse({"status":"ok","username":qry.username,"place":qry.place,"phone":qry.phone,"email":qry.email,"height":qry.height,"weight":qry.weight,"age":qry.age})

def and_update_profile(request):
    u = request.POST['u']
    p = request.POST['p']
    ph = request.POST['ph']
    e = request.POST['e']
    h = request.POST['h']
    w = request.POST['w']
    a = request.POST['a']
    uid = request.POST['id']
    user.objects.filter(userid=uid).update(username=u,place=p,phone=ph,email=e,height=h,weight=w,age=a)
    return JsonResponse({"status": "ok"})


def and_schedule(request):
    did=request.POST['doctorid']

    qry=schedule.objects.filter(doctorid=did)
    ar = []
    for i in qry:
        ar.append({"id":i.id,"tocken_count":i.tocken_count,"schedulingtime":i.schedulingtime,"schedulingdate":i.schedulingdate})
    return JsonResponse({"status":"ok","data":ar})


def and_userregistration(request):
    us =request.POST['uname']
    p = request.POST['p']
    phn =request.POST['phn']
    e = request.POST['e']
    h =request.POST['h']
    w = request.POST['w']
    a = request.POST['a']
    pa=request.POST['pa']
    cp=request.POST['cp']

    obj1=login()
    obj1.username=e
    obj1.password=pa
    obj1.usertype='user'
    obj1.save()

    obj=user()
    obj.username=us
    obj.place=p
    obj.phone=phn
    obj.email=e
    obj.height=h
    obj.weight=w
    obj.age=a
    obj.userid=login.objects.get(id=obj1.id)
    obj.save()
    return JsonResponse({"status":"ok"})


def and_book(request):
    sid=request.POST['sid']
    id=request.POST['id']
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    qry=schedule.objects.get(id=sid)
    # t=qry.tocken_count
    # qry1=booking.objects.filter(schedule_id=id)
    # if qry1.exists():
    #     tk=qry1.tocken_no
    #     print(tk)
    #     obj=booking()
    #     obj.date=date
    #     obj.tocken_no=tk+1
    #     obj.schedule_id_id=sid
    #     obj.userid=user.objects.get(userid=id)
    #     obj.save()
    #     return JsonResponse({"status":"ok"})
    # else:
    obj=booking()
    obj.date = date
    obj.tocken_no = "1"
    obj.schedule_id_id = sid
    obj.userid = user.objects.get(userid=id)
    obj.save()
    return JsonResponse({"status": "ok"})

def and_view_booking(request):
    id=request.POST['id']
    u=user.objects.get(userid=id)
    qry=booking.objects.filter(userid=u)

    ar = []
    for i in qry:
        ar.append({"id": i.schedule_id.doctorid_id, "Date": i.date, "Doctorname": i.schedule_id.doctorid.doctorname,"schedulingdate": i.schedule_id.schedulingdate,"token_no": i.tocken_no})
    return JsonResponse({"status": "ok", "data": ar})


# ==============chat=================


def inmessage(request):
    fid=request.POST['lid']
    toid=request.POST['toid']
    msg=request.POST['message']
    # rtype=request.POST['type']
    # print(fid,toid,msg,"sendddddddd")
    u=user.objects.get(userid=fid)
    # uid=u.id
    d=doctor.objects.get(id=toid)
    # did=d.id
    ch=chat()
    ch.date=datetime.datetime.now().date()
    ch.userid=u
    ch.doctorid=d
    ch.type="user"
    ch.message=msg

    ch.save()
    return JsonResponse({'status':'Inserted'})

def view_message2(request):
    fid=request.POST['lid']
    toid=request.POST['toid']
    lmid=request.POST['lastid']
    usr = user.objects.get(userid=fid)
    # u=usr.id
    adv = doctor.objects.get(id=toid)
    print("aaa",fid,toid,lmid)
    d=adv.id
    # cha = chat.objects.filter(userid=usr,doctorid=adv,id__gte=lmid)
    cha = chat.objects.filter(user_id=usr,doctor_id=adv,id__gte=lmid)

    if cha.exists():
        a = []
        for i in cha:
            print(i)
            if i.id > int(lmid):
                a.append({'id': i.id, 'msg': i.message, 'date': i.date, 'type':i.type})
        print(a)
        return JsonResponse({'status': 'ok', 'data': a})
    else:
        return JsonResponse({'status': 'no'})

def and_chat_doctor(request):
    qry = doctor.objects.filter(doctorid__usertype='doctor')
    if qry.exists():
        ar = []
        for i in qry:
            ar.append(
                {'did': i.id, 'dn': i.doctorname})

        return JsonResponse({'status': 'ok', 'data': ar})
    else:
        return JsonResponse({'status': 'no'})




def doctor_view_users(request):
    obj=booking.objects.filter(schedule_id__doctorid_id=request.session['lid'])
    return render(request, "doctor_temp/view_users.html", {'data':obj})

def doctor_Chat_user(request, id):
    obj=chat.objects.filter(doctor_id_id=request.session['lid'], user_id_id=id)
    return render(request, "doctor_temp/doctor_user_chat.html", {'data':obj, 'u':id})



def doctor_in_message2(request):
    fromid = request.session['lid']
    print("fromid",fromid)
    toid = request.POST['u']
    print("toid",toid)
    message=request.POST['e']
    ob=chat()
    ob.doctor_id=doctor.objects.get(id=fromid)
    ob.user_id=user.objects.get(id=toid)
    ob.message=message
    ob.date=datetime.datetime.now().date()
    ob.type="doctor"
    ob.save()
    data = {"task": "success"}
    return JsonResponse(data)




def view_message2(request):
    fromid=request.session['lid']
    toid=request.POST['toid']
    lmid = request.POST['lmid']

    from django.db import connection
    doctor_id = doctor.objects.get(doctorid=fromid)
    user_id = user.objects.get(id=toid)

    cursor=connection.cursor()
    sen_res = []
    # qry="SELECT * FROM diabetes_moule_chat WHERE (fromid='"+str(doctor_id.id)+"' AND toid='"+str(toid)+"') OR (fromid='"+str(toid)+"' AND toid='"+str(doctor_id.id)+"') ORDER BY DATE ASC"
    cursor.execute("SELECT type,`message`,`date`,`id` FROM `diabetes_moule_chat` WHERE  `doctor_id_id`='"+str(fromid)+"' AND  `user_id_id`='"+toid+"' AND  (type = 'doctor' or type ='user')  ORDER BY id ASC")
    # cursor.execute(qry)
    # print("SELECT `from_id`,`message`,`date`,`chat_id` FROM `chat` WHERE `chat_id`>%s AND ((`to_id`=%s AND  `from_id`=%s) OR (`to_id`=%s AND `from_id`=%s)  )  ORDER BY chat_id ASC''')
    # val=(str(lmid),str(toid),str(fromid),str(fromid),str(toid))
    res=cursor.fetchall()
    # print(res,"============================")
    data = []
    lm=lmid
    for i in res:
        lm=i[3]
        row = {"type": i[0], "chat": i[1], "date": i[2],
               'id': i[3]}
        data.append(row)
    print(data)

    return JsonResponse({"data": data,"status":"ok", 'lmid':lm})




def in_message_and(request):
    fromid = request.POST['fid']
    print("fromid",fromid)
    toid = request.POST['toid']
    print("toid",toid)
    message=request.POST['msg']
    ob=chat()
    ob.doctor_id=doctor.objects.get(id=toid)
    ob.user_id=user.objects.get(userid_id=fromid)
    ob.message=message
    ob.date=datetime.datetime.now().date()
    ob.type="user"
    ob.save()
    data = {"status": "Inserted"}
    return JsonResponse(data)




def viewchat(request):
    fromid=request.POST['lid']
    toid=request.POST['toid']
    print(fromid, toid)
    lmid = request.POST['lastid']
    print("msgggggggggggggggggggggg"+lmid)
    from django.db import connection
    cursor=connection.cursor()
    usr = user.objects.get(userid=fromid)
    sen_res = []
    cursor.execute("SELECT type,`message`,`date`,`id` FROM `diabetes_moule_chat` WHERE diabetes_moule_chat.id>'"+lmid+"' and  `doctor_id_id`='"+str(toid)+"' AND  `user_id_id`='"+str(usr.id)+"' AND  (type = 'doctor' or type ='user')  ORDER BY id ASC")
    res=cursor.fetchall()
    print(res,"============================")
    data = []
    lm=lmid
    for i in res:
        lm=i[3]
        row = {"type": i[0], "chat": i[1], "date": i[2],'id': i[3]}
        data.append(row)
    print(data)

    return JsonResponse({"data": data,"status":"ok"})


# ==========================================================================================================================================
#                                                 MAIN SECTION
# ==========================================================================================================================================

# =============================# diabeties_prediction============================================================


def bmii(request):
    id=request.POST['id']
    qry=user.objects.get(userid=id)
    height=qry.height
    weight=qry.weight
    h1=float(height)/100
    w=float(weight)
    print(height)
    bmi_calc=w/(h1*h1)
    bb=round(bmi_calc,1)
    print(bmi_calc)
    return JsonResponse({"status":"ok","bm":bb})



def diabet_prediction(request):
    Pregnaneies=request.POST['preg']
    Glucose=request.POST['gluc']
    Blood_Pressure=request.POST['bp']
    Skin_Thikness=request.POST['skin']
    Insulin=request.POST['insl']
    Diabetes_Pedigree_Function=request.POST['dpf']
    Age=request.POST['agee']
    bmi=request.POST['bmi']
    import numpy as np

    ar = []

    ar.append(int(Pregnaneies))
    ar.append(int(Glucose))
    ar.append(int(Blood_Pressure))
    ar.append(int(Skin_Thikness))
    ar.append(int(Insulin))
    ar.append(float(bmi))
    ar.append(int(Diabetes_Pedigree_Function))
    ar.append(int(Age))

    aatest = np.array([ar])
    import pandas as pd
    a = pd.read_csv("D:\\diabetes_prediction\\diabetes_moule\\static\\datasets\\diabetes\\diabetes.csv")
    attributes = a.values[:, 0:8]
    labels = a.values[:, 8]

    rf = RandomForestClassifier()
    rf.fit(attributes, labels)
    res = rf.predict(aatest)
    print(res)
    return JsonResponse({'status': 'ok', 'rslt': res[0]})




# ===================================================skin disease=============================================


def skin_diseases(request):
    picc=request.FILES['pic']
    date=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs=FileSystemStorage()
    fs.save(r"D:\diabetes_prediction\diabetes_moule\static\pic\\"+date+'.jpg',picc)
    import numpy as np
    from skimage import io, color, img_as_ubyte
    # from DBConnection import Db
    from skimage.feature import greycomatrix, greycoprops
    from sklearn.metrics.cluster import entropy
    #
    rgbImg = io.imread(r"D:\diabetes_prediction\diabetes_moule\static\pic\\"+date+'.jpg')
    grayImg = img_as_ubyte(color.rgb2gray(rgbImg))

    distances = [1, 2, 3]
    angles = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]
    properties = ['energy', 'homogeneity', 'dissimilarity', 'correlation', 'contrast']

    glcm = greycomatrix(grayImg,
                        distances=distances,
                        angles=angles,
                        symmetric=True,
                        normed=True)

    feats = np.hstack([greycoprops(glcm, 'energy').ravel() for prop in properties])
    feats1 = np.hstack([greycoprops(glcm, 'homogeneity').ravel() for prop in properties])
    feats2 = np.hstack([greycoprops(glcm, 'dissimilarity').ravel() for prop in properties])
    feats3 = np.hstack([greycoprops(glcm, 'correlation').ravel() for prop in properties])
    feats4 = np.hstack([greycoprops(glcm, 'contrast').ravel() for prop in properties])

    k = np.mean(feats)
    l = np.mean(feats1)
    m = np.mean(feats2)
    n = np.mean(feats3)
    o = np.mean(feats4)
    ar = []
    ar.append(k)
    ar.append(l)
    ar.append(m)
    ar.append(n)
    ar.append(o)
    arr = []
    test_val = np.array(ar)
    arr.append(test_val)

    import pandas as pd
    a = pd.read_csv(r"D:\diabetes_prediction\diabetes_moule\static\datasetsfeatures.csv")
    attributes = a.values[1:, 0:5]
    labels = a.values[1:, 5]

    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(attributes, labels)
    pred = rf.predict(arr)
    # print(pred, pred[0][1])
    print(pred)
    if pred == 'Acne and Rosacea':
        return JsonResponse({"status":"ok","rslt":"Predicted result is Acne and Rosacea disease"})
    elif pred == 'Actinic Keratosis':
        return JsonResponse({"status":"ok","rslt":"Predicted result is Actinic Keratosis disease"})
    elif pred == 'Atopic Dermatitis':
        return JsonResponse({"status":"ok","rslt":"Predicted result is Atopic Dermatitis disease"})
    elif pred == 'Bullous Disease':
        return JsonResponse({"status":"ok","rslt":"Predicted result is Bullous Disease disease"})
    else:
        return JsonResponse({"status":"ok","rslt":"Error..Try Again!!"})








# ===========================================COVID PREDICTION===================================================



def covid_prediction(request):
    fever=request.POST['r1']
    tirdness=request.POST['r2']
    dry_cough=request.POST['r3']
    difficulty_in_breathing=request.POST['r4']
    sore_throat=request.POST['r5']
    none_sympton=request.POST['r6']
    pains=request.POST['r7']
    nasal_congestion=request.POST['r8']
    runny_nose=request.POST['r9']
    diarrhea=request.POST['r10']
    none_experiencing=request.POST['r11']
    age=request.POST['r12']
    gender=request.POST['r13']
    contact_dont_know=request.POST['r14']
    contact_no=request.POST['r15']
    contact_yes=request.POST['r16']
    import numpy as np

    ar = []

    ar.append(int(fever))
    ar.append(int(tirdness))
    ar.append(int(dry_cough))
    ar.append(int(difficulty_in_breathing))
    ar.append(int(sore_throat))
    ar.append(float(none_sympton))
    ar.append(int(pains))
    ar.append(int(nasal_congestion))
    ar.append(int(runny_nose))
    ar.append(int(diarrhea))
    ar.append(int(none_experiencing))
    ar.append(int(age))
    ar.append(int(gender))
    ar.append(int(contact_dont_know))
    ar.append(int(contact_no))
    ar.append(int(contact_yes))
    aatest = np.array([ar])
    import pandas as pd
    a = pd.read_csv("D:\\diabetes_prediction\\diabetes_moule\\static\\datasets\\covid\\aa.csv")
    attributes = a.values[:, 0:16]
    labels = a.values[:, 16]

    rf = RandomForestClassifier()
    rf.fit(attributes, labels)
    res = rf.predict(aatest)
    print(res)
    if res == 0:
        return JsonResponse({"status":"ok","rslt":"Mild Stage"})
    if res == 1:
        return JsonResponse({"status":"ok","rslt":"Modarate Stage"})
    if res == 2:
        return JsonResponse({"status": "ok", "rslt": "Result is negative"})
    if res == 3:
        return JsonResponse({"status": "ok", "rslt": "Severe Stage"})



# =====================================obesity prediction===============================================================


def obesity_prediction(request):
    gender=request.POST['r1']
    fh=request.POST['r2']
    fcvc = request.POST['r3']
    ncp = request.POST['r4']
    caec = request.POST['r5']
    smoke = request.POST['r6']
    ch20 = request.POST['r7']
    ssc = request.POST['r8']
    faf = request.POST['r9']
    tue = request.POST['r10']
    calc = request.POST['r11']
    mtrans = request.POST['r12']
    # gender = request.POST['r1']
    # Age = request.POST['r2']
    # Height = request.POST['r3']
    # Weight = request.POST['r4']
    # fh = request.POST['r5']
    # favc = request.POST['r6']
    # fcvc = request.POST['r7']
    # ncp = request.POST['r8']
    # caec = request.POST['r9']
    # smoke = request.POST['r10']
    # ch20 = request.POST['r11']
    # ssc = request.POST['r12']
    # faf = request.POST['r13']
    # tue = request.POST['r14']
    # calc = request.POST['r15']
    # mtrans = request.POST['r16']
    import numpy as np

    ar= []



    ar.append(int(gender))
    ar.append(int(Age))
    ar.append(int(Height))
    ar.append(int(Weight))
    ar.append(int(fh))
    ar.append(int(favc))
    ar.append(int(fcvc))
    ar.append(int(ncp))
    ar.append(int(caec))
    ar.append(int(smoke))
    ar.append(int(ch20))
    ar.append(int(ssc))
    ar.append(int(faf))
    ar.append(int(tue))
    ar.append(int(calc))
    ar.append(int(mtrans))
    import  pandas as pd
    a = pd.read_csv("D:\\diabetes_prediction\\diabetes_moule\\static\\datasets\\obesity\\obcpr.csv")

    attributes = a.values[:, 0:16]
    labels = a.values[:, 16]

    rf = RandomForestClassifier()
    rf.fit(attributes, labels)
    res = rf.predict(ar)
    print(res)
    if res == 0:
        return JsonResponse({"status":"ok","rslt":"Normal weight"})
    if res == 1:
        return JsonResponse({"status":"ok","rslt":"Insufficient Weight"})
    if res == 2:
        return JsonResponse({"status":"ok","rslt":"Normal weight"})
    if res == 3:
        return JsonResponse({"status":"ok","rslt":"Over weight level I"})
    if res == 4:
        return JsonResponse({"status":"ok","rslt":"Over weight level II"})
    if res == 5:
        return JsonResponse({"status":"ok","rslt":"Obesity type I"})
    if res == 6:
        return JsonResponse({"status":"ok","rslt":"Obesity type II"})
    if res == 7:
        return JsonResponse({"status":"ok","rslt":"Obesity type III"})







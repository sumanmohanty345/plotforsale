from django.shortcuts import render
from .models import PlotModel,EmployeeModel,AppartmentModel
# Create your views here.
def Showmain(request):
    return render(request,"login.html")


def AdminSuccess(request):
    name=request.POST.get('uname')
    passd=request.POST.get('upass')
    if name == "admin" and passd == 'admin1997':
        return render(request,"Adminsucess.html")
    else:
        return render(request,'login.html',{'msg':"Wrong userId Or Password"})





def Addplot(request):

    return render(request,"addplot.html")


def Saveplot(request):
    plno=request.POST.get('pno')
    rno=request.POST.get('rdno')
    surno=request.POST.get('srno')
    costpersqr=request.POST.get('cqspo')
    otherexp=request.POST.get('oexp')
    boundries=request.POST.get('bnds')
    facing=request.POST.get('fac')
    sttus=request.POST.get('sts')
    tcost=request.POST.get('tct')
    pimg=request.FILES['pimg']
    PlotModel(plotno=plno,road_no=rno,survey_no=surno,cost_persqryrd=costpersqr,otherexpense=otherexp,boundry=boundries,facing=facing,status=sttus,total_cost=tcost,property_image=pimg).save()
    return render(request,"Adminsucess.html",{"msg":"Plot Added SUcsessfully"})


def editplot(request):
    return render(request,"editplot.html")


def Searchplot(request):
    plno=request.POST.get("plotno")
    return render(request,"editplot.html",{'data':PlotModel.objects.get(plotno=plno)})


def updateplot(request):
    plno = request.POST.get('pno')
    rno = request.POST.get('rdno')
    surno = request.POST.get('srno')
    costpersqr = request.POST.get('cqspo')
    otherexp = request.POST.get('oexp')
    boundries = request.POST.get('bnds')
    facing = request.POST.get('fac')
    sttus = request.POST.get('sts')
    tcost = request.POST.get('tct')
    pimg = request.FILES['pimg']
    PlotModel(plotno=plno, road_no=rno, survey_no=surno, cost_persqryrd=costpersqr, otherexpense=otherexp,boundry=boundries, facing=facing, status=sttus, total_cost=tcost,property_image=pimg).save()

    return render(request,"Adminsucess.html",{'msg2':"Plot updated Successfully"})


def viewallplot(request):
    return render(request,"viewall.html",{'plotdata':PlotModel.objects.all()})


def addaptmpt(request):
    return render(request,"addaptmpt.html")


def saveaptmpt(request):
    plno = request.POST.get('pno')
    rno = request.POST.get('rdno')
    surno = request.POST.get('srno')
    costpersqr = request.POST.get('cqspo')
    otherexp = request.POST.get('oexp')
    boundries = request.POST.get('bnds')
    facing = request.POST.get('fac')
    sttus = request.POST.get('sts')
    tcost = request.POST.get('tct')
    pimg = request.FILES['pimg']
    AppartmentModel(Appartmentno=plno,road_no=rno,survey_no=surno,cost_perbhk=costpersqr,otherexpense=otherexp,BHK=boundries,facing=facing,status=sttus,totalcost=tcost,Appartment_image=pimg).save()
    return render(request,"Adminsucess.html",{'msgsucs':"Appartment Added Sucessful"})


def viewallapt(request):
    return render(request,"viewallaptmpt.html",{'aptdata':AppartmentModel.objects.all()})


def editaptmpt(request):
    return render(request,"editaptmpt.html")


def searchaptmpt(request):
    plno = request.POST.get("plotno")
    return render(request, "editaptmpt.html", {'data': AppartmentModel.objects.get(Appartmentno=plno)})


def updateatmpt(request):
    plno = request.POST.get('pno')
    rno = request.POST.get('rdno')
    surno = request.POST.get('srno')
    costpersqr = request.POST.get('cqspo')
    otherexp = request.POST.get('oexp')
    boundries = request.POST.get('bnds')
    facing = request.POST.get('fac')
    sttus = request.POST.get('sts')
    tcost = request.POST.get('tct')
    pimg = request.FILES['pimg']
    AppartmentModel(Appartmentno=plno, road_no=rno, survey_no=surno, cost_perbhk=costpersqr, otherexpense=otherexp,BHK=boundries, facing=facing, status=sttus, totalcost=tcost, Appartment_image=pimg).save()
    return render(request, "Adminsucess.html", {'msgup2': "Appartment Updated Sucessful"})


def about(request):
    return render(request,"about.html")

from .forms import EmployeeFrom
def Addemployee(request):
    return render(request,'addemp.html',{'forms':EmployeeFrom()})


def Saveemployee(request):
    idn=request.POST.get('idno')
    na=request.POST.get('name')
    mail=request.POST.get('mail')
    loc=request.POST.get('location')
    doj=request.POST.get('DOJ')
    desg=request.POST.get('designsation')
    qual=request.POST.get('qualification')
    rem=request.POST.get('remark')
    EmployeeModel(idno=idn,name=na,mail=mail,location=loc,DOJ=doj,designsation=desg,qualification=qual,remark=rem).save()
    return render(request,"Adminsucess.html",{"Empmsg":"Employee Added Sucessfully"})


def viewemployee(request):
    return render(request,"viewemployee.html",{'empdata':EmployeeModel.objects.all()})

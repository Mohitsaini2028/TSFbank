from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings
from . import models
import time

curl=settings.CURRENT_URL

def home(request):
    return render(request, "index.html",{'curl':curl})

def cusdetl(request):
    cus = models.addcustomer.objects.all()
    return render(request,"cusdetail.html",{'curl':curl,"data": cus})

def transactionH(request):
    cus = models.trans.objects.all()
    return render(request, "transactionh.html", {'curl':curl,"data": cus})

def addcustomer(request):
    if request.method=="GET":
        return render(request,"addcustomer.html",{'curl':curl,'msg':''})
    else:
        name=request.POST.get("name")
        mobile=request.POST.get("mobile")
        email=request.POST.get("email")
        account=request.POST.get("account")
        balance=request.POST.get("balance")
        info=time.asctime(time.localtime(time.time()))
        p=models.addcustomer(name=name,mobile=mobile,email=email,account=account,balance=balance,role=0,dt=info)
        p.save()

        return render(request,"addcustomer.html",{'curl':curl,'msg':'Customer Added Successfully....'})

def transaction(request):
	c = models.addcustomer.objects.all()
	a = request.GET["a"]

	ad = models.addcustomer.objects.filter(account = a)

	return render(request, "transaction.html", {"a":a, "data":ad,  "clist":c})

def send(request,pk):
	sname=request.POST.get("sname")
	sacc=request.POST.get("sacc")
	sb=request.POST.get("sb")
	rname=request.POST.get("rname")
	amount=request.POST.get("amount")
	info=time.asctime(time.localtime(time.time()))
	ad =models.addcustomer.objects.get(name=sname)
	cu = models.addcustomer.objects.get(name=rname)
	cu.balance = str(int(amount) + int(cu.balance))
	cu.save()
	ad.balance = str(int(ad.balance) - int(amount))
	ad.save()

	tr = models.trans(sname=sname,sacc=sacc,sb=sb,rname=rname,amount=amount,dt=info)
	tr.save()

	return render(request,"transaction.html",{'curl':curl,'pk':pk,'msg':'Money Transfered Successfully....'})


# def delete(request):
# 	dell = request.GET.get("del")
# 	regid=request.GET.get("regid")
# 	# d = models.trans.objects.get(sacc = dell)
# 	# d.delete()
# 	models.trans.objects.filter(regid=regid).delete()
# 	return render(request,"transactionH.html",{'curl':curl,'msg':'Transaction Deleted Successfully....'})


# 	#  s=request.GET.get("s")
#     #     regid=request.GET.get("regid")

# 	# 	myweb_models.Register.objects.filter(regid=int(regid)).delete()

# 	# 	{{curl}}myadmin/manageuserstatus/?s=delete&regid={{row.regid}}

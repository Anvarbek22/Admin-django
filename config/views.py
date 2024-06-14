from django.shortcuts import render,redirect,HttpResponse
from django.template import RequestContext
from django.views import View
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from datetime import *


def loginPage(request,UN,PN,TS,CM,P,M):
    Userss.objects.create(UN=UN,PN=PN,TS=TS,CM=CM,P=P,M=M)
    return HttpResponse("Complite")
    

def handler404(request,exception):
    return render(request,'404.html',status=404)

def HomePage(request):
    data2=[]
    user=request.user

    if str(user)=="AnonymousUser":
        user=""
    return render(request,'index.html',{"user":user})


def ShopsPage(request):
    data=Maxsulotlar.objects.all()
    data2=[]
    for i in data:
        print(i.img)
        data2.append([i.id,i.name,i.destrib,i.img])
    return render(request,'SHOPS.html',{"data2":data2})



def ShopsBuyPage(request,name):
    data=Maxsulotlar.objects.all()
    if request.method=="POST":
        miqtor=request.POST.get("qiymat")
        now=datetime.now()
        kun=now.day+5
        yil=now.year
        oy=now.month
        sana=datetime(yil,oy,kun)
        x=Maxsulotlar.objects.all()[name-1]
        x.min_soni=str(int(x.min_soni)+int(miqtor))
        x.save()
        return redirect("/shop/")
    data2=["false"]
    for i in data:
        if i.id==name:
            data2=["true",i.name,i.narx,i.destrib,i.img,i.id,i.url]
    return render(request,'SHOPS.html',{"data2":data2})

 
# class AdminPage(View):
#     def post(self,request):
#         data=Maxsulotlar.objects.all()
#         name=request.POST.get('name')
#         price=request.POST.get('narx')
#         dona=request.POST.get('donasi')
#         dest=request.POST.get('dest')
#         img=request.POST.get('img')
#         for i in data:
#             if name==i.name:
#                 i.narx=price
#                 i.max_soni=str(int(dona)+int(i.max_soni))
#                 i.min_soni=0
#                 i.destrib=dest
#                 i.img=img
#                 i.save()
#                 break
#         else:        
#             Maxsulotlar.objects.create(name=name,narx=price,max_soni=dona,min_soni='0',destrib=dest,img=img)
#         return redirect("/administrator/76435667666574364324343sdjfnaervireugiberuefgyerubrurf3489t394u9hdfueh3487ty3h97f3r/")
#     def get(self,request):     
#             data=Maxsulotlar.objects.all()
#             data2=[]
#             t=40
#             for i in data:
#                 data2.append([i.name,i.narx,int((int(i.max_soni)-int(i.min_soni))/int(i.max_soni)*100),t])
#                 t+=30
#             return render(request,"admin.html",{"data":data,"data2":data2,"form":form})

# Create your views here.

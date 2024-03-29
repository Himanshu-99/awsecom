from django.shortcuts import render, redirect
from app1.models import ProductModel

# Create your views here.
def showindex(request):
    return render(request,'index.html',{"product":ProductModel.objects.all()})


def save_photo(request):
    no = request.POST.get('t1')
    nam = request.POST.get('t2')
    pri = request.POST.get('t3')
    photo = request.FILES['photo']
    ProductModel(no=no,name=nam,price=pri,photo=photo).save()
    return redirect('main')


def delete(request):
    delnum = request.POST["no"]
    ProductModel.objects.filter(no=delnum).delete()
    return redirect('main')

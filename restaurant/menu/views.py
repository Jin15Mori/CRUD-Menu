from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from menu.models import Home
from django.template import loader

# Create your views here.
def index(request):
    if request.method=='POST':
        foodname = request.POST.get('foodname')
        foodcost = request.POST.get('foodcost')
        foodtype = request.POST.get('foodtype')
        x = Home(foodname = foodname, foodcost = foodcost, foodtype = foodtype)
        x.save()
    return render(request, "index.html")

def show(request):
   myhome = Home.objects.all().values()
   template = loader.get_template('show.html')
   context = {
           'myhome': myhome,
  }
   return HttpResponse(template.render(context, request))

def update(request,id):
    myhome = Home.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'myhome': myhome,
    }
    return HttpResponse(template.render(context,request))

def delete(request,id):
    home = Home.objects.get(id=id)
    home.delete()
    return HttpResponseRedirect(reverse('index'))

def updaterecord(request,id):
    foodname = request.POST['foodname']
    foodcost = request.POST['foodcost']
    foodtype = request.POST['foodtype']
    home = Home.objects.get(id=id)
    home.foodname = foodname
    home.foodcost =foodcost
    home.foodtype = foodtype
    home.save()
    return HttpResponseRedirect(reverse('index'))
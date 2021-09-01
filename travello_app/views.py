from django.shortcuts import render
from django.shortcuts import render
from . models import place,blog
# Create your views here.
def fun(request):
    #
    # obj=place()
    # obj.name="kerala"
    # obj.price=200
    # obj.desc="God's own country"
    obj=place.objects.all()
    obj1=blog.objects.all()
    # obj1=detail.objects.all()

    return render(request,"index.html",{'results':obj,'blogs':obj1})


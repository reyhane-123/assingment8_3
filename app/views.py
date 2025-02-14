from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
list1=[
    {"id":1,"name":"class_python","description":"پایتون از همهی زبان های برنامه نویسی اسان تر است"},
    {"id":2,"name":"class_html","description":"برای طراحی وب استفاده میشود و ساختار صفحه وب را مشخص میکند و عناصر مختلفی دارد"},
    {"id":3,"name":"class_jango","description":"برنامه نویسی توسعه یافته است و هدف اصلی ان ساخت  وبسایت های پیچیده است"},
    {"id":4,"name":"class_c#","description":"زبان برنامه نویسی چندمنظوره و سطح بالا است"},
]

def detail(request):
    context={'list':list1}
    return render(request,'app/list.html', context=context)

def course_list(request,id):
    selected_item={}
    for item in list1:
        if item["id"] == id:
            selected_item = item
    return render(request,'app/list2.html', context=selected_item)
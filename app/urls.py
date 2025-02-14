from django.urls import path
from . import views

urlpatterns = [
    path('course_list/<int:id>',views.course_list, name="course"),
    path('detail',views.detail),
]

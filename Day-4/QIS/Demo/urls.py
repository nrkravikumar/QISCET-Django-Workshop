from django.urls import path
from Demo import views

urlpatterns = [
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('cnt/',views.contact,name="ct"),
    path('rg/',views.reg,name="rt"),
]

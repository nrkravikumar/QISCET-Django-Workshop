from django.urls import path
from Demo import views
from django.contrib.auth import views as y 

urlpatterns = [
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('cnt/',views.contact,name="ct"),
    # path('rg/',views.reg,name="rt"),
    path('rg/',views.regi,name="rt"),
    path('ds/',views.dashboard,name="dsh"),
    path('lg/',y.LoginView.as_view(template_name="html/login.html"),name="log"),
    path('lgt/',y.LogoutView.as_view(template_name="html/logout.html"),name="logt"),
]

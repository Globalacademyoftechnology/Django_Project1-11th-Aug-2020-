from django.urls import path
app_name="Myapp"
from Myapp import views

urlpatterns=[
    
    path("header",views.header,name="header"),
    path("base",views.base,name="base"),
    path("about_us",views.about_us,name="about_us"),
    path("gallery",views.gallery,name="gallery"),
    path("order",views.order,name="order"),
    path("sign_up",views.sign_up,name="sign_up"),
    path("login",views.login,name="login"),
    

    
    
    
]
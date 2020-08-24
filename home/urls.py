from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # vì views này  trùng tên với line 2 nên đổi tên là auth_views . views của cái auth
urlpatterns = [
    path('', views.HomeView,name='home'),
    path('base/',views.HomeBase),
    path('pages/<int:id>',views.Sanpham),
    path('test1/',views.test1),
    #path('pages/<int:id>',views.test2),
    path('home/<int:id>',views.Dienthoai),
    path('table/',views.Table),
    path('oplung/',views.Oplung),
    path('phukien/',views.Phuk),
    path('hangcu/',views.Hangcu),
    path('lienhe/',views.Lienhe),
    path('register/',views.register,name='register'),
    #path('<int:pk>/', views.PostDetal, name = "data"),
    #path('contact/', views.contact),
    path('luugh',views.savecart,name='luugh'),
    path('pages/GB/',views.color,name='mausat'),
    path('pages/gioh/',views.gioh,name="gioh"), #trang url.py
    path('giohang/',views.shopcart,name='danh sach sp trong gha'),
    path('login/', auth_views.LoginView.as_view(template_name="pages/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name='logout')
]
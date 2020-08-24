from django.shortcuts import render
from . import templates
from .forms import RegistrationForm,cartform
from .models import Products,Productype,Prodtype,Giohang
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import ListView,DetailView
from django.template.loader import render_to_string, get_template
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
       total = 0;#khai bao tinh tong tien trong gio hang
       carts = request.session['cart']
       for key,value in carts.items():
              total += int(value['price'])*int(value['num'])
              tol =key.count()
       return render(request, 'pages/home.html',{'total':total,'tol':tol,'carts':carts})
def HomeBase(request):#template
       Data1 = {'Pro':Productype.objects.filter(idname=1)}
       return render(request,'pages/base.html',Data1)
def HomeView(request):#trang chủ   
       Data = {'Data':Products.objects.filter(idpro=1),'Pro':Productype.objects.filter(idname=1),'tab':Products.objects.filter(idpro=2)}
       return render(request,'pages/home.html',Data)
#def Showsp(request,pk):
def Sanpham(request, id):
       pro = {'product':Products.objects.get(id=id),'Pro':Productype.objects.filter(idname=1)} 
       return render(request,'pages/product.html',pro)
def color(request,id):
       html=()
       if request.is_ajax(): #kiem tra thong tin = ajax
              id = request.POST.get('id') #id san pham  = id
              num = request.POST.get('num')#so luong
              Prod = Products.objects.get(id=id)
       return render(request,'pages/product.html',{'{product':Prod})
def test1(request):
       test1 = Test2.objects.all()
       return render(request,'pages/test1.html',{'test1':test1})
def test2(request, id):
         test2 = Test2.objects.get(id=id)
         return render(request,'pages/test2.html',{'test2':test2})
def Dienthoai(request, id):
       Data = {'Data':Products.objects.filter(idtype=id),'Pro':Productype.objects.filter(idname=1)}    
       return render(request,'pages/dienthoai.html',Data)
def Table(request):
        Data = {'Data':Products.objects.filter(idpro=2),'Pro':Productype.objects.filter(idname=1)}        
        return render(request,'pages/table.html',Data)
def Oplung(request):
       Data = {'Data':Products.objects.filter(idpro=3),'Pro':Productype.objects.filter(idname=1)}        
       return render(request,'pages/oplung.html',Data)
def Phuk(request):
       Data = {'Data':Products.objects.filter(idpro=3),'Pro':Productype.objects.filter(idname=1)}
       return render(request, 'pages/phuk.html',Data)
def Hangcu(request):
       Data = {'Data':Products.objects.filter(type='99%'),'Pro':Productype.objects.filter(idname=1)}    
       return render(request,'pages/hangcu.html',Data) 
def Lienhe(request):
       return render(request, 'pages/')
def register(request):
       form = {'form':RegistrationForm(),'Pro':Productype.objects.filter(idname=1)}
       if request.method == 'POST':
              form = RegistrationForm(request.POST)
              if form.is_valid():# kiểm tra coi có hợp lệ hok hàm valid sẽ tự động gọi toàn bộ hàm bên form.py kiểm tra
                     form.save()# nếu hợp lệ thì lưu lại
                     user = form.cleaned_data.get('username')
                     messages.success(request, 'Đã tồn tại tài khoản ' + user)
                     return HttpResponseRedirect('/login') # khi đăng nhập thành công trả về trang chủ hoặc {% url 'home' %}
       return render(request, 'pages/register.html', form)
def login(request):
       if request.method == 'POST':
              username = request.POST.get('username')
              password = request.POST.get('password')
              user = authenticate(request, username=username, password=password)
              if user is not None:
                     login(request, user)
                     return redirect('home')#đăng nhập xong trả về trang chủ
              else:
                     messages.info(request,"Đăng nhập thất bại, vui lòng thử lại")
       context = {}
       return render(request, 'pages/login.html',context)
def logout(request):
       logout(request)
       return redirect('home')
       return render(request,'pages/home.html')
cart={}
@login_required(login_url='/login')
def gioh(request): #views.py
       html=()
       current_user = request.user
       if request.is_ajax(): #kiem tra thong tin = ajax
              id = request.POST.get('id') #id san pham  = id . lấy ra sản phẩm mà người dùng gửi lên
              num = request.POST.get('num')#so luong
              Prod = Products.objects.get(id=id) #lay thong tin san pham theo id
              if id in cart.keys(): 
                     itemCart = { # đã mua hàng và muốn mua thêm món nữa
                            'user': current_user.id,
                            'name':Prod.name,
                            'price':Prod.price,
                            'img':str(Prod.image),
                            'num':int(cart[id]['num'])+1
                     }
              else:# lần đầu tiên kick vào mua hàng
                   itemCart = { 
                            'user': current_user.name,
                            'name':Prod.name,
                            'price':Prod.price,
                            'img':str(Prod.image),
                            'num':num
                     }
              cart[id] = itemCart
              request.session['cart'] = cart
              cartInfo = request.session['cart']
              html = render_to_string('pages/gioh.html',{'cart': cartInfo})
       return HttpResponse(html)

def shopcart(request):
       Pro = Productype.objects.filter(idname=1)
       total = 0;#khai bao tinh tong tien trong gio hang
       carts = request.session['cart']
       for key,value in carts.items():
              total += int(value['price'])*int(value['num'])
       return render(request,'pages/shopcart.html',{'total':total,'Pro':Pro})
def savecart(request):
       form = cartform()
       current_user = request.user
       if request.method == 'POST':
              carts = request.session['cart']
              form = cartform(request.POST)
              if form.valid():
                     Giohang = form.save(commit=False)
                     Giohang.iduser = request.user
                     Giohang.save()
                     messages.success(request, "ban da dat mua hang thanh cong")
                     return HttpResponseRedirect('/')
              else: print(form.errors)
       return render(request,'pages/shopcart.html',{'form':form})
#def upcart(request):

#def PostDetal(request):
#       Data = {'Data':Products.objects.all()}
#       paginate_by= 1
#       return render(request, 'pages/home.html', Data)
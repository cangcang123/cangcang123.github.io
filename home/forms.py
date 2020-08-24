from django import forms
from .models import Giohang
import re# kiểm tra coi có ký tự đặt biệt hok
from django.contrib.auth.models import User #lấy cái thư viện user ra
from django.core.exceptions import ObjectDoesNotExist # lấy cái lỗi ra
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=30) #charField là kiểm tra
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    #                                                 hàm này khi mình nhập mk nó sẽ che đi
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())
    def clean_password2(self):
        if 'password2' in self.cleaned_data: # hàm này kiểm tra pass 1 đã dc nhập chưa
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1: # kiểm tra pass có đúng hay hok . nếu ng dùng gõ dấu cách nhiều vẫn tính là clear
                return password2
        raise forms.ValidationError("Mật khẩu hok hợp lệ")
    def clean_username(self): #hàm kiểm tra usernam
        username = self.cleaned_data["username"] # lấy cái username ra
        if not  re.search(r'^\w+$', username): #kiểm tra username có ký tự đặt biệt hok not là phủ định 
            #(r'^\W+$') có nghĩa là ký tự thường  trong username phủ định xem nếu trong user hok phải kí tự thường thì trả về tên sai
            raise forms.ValidationError("tên đăng nhập hok đúng")
        try:# kiem tra xem tên username này có trung chưa
            User.objects.get(username=username)
        except ObjectDoesNotExist: # nếu cái objects này hok tồn tại , nếu như trả lại lỗi hok có user nào đã tồn tâij
            return username
        raise forms.ValidationError("Trùng tài khoản")
    def save(self):
        User.objects.create(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])
        # hàm tạo tài khoản

class cartform(forms.ModelForm):
    class Meta:
        model = Giohang
        fields = "__all__"





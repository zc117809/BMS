from django import forms
from app01 import models


# 登录表单
class LoginForm(forms.Form):
    username = forms.CharField(label='账号', widget=forms.widgets.TextInput(
        attrs={'class': "form-control", "placeholder": "Username", 'aria-describedby': "sizing-addon1"}))

    password = forms.CharField(label='密码', min_length=8,error_messages={'required':'账号或密码错误'}, max_length=16, widget=forms.widgets.PasswordInput(
        attrs={'class': "form-control", "placeholder": "Password", 'aria-describedby': "sizing-addon1"}))


class RegForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=32, label='账号',
                               error_messages={'min_length': '最小4位', 'max_length': '最大32位', 'required': '账号不能为空', },
                               widget=forms.widgets.TextInput(
                                   attrs={'class': 'form-control c1 c2', 'placeholder': "请输入注册账号",
                                          'aria-describedby': "sizing-addon1"}))
    password = forms.CharField(min_length=6, max_length=12, label='密码',
                               error_messages=
                               {'min_length': '最小6位',
                                'max_length': '最大12位',
                                'required': '密码不能为空'},
                               widget=forms.widgets.PasswordInput(attrs={'class': 'form-control c1 c2',

                                                                         'placeholder': "请输入密码，不少于6位",
                                                                         'aria-describedby': "sizing-addon1"
                                                                         }))
    confirm_password = forms.CharField(min_length=6, max_length=12, label='确认密码',
                                       error_messages=
                                       {'min_length': '最小6位',
                                        'max_length': '最大12位',
                                        'required': '密码不能为空'},
                                       widget=forms.widgets.PasswordInput(attrs={'class': 'form-control c1 c2',

                                                                                 'placeholder': "请确认密码",
                                                                                 'aria-describedby': "sizing-addon1"
                                                                                 }))
    email = forms.EmailField(label='邮箱', error_messages={'invalid': '邮箱格式不正确',
                                                         'required': '邮箱不能为空'},
                             widget=forms.widgets.TextInput(attrs={'class': 'form-control c1 c2',

                                                                   'placeholder': "请输入邮箱",
                                                                   'aria-describedby': "sizing-addon1"})
                             )

    # def clean_username(self):
    #     # 获取用户名
    #     username = self.cleaned_data.get('username')
    #     user = models.UserInfo.objects.filter(username=username).first()
    #     # 判断用户名是否存在
    #     if user:
    #         # 存在抛异常
    #         self.add_error('username', '用户已存在')
    #     return username

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not confirm_password == password:
            self.add_error('confirm_password', '两次密码不一致')
        return self.cleaned_data



class AddForm(forms.Form):
    date = forms.DateField(label='日期', widget=forms.DateInput(attrs={'type': 'date'}))


class SetPassForm(forms.Form):
    old_password = forms.CharField(min_length=6, max_length=12, label='密码',
                               error_messages=
                               {'min_length': '最小6位',
                                'max_length': '最大12位',
                                'required': '密码不能为空'},
                               widget=forms.widgets.PasswordInput(attrs={'class': 'form-control c1 c2',

                                                                         'placeholder': "请输入密码，不少于6位",
                                                                         'aria-describedby': "sizing-addon1"
                                                                         }))
    new_password = forms.CharField(min_length=6, max_length=12, label='确认密码',
                                       error_messages=
                                       {'min_length': '最小6位',
                                        'max_length': '最大12位',
                                        'required': '密码不能为空'},
                                       widget=forms.widgets.PasswordInput(attrs={'class': 'form-control c1 c2',

                                                                                 'placeholder': "请确认密码",
                                                                                 'aria-describedby': "sizing-addon1"
                                                                                 }))
    confirm_password = forms.CharField(min_length=6, max_length=12, label='确认密码',
                                   error_messages=
                                   {'min_length': '最小6位',
                                    'max_length': '最大12位',
                                    'required': '密码不能为空'},
                                   widget=forms.widgets.PasswordInput(attrs={'class': 'form-control c1 c2',

                                                                             }))

    def clean(self):
        password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not confirm_password == password:
            self.add_error('confirm_password', '两次密码不一致')
        return self.cleaned_data

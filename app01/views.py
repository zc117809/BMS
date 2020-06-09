from django.shortcuts import render,redirect,HttpResponse,reverse
from app01 import models
from django.contrib.auth.decorators import login_required
from app01 import forms
from  utls import pure
from django.contrib.auth.models import User

from django.contrib import auth
# Create your views here.


def login(request):
    login_form = forms.LoginForm()
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            # 通过用户名和密码查询用户是否存在
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user_obj = auth.authenticate(request,username=username,password=password)
            # 判断当前用户是否存在
            if user_obj:
                # 保存用户状态 ，就相当于session保存用户已经登录过的状态
                auth.login(request,user_obj)
                return redirect('index')
            msg = '用户名或密码不正确'
    return render(request,'login.html',locals())


def reg(request):
    reg_form = forms.RegForm()
    if request.method == 'POST':
        reg_form = forms.RegForm(request.POST)  # 表单验证

        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            password = reg_form.cleaned_data['password']
            email = reg_form.cleaned_data['email']
            User.objects.create_user(username=username,password=password)
            return redirect('login')
    return render(request, 'register.html', locals())


@login_required(login_url='/')
def set_password(request):
    setpassword_form = forms.SetPassForm()
    if request.method == 'POST':
        setpassword_form = forms.SetPassForm(request.POST)
        if setpassword_form.is_valid():
            old_password = setpassword_form.cleaned_data.get('old_password')
            new_password = setpassword_form.cleaned_data.get('confirm_password')
            # 在数据库中校验一下原来的密码输入是否正确
            is_right = request.user.check_password(old_password)
            if is_right:
                # 修改密码
                request.user.set_password(new_password)
                request.user.save()
            return redirect('login')
    return render(request,'set_password.html',locals())




@login_required(login_url='/')
def index(request,*args,**kwargs):

    return render(request,'index.html',locals())


@login_required(login_url='/')
def book_list(request):
    book_li = models.Book.objects.all()
    current_page = request.GET.get('page', 1)
    all_count = book_li.count()
    # 1 传值生成对象
    page_obj = pure.Pagination(current_page=current_page, all_count=all_count)
    # 2 直接对总数据进行切片操作
    page_queryset = book_li[page_obj.start:page_obj.end]


    return render(request, 'booklist.html', locals())


# 添加书籍
@login_required(login_url='/')
def book_add(request):
    add_form = forms.AddForm()
    publish_list = models.Publish.objects.all()
    author_list = models.Author.objects.all()
    if request.method == 'POST':
        # 获取前端提交过来的所有数据
        add_form = forms.RegForm(request.POST)  # 表单验证
        """

        """
        if add_form.is_valid():
            date = add_form.cleaned_data['date']
            title = request.POST.get("title")
            price = request.POST.get("price")
            # publish_date = request.POST.get("publish_date")
            publish_id = request.POST.get("publish")
            authors_list = request.POST.getlist("authors")  # [1,2,3,4,]
            # 操作数据库存储数据
            # 书籍表
            book_obj = models.Book.objects.create(title=title, price=price, publish_date=date,publish_id=publish_id)
            # 书籍与作者的关系表
            book_obj.authors.add(*authors_list)
            # 跳转到书籍的展示页面
        return redirect('book_list')
    # 先获取当前系统中所有的出版社信息和作者信息

    return render(request, 'add_book.html', locals())


# 编辑书籍
@login_required(login_url='/')
def edit_book(request, cc_id):
    publish_list = models.Publish.objects.all()
    author_list = models.Author.objects.all()
    edit_book_list = models.Book.objects.filter(pk=cc_id).first()
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')
        publish_id = request.POST.get('publish')
        author = request.POST.getlist('author')
        models.Book.objects.filter(pk=cc_id).update(title=title,price=price,publish_date=publish_date,publish_id=publish_id)
        edit_book_list.authors.set(author)
        return redirect('book_list')
    return render(request, 'edit_book.html',locals())


@login_required(login_url='/')
def book_delete(request,delete_id):
    models.Book.objects.filter(pk=delete_id).delete()
    return redirect('book_list')

@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return render(request,'index.html')



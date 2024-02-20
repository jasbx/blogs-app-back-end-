
from django.shortcuts import redirect, render
from django.contrib.auth import logout,login
from .models import *
from .filter import Oreder
from .form import *
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


# ====================================================================={display}
@login_required(login_url='login')
def blog(request):
    blog=Blogform()
    context={
        'blog':blog,
        'item':Blogse.objects.all()
    }
  

    return render (request,'blog.html',context=context)
# ========================================================================{create}
@login_required(login_url='login')
def writblog(request):
   if request.method=='POST':
        ti=request.POST.get('title')
        imge=request.POST.get('img')
        desc=request.POST.get('desc')
        dat=request.POST.get('date')
        blog_n=request.POST.get('name')
        savblog=Blogse(title=ti,discribtion=desc,date=dat,blog_name=blog_n,img=imge)
        savblog.save()


  
   return render (request,'blogswrite.html')
# ============================================================================{delete}
@login_required(login_url='login')
def delete_blog(request,pk):
    blogs=Blogse.objects.get(id=pk)
    if request.method=='POST':
        blogs.delete()


        
    contect={
        'iteblog':blogs
    }
    return render(request,'delete_blog.html',context=contect)
# ==============================================================[update]
@login_required(login_url='login')
def update(request,pk):
    blogs=Blogse.objects.get(id=pk)
    form=Blogform(instance=blogs)
    if request.method=='POST':
        form=Blogform(request.POST,instance=blogs)
        if form.is_valid():
            form.save()
         
    context={
        'form':form
    }
    return render (request,'update_blog.html',context=context)
from django.contrib import messages
# =======================================================================================
# {regestar}
def regs(request):
    form=Loginform()
    if request.method=='POST':
      form=Loginform(request.POST)
      if form.is_valid():
            form.save()
           
            messages.success(request,"create user succsessfully")
            return redirect('login')
    context={'form':form}
    return render (request,'regs.html',context=context)
# ===========================================================================================
# {login}
def login_user(request):
    if request.user.is_authenticated:
        return redirect('blog')
    else:
        form=Loginform()
        if request.method=='POST':

          username=request.POST.get('username')
          password=request.POST.get('password1')
          user=authenticate(request,username=username,password=password)
          form=Loginform(request.POST)
          if user is not None:
                login(request,user)
                return redirect('blog')
        else:
            messages.info(request,"the user or password not corecct")
        
        context={'form':form}
        return render (request,'login.html',context=context)
# ==============================================={logout}
def logout_user(request):
    logout(request)
    return redirect('login')


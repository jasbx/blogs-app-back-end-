from django.urls import path

from . import views

urlpatterns = [
  
    # ========={blog/update/write/delete}
    
    path('blogs',views.blog,name='blog'),
    path('delete/<str:pk>',views.delet,name='delete'),

    path('blogswrite',views.writblog,name='blogswrite'),
    path('delete_blog/<str:pk>',views.delete_blog,name='delete_blog'),
    path('update/<str:pk>',views.update,name='update'),
    # ========{login/logout/registar}
    path('',views.regs,name='regs'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    
]

from django.conf.urls import url
from user import views
# SET THE NAMESPACE!
app_name = 'user'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    # url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^accounts/login/$',views.user_login,name='user_login'),
    url(r'^special/',views.special,name='special'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^post/(?P<mid>[\w-]+)/$',views.post,name='post'),
    url(r'^shop/$',views.product,name='product'),
	url(r'^', views.index, name='index'),
]
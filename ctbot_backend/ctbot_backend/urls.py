#ctbot_backend/ctbot_backend/urls.py
from django.contrib import admin
from django.urls import path
from core.views import LoginView ,UserView , CSRFTokenView , API_verify , API_list , delete_API


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', LoginView.as_view(), name='login'),  # 定义 API 路由并将其指向对应的视图处理函数
    path('api/user/', UserView.as_view(), name='user'),
    path('csrf_token/', CSRFTokenView.as_view(), name='csrf_token'), # 添加获取 CSRF Token 的路由
    path('api/api_verify/',API_verify,name='api_verify'),
    path('api/api_list/',API_list,name='api_list'),
    path('api/delete_api/<str:tag>',delete_API,name='delete_api')
]

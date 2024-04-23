from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token
from django.contrib.auth.models import User
from binance.client import Client
from django.views import View
from .models import API
import logging

logger = logging.getLogger(__name__)

class CSRFTokenView(View):
    def get(self, request):
        csrf_token = get_token(request)
        return JsonResponse({'csrfToken': csrf_token})

class LoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # 用户验证成功，执行登录成功的逻辑
            login(request, user)
            return JsonResponse({'message': 'LoginV登录成功'})
        else:
            # 用户验证失败，执行登录失败的逻辑
            return JsonResponse({'message': '用户名或密码错误'}, status=400)

class UserView(View):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 获取当前登录用户的用户信息
        user = request.user
        return JsonResponse({
            'id': user.id,
            'username': user.username,
            # 其他用户信息字段
        })

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def API_verify(request):
    # 设置CORS头部
    response = HttpResponse()
    response["Access-Control-Allow-Origin"] = "*"  # 允许来自任何域的跨域请求
    response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"  # 允许的请求方法
    response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"  # 允许的请求头

    try:
        api_key = request.data.get('api_key')
        api_secret = request.data.get('api_secret')
        tag = request.data.get('tag')

        # 获取当前登录的用户
        user = request.user
        if user.is_authenticated:
            # 检查是否存在相同的api_key或api_secret或tag
            if API.objects.filter(api_key=api_key).exists() or \
                    API.objects.filter(api_secret=api_secret).exists() or \
                    API.objects.filter(tag=tag).exists():
                response.status_code = 400
                response.data = {'message': 'API密钥或标签已存在.'}
            else:
                # 初始化 Binance 客户端
                client = Client(api_key, api_secret)

                # 调用 Binance API，检查API密钥的状态和权限
                account_status = client.get_account_status()

                # 检查账户状态是否正常
                if account_status.get('data') == 'Normal':
                    # API Key 和 API Secret 有效，保存到数据库中
                    api = API.objects.create(user=user, api_key=api_key, api_secret=api_secret, tag=tag)
                    response.status_code = 200
                    response.content = {'message': 'API密钥有效并保存成功.'}
                else:
                    response.status_code = 400
                    response.content = {'message': 'API密钥状态异常.'}
        else:
            response.status_code = 401
            response.content = {'message': '用户未登录.'}
    except Exception as e:
        # 捕获所有异常，返回友好的错误消息
        error_message = '无法验证 API 密钥.'
        if hasattr(e, 'message'):
            error_message = str(e.message)
        logger.error(error_message, exc_info=True)
        response.status_code = 400
        response.content = {'message': error_message}

    return response

def API_list(request):
    try:
        # 获取当前登录的用户
        user = request.user
        if user.is_authenticated:
            # 获取该用户的所有API
            api_objects = API.objects.filter(user=user)
            
            # 构造API列表数据
            API_list = []
            for api_object in api_objects:
                api_data = {
                    'tag': api_object.tag,
                    'api_key': api_object.api_key,
                    'api_secret': api_object.api_secret,
                    'created_at': api_object.created_at,
                    
                    # 其他API信息字段
                }
                API_list.append(api_data)

            return JsonResponse({'API_list': API_list}, status=200)
        else:
            return JsonResponse({'message': '用户未登录'}, status=401)
    except Exception as e:
        # 捕获异常并返回错误消息
        error_message = '无法获取API列表'
        logger.error(error_message, exc_info=True)
        return JsonResponse({'message': error_message}, status=400)

def delete_API(request, tag):
    try:
        # 从数据库中获取要删除的 API 对象
        api = get_object_or_404(API, tag=tag)

        # 执行删除操作
        api.delete()

        # 返回成功的响应
        return JsonResponse({'message': 'API删除成功'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)    
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from authentication.views import *
from projects.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
 
router = routers.SimpleRouter()
router.register('user', UserRegisterView, basename='user')
router.register('project', ProjectView, basename='project')
router.register('issue', IssueView, basename='issue')
router.register('comment', CommentView, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls))
]
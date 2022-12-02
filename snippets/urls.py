from xml.dom.minidom import Document
from django.urls import path,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from snippets import views
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from snippets import views
from snippets.views import SnippetsUpdateView

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet,basename="snippets")
router.register(r'users', views.UserViewSet,basename="users")

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', include(router.urls)),
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('', include(router.urls)),
    path('snippets/<int:pk>/change/',SnippetsUpdateView.as_view()),
    path('snippets/<int:pk>/delete/',SnippetsUpdateView.as_view()),
    
]
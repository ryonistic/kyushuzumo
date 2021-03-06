from django.urls import path
from .views import AdmissionView, ContactView, PostList, PostDetail, ProList, UserDetail, UserList, ProDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
    path('pros/', ProList.as_view()),
    path('pros/<int:pk>/', ProDetail.as_view()),
    path('contact/', ContactView.as_view()),
    path('admission/', AdmissionView.as_view()),
]

from unicodedata import name
from django.urls import path, include
from .views import UserAddShowView, UserDeleteView, UserUpdateView

urlpatterns = [
    path('', UserAddShowView.as_view(), name='addshow'),
    path('update/<int:id>/', UserUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', UserDeleteView.as_view(), name='delete'),
    path('api/', include('enroll.api.urls'))
]

from django.urls import path
from .views import UserCreate, BlacklistTokenView

app_name = 'accounts'

urlpatterns = [
    path('register/', UserCreate.as_view(), name='create_user'),
    path('logout/blacklist/', BlacklistTokenView.as_view(), name='blacklist'),
]
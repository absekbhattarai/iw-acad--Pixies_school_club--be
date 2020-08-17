from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .students.views import GenericAPIView
from .views import ClubViewSet, home
from .accounts.views import AdminRegistrationView, StaffRegistrationView, MemberRegistrationView


r = DefaultRouter()
r.register('clubs,', ClubViewSet)



urlpatterns = [
    # path('clubs/', ClubViewSet.as_view,
    path('signup/admin/', AdminRegistrationView.as_view()),
    path('signup/staff/', StaffRegistrationView.as_view()),
    path('signup/member/', MemberRegistrationView.as_view()),
    path('login/', obtain_auth_token, name='login'),
    path('home/', home, name='home'),
    path('generic/member/',GenericAPIView.as_view()),
] + r.urls
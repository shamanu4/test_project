from django.urls import path
from .views import (
    NewUserByRefCodeView,
    AuthView,
    user_logout,
    UserProfileDetailView,
    VerificationFormView,
    VerificationDocumentLoaderView,
    VerificationsListView,
    VerificationUserDetailView,
    ChangeDirectionView,
)


app_name = 'user'
urlpatterns = [
    path('register-by-ref/<str:ref_code>/', NewUserByRefCodeView.as_view(), name='register-by-ref'),
    path('login/', AuthView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', UserProfileDetailView.as_view(), name='profile'),
    path('verification/', VerificationFormView.as_view(), name='verification'),
    path('verification/document-loader/', VerificationDocumentLoaderView.as_view(), name='verification-document-loader'),
    path('verification/users/', VerificationsListView.as_view(), name='verification-users'),
    path('verification/user/<int:pk>/', VerificationUserDetailView.as_view(), name='verification-user-detail'),
    path('change-direction/', ChangeDirectionView.as_view(), name='change-direction'),
]

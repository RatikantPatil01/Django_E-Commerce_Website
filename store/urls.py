from cProfile import Profile
from re import template
from django.contrib import admin
from django.urls import path
from store import views
from store.views.MyPasswordResetForm import MyPasswordResetForm
from store.views.profile import ProfileView
from . import views
from django.contrib.auth import views as auth_views
from .views.MySetPasswordForm import MySetPasswordForm

from store.views.profile import ProfileView
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.profile import ProfileView
from django.contrib import auth
from store.views.passwordchange import MyPasswordChangeForm

from store.views import passwordchange,profile



urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('profile/', ProfileView.as_view() , name='profile'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html' , form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

]

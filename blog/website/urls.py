from django.urls import path
from website import views

app_name = 'website'

urlpatterns = [
    path('', views.indexPage, name = 'index'),
    path('writterspage/<str:writter_slug>/', views.writtersPage, name = 'writterpage'),
    path('pubpage/<str:pub_slug>/', views.pubPage, name = 'pubpage'),
    path('resultpage/', views.resultPage, name = 'resultpage'),
    path('aboutus/', views.aboutusPage, name = 'aboutuspage'),
    path('user/', views.loginPage, name = 'loginpage'),
    path('user/user/', views.checkLogin),
    path('accounts/login/writterarea/postpub/', views.postPub, name = 'postpub'),
    path('accounts/login/writterarea/whatdo/', views.whatDo, name = 'whatdo'),
    path('accounts/login/writterarea/updatepub/<int:pub_id>/', views.updatePub, name = 'updatepub'),
]
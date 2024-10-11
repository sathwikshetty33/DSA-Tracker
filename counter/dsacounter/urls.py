   # urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views
urlpatterns = [
      path('',views.register,name='reg'), 
      path('login/',views.login_view,name='login'),
      path('logout/',views.logout_view,name='logout'),
      path('teacher-login/',views.teacherlogin,name='tlogin'),
      path('teacher-dashboard/',views.dashboard,name='dashboard'),
      path('logout/',views.logout_view,name='logout'),
      path('home/',views.home,name='home'),
      path('<str:username>-results/',views.results,name='results'),
      path('results-delete/<str:username>/<str:date>/<str:submittime>/', views.dele , name='dele'),
      path('room-delete-<int:roomid>/', views.roomdelete , name='roomdelete'),
      path('submissins-<int:roomid>/', views.submissions , name='submissions'),
      path('delte-<int:studentid>-from-<int:roomid>/', views.deletestudent , name='deletestudent'),
      path('exitclass-<int:userid>-from-<int:roomid>/', views.exitclass , name='exitclass'),
      path('myclasses-<int:userid>/', views.myclass , name='myclass'),

   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
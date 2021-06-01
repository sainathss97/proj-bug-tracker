from django.contrib import admin
from django.urls import path
from base import views
from django.conf import settings
from django.conf.urls.static import static
from base.views import Register, TaskList, TaskListView ,TaskCreate, TaskUpdate , TaskDelete, TaskLogin, TaskLogout, BugView,BugCreate,BugUpdate,BugDelete,BugList
urlpatterns = [
    path('task_list',TaskList.as_view(),name='home'),
    path('task-list/<int:pk>/', TaskListView.as_view(),name ='task-list'),
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
    #----------------------------------------------------------------------------------------------#
    path('login/',TaskLogin.as_view(),name='login'),
    path('logout/',TaskLogout.as_view(),name='logout'),
    path('register/',Register.as_view(),name='register'),
    #----------------------------------------------------------------------------------------------#
    path('',views.bug,name='index'),
    path('bug_list/<int:pk>/',BugView.as_view(),name='bug-list'),
    path('bug-create/',BugCreate.as_view(),name='bug-create'),
    path('bug-update/<int:pk>/',BugUpdate.as_view(),name='bug-update'),
    path('bug-delete/<int:pk>/',BugDelete.as_view(),name='bug-delete'),
    path('bug-home/',BugList.as_view(),name='bug-home'),

]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
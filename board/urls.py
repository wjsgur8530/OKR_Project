from django.urls import path

from . import views
from .views import *

app_name = 'boardapp'

urlpatterns = [


    path('<int:pk>/delete/', postdelete, name='postdelete'),

    path('test4/', test2.as_view(), name='test2'),

    path('delete/<int:pk>/', companypostdelete, name='companypostdelete'),

    path('delete/person/<int:pk>/', personalgoaldelete, name='personalgoaldelete'),

    path('delete/department/<int:pk>/', departmentpostdelete, name='departmentpostdelete'),

    path('delete/classification/<int:pk>/', classificationpostdelete, name='classificationpostdelete'),

    path('savetable', views.savetable, name='savetable'),

    path('timeline/',timeline,name='timeline'),

    path('',index, name='index')

]

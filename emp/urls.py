from django.urls import path
from . import views 

urlpatterns = [
    path('home/', views.emp_home, name='emp_home'),
    path('add-emp/', views.add_emp, name='add_emp'),
    path('delete-emp/<int:emp_id>', views.delete_emp, name='delete_emp'),
    path('update-emp/<int:emp_id>', views.update_emp, name='update_emp')
]

from django.urls import path
from .views import CreateRobotView, excel_table_view,hello_world

urlpatterns = [
    path('api/create_robot', CreateRobotView.as_view(), name='create-robot'),
    path('api/excel_table/', excel_table_view, name='excel-table'),
]
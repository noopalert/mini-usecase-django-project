from django.urls import path
from .views import (
    formView,
    DailyTransFormView
)

app_name = 'form'

urlpatterns = [
    path('',formView, name='home'),
    path('create/', DailyTransFormView.as_view(), name='formCreate')
]

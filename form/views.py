from django.shortcuts import render
from .formsDailyTrans import DailyTransForm
from django.views.generic import (
    CreateView,
)



def formView(request):
    context={
        'title': 'FORM'
    }
    return render(request, 'index.html', context)

class DailyTransFormView(CreateView):
    form_class = DailyTransForm
    template_name = 'form/formCreate.html'
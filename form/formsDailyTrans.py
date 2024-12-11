from django.forms import ModelForm
from .modelsDailyTrans import DailyTrans

class DailyTransForm(ModelForm):
    class Meta:
        model = DailyTrans
        fields =[
            'modes',
            'categories',
            'subcategories',
            'amounts',
            'types_transaction',
            'currency'
        ]

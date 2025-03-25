# from django import forms
# from .models import Bank
# from django import forms
# from django_countries import countries 

# class BankForm(forms.ModelForm):
#     class Meta:
#         model = Bank
#         fields = ["bank_code", "bank_name", "swift_ifsc_code", "state", "country", "remarks"]  

# class BankForm(forms.ModelForm):
#     country = forms.CharField(
#         widget=forms.TextInput(attrs={"list": "country-list"}),  # Adds dropdown + manual entry
#         required=True
#     )
#     class Meta:
#         model = Bank  # ✅ Make sure this is included
#         fields = ['bank_code', 'bank_name', 'swift_ifsc_code', 'state', 'country', 'remarks']
from django import forms
from .models import Bank, Country

class BankForm(forms.ModelForm):
    country = forms.CharField(
        label="Country",
        widget=forms.TextInput(attrs={'list': 'country-list', 'placeholder': 'Type or select a country'})
    )

    class Meta:
        model = Bank
        fields = ['bank_code', 'bank_name', 'swift_ifsc_code', 'state', 'country', 'remarks']

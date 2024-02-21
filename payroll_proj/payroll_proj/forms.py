from django import forms


class PayrollForm(forms.Form):
        name = forms.CharField(max_length=100)
        pay_rate = forms.FloatField()
        hours_worked = forms.FloatField()

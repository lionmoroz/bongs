from django import forms

class CouponAplyForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput())
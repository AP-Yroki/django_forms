from django import forms
from .models import News


class UserForm(forms.Form):
    name = forms.CharField()
    second_name = forms.CharField()
    email = forms.CharField()
    country = forms.CharField()
    city = forms.CharField()
    street = forms.CharField()
    home_num = forms.IntegerField()
    home = forms.IntegerField()

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'image', 'published', 'pub_date']
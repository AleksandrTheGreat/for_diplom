from django import forms

class Form_Help(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=20)
    pochta = forms.EmailField(label='Ваша эл.почта')
    message = forms.CharField(label='Ваше сообщение', widget=forms.Textarea())
from django import forms


class ContactForm(forms.Form):
    sub = forms.CharField(widget=forms.TextInput(attrs={'class': "col-md-3 control-label"}), max_length=150)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "col-md-3 control-label"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))



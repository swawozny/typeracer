from django import forms

from news.models import Post


class JoinForm(forms.Form): # or forms.ModelForm
    email = forms.EmailField()
    name = forms.CharField(max_length=120)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email == "abc@gmail.com":
            raise forms.ValidationError("this is not valid")
        return email
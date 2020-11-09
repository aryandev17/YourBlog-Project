from django import forms

class ImageForm(forms.Form):
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={"hidden":True}))
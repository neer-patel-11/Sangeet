from django import forms
from .models import Users

class UserForm(forms.ModelForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = Users
        fields = "__all__"

    # def save(self, commit=True):
    #     user = super(UserForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from seniorapp.models import Student

class StudentCreationForm(UserCreationForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ('academic_id', 'name','cpr','gpa','college','department','course')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# class StudentCreationForm(UserCreationForm):

#     class Meta(UserCreationForm.Meta):
#         model = Student
#         fields = Student.Meta


class StudentLoginForm(forms.Form):
    academic_id = forms.CharField(label='Academic ID', max_length=8)
    password = forms.CharField(widget=forms.PasswordInput(),max_length=32)

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BaseForm(forms.ModelForm):
    """Base form to provide common styling for fields"""
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
            field.label = ''
            if isinstance(field, forms.EmailField):
                field.widget.attrs['placeholder'] = 'E-mail Address'

class SignUpForm(BaseForm, UserCreationForm):
    """Form for creating new users with additional styling"""
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # Additional customization if needed

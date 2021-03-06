from django import forms

from account import models


class SignUpForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=150, required=True)

    class Meta():
        model = models.User
        fields = ('email', 'first_name', 'last_name', 'username', 'password', 'password2', 'phone')


    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['password2']:
                raise forms.ValidationError('Password do not match')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = False
        user.save()

        activation_code = user.activation_codes.create()
        activation_code.send_activation_code()
        return user


class SignUpSMSForm(SignUpForm):

    def save(self, commit=True):
        user = super(forms.ModelForm, self).save(commit=False)  # no save to database
        user.set_password(self.cleaned_data['password'])  # password should be hashed!
        user.is_active = False  # user cannot login
        user.save()

        sms_code = user.sms_codes.create()
        sms_code.send_sms_code()
        return user


class ActivateForm(forms.Form):
    sms_code = forms.CharField()


# class CommentForm(forms.ModelForm):
#     text = forms.Textarea()


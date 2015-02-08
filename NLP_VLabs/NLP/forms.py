from django import forms            
from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm     

class RegistrationForm(UserCreationForm):

    email = forms.EmailField(label='Email',)
    institute = forms.CharField(label='Institute', max_length=200)
    course = forms.CharField(label='Course', max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')   

    def save(self,commit = True):   
        user = super(RegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.institute = self.cleaned_data['institute']
        user.course = self.cleaned_data['course']

        if commit:
            user.save()

        return user

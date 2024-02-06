from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import DeathReg, User
from .models import Customer,Address,Regcenter

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"enter your username"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"enter your password"
            }
        )
    )


class SignUpForm(UserCreationForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('gender',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.gender = self.cleaned_data['gender']
        if commit:
            user.save()
        return user
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Enter name"
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Enter surname"
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Enter Username"
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Enter password"
            }
        )
    )

    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"confirm password"
            }
        )
    )

    
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Enter Email"
            }
        )
    )


    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','gender','password1','password2','is_admin','is_employee')

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name','middle_name','last_name','email','gender','dob','registered_date','fathername','mothername','address','district','city','region','religion','contact','height','citizenship','photo']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control shadow-none mb-3'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control shadow-none mb-3'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control shadow-none mb-3'}),
            'email': forms.EmailInput(attrs={'class': 'form-control shadow-none mb-3'}),
            'gender': forms.Select(attrs={'class': 'form-control shadow-none mb-3'}),
            'dob': forms.DateInput(attrs={'type': 'date','class': 'form-control shadow-none mb-3'}),
            'registered_date': forms.DateInput(attrs={'type': 'date','class': 'form-control shadow-none mb-3'}),
            'fathername': forms.TextInput(attrs={'class': 'form-control shadow-none mb-3'}),
            'mothername': forms.TextInput(attrs={'class': 'form-control shadow-none mb-3'}),
            'address': forms.TextInput(attrs={'class': 'form-control shadow-none mb-3'}),
            'district': forms.Select(attrs={'class': 'form-control shadow-none mb-3'}),
            'city': forms.Select(attrs={'class': 'form-control shadow-none mb-3'}),
             'religion': forms.Select(attrs={'class': 'form-control shadow-none mb-3'}),
            'region': forms.Select(attrs={'class': 'form-control shadow-none mb-3'}),
            'contact': forms.TextInput(attrs={'class': 'form-control shadow-none mb-3'}),
            'height': forms.TextInput(attrs={'class': 'form-control shadow-none mb-3'}),
            'citizenship': forms.TextInput(attrs={'class': 'form-control shadow-none mb-3'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file shadow-none mb-3'}),   
            }
        

# nin form
class NINForm(forms.Form):
    nin = forms.CharField(label='National Identification Number', max_length=7)



# death form
class DeathForm(forms.ModelForm):
    class Meta:
        model = DeathReg
        fields = ['first_name','middle_name','last_name','gender','date_of_death','cause_of_death','time_of_death','address','district','city','age','registered_date','photo']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control shadow-none mb-3'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control shadow-none mb-3'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control shadow-none mb-3'}),
            'gender': forms.Select(attrs={'class': 'form-control shadow-none mb-3'}),
            'date_of_death': forms.DateInput(attrs={'class': 'form-control shadow-none mb-3', 'type': 'date'}),
            'cause_of_death': forms.TextInput(attrs={'class': 'form-control shadow-none mb-3'}),
            'time_of_death': forms.TimeInput(attrs={'class': 'form-control shadow-none mb-3', 'type': 'time'}),
            'address': forms.TextInput(attrs={'class': 'form-control shadow-none mb-3'}),
            'district': forms.Select(attrs={'class': 'form-control shadow-none mb-3'}),
            'city': forms.Select(attrs={'class': 'form-control shadow-none mb-3'}),
            'age': forms.NumberInput(attrs={'class': 'form-control shadow-none mb-3', 'min': 1, 'max': 150}),
            'registered_date': forms.DateInput(attrs={'class': 'form-control shadow-none mb-3', 'type': 'date'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control shadow-none mb-3'}),
        }
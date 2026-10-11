from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
)

from .models import (
    CustomUser,
    ContactMessage,
    Profile,
    Skill,
    Education,
    Experience,
    Project,
)


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )

    profile_picture = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
    )

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'profile_picture',
            'password',
            'confirm_password',
        ]

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_picture',
            'description',
            'bio',
            'phone_number',
            'address',
            'github_link',
            'linkedin_link',
            'birth_date',
        ]

        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),

            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Bio'
            }),

            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Address'
            }),

            'github_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'GitHub Link'
            }),

            'linkedin_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'LinkedIn Link'
            }),

            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }),

            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject'
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message',
                'rows': 5
            }),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Skill Name'
            }),

            'proficiency': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Proficiency (0-100)'
            }),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = [
            'degree',
            'institution_name',
            'passed_out_year',
            'results'
        ]

        widgets = {
            'degree': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Degree'
            }),

            'institution_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Institution Name'
            }),

            'passed_out_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Passed Out Year'
            }),

            'results': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Results'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        passed_out_year = cleaned_data.get('passed_out_year')

        if passed_out_year and (
            passed_out_year < 1900 or passed_out_year > 2100
        ):
            raise forms.ValidationError(
                "Please enter a valid year between 1900 and 2100."
            )

        return cleaned_data


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = [
            'company_name',
            'job_title',
            'start_date',
            'end_date',
            'description',
            'current_job'
        ]

        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company Name'
            }),

            'job_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Job Title'
            }),

            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Start Date',
                'type': 'date'
            }),

            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'End Date',
                'type': 'date'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description',
                'rows': 5
            }),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'technologies_used',
            'github_link'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Project Title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Project Description',
                'rows': 5
            }),

            'technologies_used': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Technologies Used'
            }),

            'github_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'GitHub Link'
            }),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username or Email'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

    def clean(self):
        username_or_email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username_or_email and password:
            if '@' in username_or_email:
                try:
                    user = CustomUser.objects.get(
                        email=username_or_email
                    )
                    username = user.username
                except CustomUser.DoesNotExist:
                    raise forms.ValidationError(
                        "Invalid email or password."
                    )
            else:
                username = username_or_email

            self.cleaned_data['username'] = username

        return super().clean()


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Old Password'
        })
    )

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'New Password'
        })
    )

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm New Password'
        })
    )

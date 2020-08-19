from django.forms import ModelForm

from administration.models import User, UserProfile


class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'image')

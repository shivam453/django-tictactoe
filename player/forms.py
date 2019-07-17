from django.forms import ModelForm # A form based on a Django Model
from .models import Invitation

# documentation link: https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/


class InvitationForm(ModelForm):  # Inherit from ModelForm class
    class Meta:
        model = Invitation  # Model that we want to generate a form for
        exclude = ('from_user', 'timestamp')  # Model fields to leave out of form

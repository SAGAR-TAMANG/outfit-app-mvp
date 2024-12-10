from django import forms
from user_auth.models import UserProfile

class UserProfileForm(forms.ModelForm):
    MEASUREMENT_CHOICES = [
        ('chest', 'Chest'),
        ('waist', 'Waist'),
        ('hips', 'Hips'),
        ('shoulders', 'Shoulders'),
        ('legs', 'Legs'),
    ]  # Checklist options for measurements

    price_range = forms.IntegerField()

    measurements = forms.MultipleChoiceField(
        choices=MEASUREMENT_CHOICES,
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = UserProfile
        fields = ['brand_preferences', 'price_range', 'measurements']

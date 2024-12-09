from django import forms
from user_auth.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['brand_preferences', 'price_range', 'measurements']
        widgets = {
            'brand_preferences': forms.TextInput(attrs={
                'placeholder': 'Enter your preferred brands (e.g., Nike, Adidas)',
                'class': 'form-control mb-2',
            }),
            'price_range': forms.TextInput(attrs={
                'placeholder': 'Enter your price range (e.g., $50-$100)',
                'class': 'form-control mb-2',
            }),
            'measurements': forms.TextInput(attrs={
                'placeholder': 'Enter your measurements (e.g., {"chest": 38, "waist": 32})',
                'class': 'form-control mb-2',
            }),
        }

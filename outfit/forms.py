from django import forms
from user_auth.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['brand_preferences', 'price_range', 'measurements', 'preference']
    
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        
        # Initialize brand_preferences to be displayed as checkboxes
        self.fields['brand_preferences'].widget = forms.CheckboxSelectMultiple()
        
        # Initialize measurements fields to be displayed as dropdowns
        self.fields['measurements'] = forms.MultipleChoiceField(
            choices=[('chest', 'Chest'), ('waist', 'Waist'), ('hips', 'Hips'), 
                     ('shoulders', 'Shoulders'), ('legs', 'Legs')],
            widget=forms.Select()
        )

        # Initialize preference field to be displayed as a slider
        self.fields['preference'] = forms.ChoiceField(
            choices=[(1, 'Tight'), (2, 'Slim'), (3, 'Regular'), (4, 'Loose'), (5, 'Oversized')],
            widget=forms.Select()
        )
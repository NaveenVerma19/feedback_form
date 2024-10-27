from django.forms import ModelForm
from .models import *


class TourFeedbackform(ModelForm):
    class Meta:
        model = TourFeedback
        fields = '__all__'
        
        
# class ReviewRatingForm(ModelForm):
#     class Meta:
#         model = ReviewRating
#         fields = ['subject', 'review', 'rating']

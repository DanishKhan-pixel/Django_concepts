from django import forms

class FeedbackFrom(forms.Form):
    email=forms.EmailField(label="Enter your email",max_length=100)
    name=forms.CharField(label="Enter your name ",max_length=100)
    feedback=forms.CharField(label="Enter your feedback",widget=forms.Textarea)
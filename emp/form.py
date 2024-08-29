from django import forms

class FeedbackFrom(forms.Form):
    email=forms.EmailField(label="Enter your email",max_length=100)
    name=forms.CharField(label="Enter your name ",max_length=100)
    feedback=forms.CharField(label="Enter your feedback",widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(FeedbackFrom, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
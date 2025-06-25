from .models import Question, Testimonial
from portfolio.models import Skill
from django.forms import ModelForm
from portfolio.models import Photo


class FaqForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FaqForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        exclude = ['created_at']
    
    def __init__(self, *args, **kwargs):
        super(TestimonialForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ['created_at']

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})   
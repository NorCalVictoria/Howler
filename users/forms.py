from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, PostContent

					#	blogPro/postApp/models.py  import this into forms for Post class

class ContactForm(forms.Form):
	
	name = forms.CharField()
	email = forms.EmailField(label='E-Mail')
	category = forms.ChoiceField(choices=[('question', 'Choose'), ('other', 'Other')])
	subject = forms.CharField(required=False)
	body = forms.CharField(widget=forms.Textarea)


def __init__(self, *args, **kwargs):
	super().__init__(*args, **kwargs)

	self.helper = FormHelper
	self.helper.form_method = "post"

	self.helper.layout = Layout(
		"name",
		"email",
		"category",
		"subject",
		"body",
		Submit('submit', "Submit", css_class='btn-success')
		)
		
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']

class PostForm(forms.ModelForm):   ######### video upload ##########
	class Meta:
		model = Post
		fields = ['name','clip','image']  # fields=["name", "clip"]    <--- alt.


class ImageForm(forms.ModelForm):
	class Meta:
		model = PostContent
		fields = ['imagePost','author']
		
	







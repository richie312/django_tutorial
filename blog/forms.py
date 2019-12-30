from django import forms 
from django.forms import ModelForm
from .models import BlogPost
from django.contrib.auth.decorators import login_required

class BlogPostForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	content = forms.CharField(widget=forms.Textarea)

# Create the form class.
class BlogPostModelForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title','slug','content']
	def clean_title(self,*args,**kwargs):
		title = self.cleaned_data.get('title')
		qs = BlogPost.objects.filter(title_iexact = title)
		if qs.exists():
			raise forms.ValidationError("The title already exists. Please chose another title.")
		return title
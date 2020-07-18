from django import forms ### video ####
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (   # generic == class 
     ListView, 
     DetailView, 
     CreateView,
     UpdateView,
     DeleteView
)
from .models import Post
# from django.http import HttpResponse
from users.forms import ContactForm


def indexLand(request):					# function based view

	return render(request, 'postApp/landing.html')


def home(request):						# function based view
	context = {
	'posts': Post.objects.all()
	}
	return render(request, 'postApp/home.html', context, {'title': 'Home'})


def about(request):

	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']

			print(name, email)


	form = ContactForm()


	return render(request, 'postApp/about.html', {'form': form})
	# return render(request, 'postApp/about.html', {'title': 'About'})  # before



class PostListView(ListView): 
	model = Post
	template_name = 'postApp/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 3

class UserPostListView(ListView): 
	model = Post
	template_name = 'postApp/user_posts.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	
	paginate_by = 4

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):     # postApp/Post_Detail
	model = Post 





class PostCreateView(LoginRequiredMixin, CreateView):

	model = Post
	fields = ['title', 'content', 'clip'] 
	# return render(request, 'TEMPLATE for NEW POST.html', {'form': form})
	
	def form_valid(self, form):
		image = self.get_object()
		template_name = 'auth/post_form.html'
		form.instance.author = self.request.user
		return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, Post):
	model = Post
	fields = ['title', 'content', 'clip']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
																	##### upload video #### working
	def test_func(self):
		post = self.get_object()
		
		if self.request.user == post.author:
			return True
		return False
	# def get_object(self):
	# 	return self.request.user.image #????????????

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):     
	model = Post 
	success_url = '/post/new/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False



# class PostForm(forms.ModelForm, CreateView):   ######### video upload ##########
# 	class Meta:
# 		model = Post
# 		fields = '__all__'








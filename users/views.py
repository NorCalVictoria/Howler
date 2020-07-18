from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm### video ###


def register(request):				#create a form that will be passed to html template
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)	# class that will get converted to html
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! Please log in')
			return redirect('login') 
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

# options for message :
# 	messages.debug
# 	messages.info
# 	messages.success
# 	messages.warning
# 	messages.error
@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, 
									request.FILES, 
									instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated.')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'users/profile.html', context)

# def post_new(request):						####### video upload  ############
# 	if request.method == "POST":
# 		form = PostForm (request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('')  # FIXX where to ???
# 	else:
# 		form = PostForm()
# 	return render(request, 'users/post_edit.html', {'form': form}) # FIXX ?
# 							#user ?					context ^

# def showvideo(request):
#   lastvideo= Post.objects.last()  ##### video upload ##### alt.
#   clip = lastvideo.clip

#   form = VideoForm(request.POST or None, request.FILES or None)

#   if form.is_valid():
# 	  form.save()
#   context= {'clip': clip,
#        'form': form
# 	   }
#   return render(request, 'video.html', context)  ## FIX ??? create html page ##




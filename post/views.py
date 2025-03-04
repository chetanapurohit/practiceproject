from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import SignupForm, PostForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Post

# from .models import CustomUser


class SignupView(TemplateView):
    template_name = "post/signup.html"

    def get(self, request):
        form = SignupForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, "Signup successful! You can now log in.")
            return redirect('login')
        return render(request, self.template_name, {'form': form})
    # def post(self, request):
    #     fm = SignupForm(request.POST)
    #     password = request.POST.get('password')
    #     if fm.is_valid():
    #         user = fm.save()
    #         user.set_password(password)
    #         user.save()
    #         messages.success(request, "Signup successful! You can now log in.")
    #         return redirect('login')
    #     return render(request, self.template_name, {'form': fm})


class LoginView(TemplateView):
    template_name = 'post/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("valid")

            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)

            if user is not None:
                print('uer')
                login(request, user)
                messages.success(request, "Login successful! Redirecting to profile...")
                return redirect('home')
            else:
                form.add_error(None, "Invalid email or password.")
            return render(request, self.template_name, {'form': form})


class ProfileView(TemplateView):
    template_name = 'post/profile.html'


class LogoutView(TemplateView):
    def get(self, request):
        logout(request)
        return redirect('login')


class BlogPostView(TemplateView):
    template_name = 'post/createblog.html'

    def get(self, request):
        post_form = PostForm()
        return render(request, self.template_name, {'form': post_form})

    def post(self, request):
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, "Successful! Created Post")
            return redirect('home')
        
        return render(request, self.template_name, {'form': post_form})


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'post/home.html'
    login_url = 'login'

    def get(self, request):
        posts = Post.objects.all().order_by('created_at')
        return render(request, self.template_name, {'posts': posts})

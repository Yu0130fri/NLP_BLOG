from .models.profile_models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .forms import UserCreationForm, ProfileForm
from blog.models import PostArticle


def index(request):
    obj = PostArticle.objects.all()[:3]
    return render(request, 'index.html', context={
        'articles': obj
    })

class Login(LoginView):
    """
    function of Login
    """
    template_name = 'login/auth.html'

    def form_valid(self, form):
        messages.success(self.request, 'ログイン完了')

        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'ログインエラー')

        return super().form_invalid(form)


def signup(request):

    if request.POST:
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # user.is_activate = False
            user.save()

            login(request, user)

            messages.success(request, '登録完了しました！')

            return redirect('/')

    return render(request, 'login/auth.html')

@login_required
def mypage(request):

    if request.POST:
        form = ProfileForm(request.POST)
        
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, '更新完了')

    return render(request, 'mypage.html')
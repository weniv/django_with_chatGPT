from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm

# from django.contrib.auth.models import User
# from django.conf import settings => settings.AUTH_USER_MODEL

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm  # 추가

User = get_user_model()


def login_view(request):
    # 로그인 뷰
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main:index")
        else:
            # 에러 메시지 반환
            pass
    else:
        form = AuthenticationForm()  # 폼 인스턴스 생성
    return render(request, "accounts/login.html", {"form": form})  # 폼을 템플릿에 전달


def logout_view(request):
    # 로그아웃 뷰
    logout(request)
    return redirect("main:index")


def signup_view(request):
    # 회원가입 뷰
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("main:index")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})


@login_required
def profile_view(request, id):
    # 해당 ID를 가진 사용자를 조회
    user = get_object_or_404(User, pk=id)

    # 추가적으로, 사용자의 프로필 정보나 관련 데이터를 불러올 수 있습니다.
    # 예: user_profile = UserProfile.objects.get(user=user)
    # 이 경우 UserProfile은 사용자의 추가 정보를 담는 모델이 될 수 있습니다.

    # 사용자 정보와 함께 템플릿 렌더링
    return render(request, "accounts/profile.html", {"user": user})

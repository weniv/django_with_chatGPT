from django.shortcuts import render


def index(request):
    # 메인 페이지 뷰
    return render(request, "main/index.html")

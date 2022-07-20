from django.shortcuts import render

# Create your views here.

"""
ここではdef index( )という関数を作っていますよね。
そしてこの関数はrequestを引数にとっています。
requestとは、ユーザーがURLを入力してサーバーにアクセスする時に送られる情報のことです。
requestには、例えばログインしている人のユーザー情報などの様々な情報が含まれています。
"""
def index(request):
    return render(request, 'blogs/index.html')
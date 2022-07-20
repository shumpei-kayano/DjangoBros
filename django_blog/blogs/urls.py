"""
1行目では、DjangoのURL機能であるpath関数をインポートしています。
2行目のfrom . import viewsという部分では、同じ階層にあるviews.pyファイルをインポートしています。
ドットは、同じ階層という意味です。
"""
from django.urls import path
from . import views

"""
path関数では、第一引数で空の文字列を指定し、第二引数で、views.indexを指定することで、
URL（http://127.0.0.1:8000/）にアクセスした時は、views.pyのindex関数を実行するように設定をしています。
例えば、ここをpath('top/', views.index, name='index')のように書き換えたとすると、
URL（http://127.0.0.1:8000/top）にアクセスしたときにindex関数が実行されることになります。
このように、第一引数ではURLのパスを設定しています。
第三引数のname='index'という部分は、このURLパスに名前をつけてあげています。
"""
app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
]
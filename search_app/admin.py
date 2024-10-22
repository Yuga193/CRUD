from django.contrib import admin
from .models import Product  # models.py から Product モデルをインポート

admin.site.register(Product)  # 管理画面で Product モデルを表示できるようにする

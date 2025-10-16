from django.urls import path
from .views import (
    WargaListView,
    WargaDetailView,
    PengaduanListView,
    WargaCreateView,
    PengaduanCreateView,  # ✅ tambahkan ini
)

urlpatterns = [
    path('', WargaListView.as_view(), name='warga_list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga_detail'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan_list'),  
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),  # ✅ tambahkan ini
]

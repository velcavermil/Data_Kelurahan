from django.shortcuts import render
from .models import Warga, Pengaduan
from django.urls import reverse_lazy
from .forms import WargaForm, PengaduanForm
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
    )
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import WargaSerializer, PengaduanSerializer
from rest_framework import viewsets # Impor viewsets
from .models import Warga, Pengaduan

# Create your views here.
class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga

class PengaduanListView(ListView):
    model = Pengaduan

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga_list')

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = '/warga/pengaduan/'

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga_list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga_list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    fields = ['judul', 'deskripsi', 'status']
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan_list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan_list')

#class WargaListAPIView(ListAPIView):
   # queryset = Warga.objects.all()
   # serializer_class = WargaSerializer

#class WargaDetailAPIView(RetrieveAPIView):
    #queryset = Warga.objects.all()
    #serializer_class = WargaSerializer

#class PengaduanListAPIView(ListAPIView):
   # queryset = Pengaduan.objects.all()
   # serializer_class = PengaduanSerializer

#class PengaduanDetailAPIView(RetrieveAPIView):
  #  queryset = Pengaduan.objects.all()
   # serializer_class = PengaduanSerializer

class WargaViewSet(viewsets.ModelViewSet):

    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer  
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']

class PengaduanViewSet(viewsets.ModelViewSet):

    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['juudl', 'deskripsi']
    ordering_fields = ['judul', 'tanggal_lapor']
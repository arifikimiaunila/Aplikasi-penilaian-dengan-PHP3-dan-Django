from django.shortcuts import render, redirect
from .models import NilaiSiswa # type: ignore
from .forms import NilaiSiswaForm # type: ignore

def index(request):
    # Mengambil semua data nilai untuk ditampilkan di tabel
    daftar_nilai = NilaiSiswa.objects.all()
    
    if request.method == 'POST':
        form = NilaiSiswaForm(request.POST)
        if form.is_index_valid := form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NilaiSiswaForm()
        
    context = {
        'daftar_nilai': daftar_nilai,
        'form': form
    }
    return render(request, 'penilaian/index.html', context)
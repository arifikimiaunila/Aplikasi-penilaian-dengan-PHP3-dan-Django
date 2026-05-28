from django import forms
from .models import NilaiSiswa

class NilaiSiswaForm(forms.ModelForm):
    class Meta:
        model = NilaiSiswa
        fields = ['nim', 'nama', 'mata_kuliah', 'nilai_1', 'nilai_2', 'nilai_3']
        widgets = {
            'nim': forms.TextInput(attrs={'class': 'form-control'}),
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'mata_kuliah': forms.TextInput(attrs={'class': 'form-control'}),
            'nilai_1': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'nilai_2': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'nilai_3': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
        }
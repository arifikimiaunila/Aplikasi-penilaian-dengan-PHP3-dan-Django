from django.db import models

class NilaiSiswa(models.Model):
    nim_matakul = models.CharField(max_length=30, primary_key=True, editable=False)
    nim = models.CharField(max_length=15)
    nama = models.CharField(max_length=100)
    mata_kuliah = models.CharField(max_length=100)
    nilai_1 = models.FloatField(default=0)
    nilai_2 = models.FloatField(default=0)
    nilai_3 = models.FloatField(default=0)
    rata_rata = models.FloatField(editable=False, blank=True, null=True)
    keterangan = models.CharField(max_length=20, editable=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        # 1. Generate nim_matakul (NIM + 3 huruf pertama Matkul dicapitalize)
        kode_matkul = self.mata_kuliah.replace(" ", "")[:3].upper()
        self.nim_matakul = f"{self.nim}_{kode_matkul}"

        # 2. Hitung Rata-rata
        self.rata_rata = round((self.nilai_1 + self.nilai_2 + self.nilai_3) / 3, 2)

        # 3. Tentukan Keterangan (Contoh standar kelulusan: 65)
        if self.rata_rata >= 65:
            self.keterangan = "LULUS"
        else:
            self.keterangan = "TIDAK LULUS"

        super(NilaiSiswa, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nim_matakul} - {self.nama}"
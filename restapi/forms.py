from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(max_length=80)
    email = forms.EmailField()
    lokasi_pemasangan_node = forms.CharField(widget=forms.Textarea)
    penanggung_jawab_pemasangan = forms.CharField(max_length=100)
    no_telp_penanggung_jawab = forms.CharField(max_length=30)
    tanggal_pemasangan_node = forms.CharField(max_length=100)
    sensor_yang_digunakan_pada_node = forms.CharField(widget=forms.Textarea)

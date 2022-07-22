from django.db import models
from django.urls import reverse

# Create your models here.

class Anagrafica(models.Model):
    codottico = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 50)
    indirizzo = models.CharField(max_length = 50)
    citta = models.CharField(max_length = 50)
    provincia = models.CharField(max_length = 2)
    cap = models.CharField(max_length = 5)
    nome2 = models.CharField(max_length = 50, blank=True)
    indirizzo2 = models.CharField(max_length = 50, blank=True)
    citta2 = models.CharField(max_length = 50, blank=True)
    provincia2 = models.CharField(max_length = 2, blank=True)
    cap2 = models.CharField(max_length = 5, blank=True)
    telefono = models.CharField(max_length = 10, blank=True)
    cellurare = models.CharField(max_length = 10, blank=True)
    codice_fiscale = models.CharField(max_length = 16)
    p_iva = models.CharField(max_length = 11)
    sconto_gen = models.CharField(max_length = 2, default = "0")
    cod_pag = models.CharField(max_length = 10)
    pagamento = models.CharField(max_length = 50)
    banca = models.CharField(max_length = 50)
    iban = models.CharField(max_length = 27)
    abi = models.CharField(max_length = 5,  blank=True)
    cab = models.CharField(max_length = 5,  blank=True)
    fa = models.CharField(max_length = 50,  blank=True)
    spedizione = models.CharField(max_length = 50)
    pagcorr = models.CharField(max_length = 50)
    note = models.CharField(max_length = 50,  blank=True)
    data_registrazione = models.DateField(auto_now_add=True)
    codcpa = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50,  blank=True)
    pec = models.EmailField(max_length = 50,  blank=True)
    applicatore =  models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.codottico} - {self.nome}"

    def get_absolute_url(self):
        return reverse("anagrafica:anagrafica-detail", kwargs={"id":self.codottico})
    
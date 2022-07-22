from django import forms
from .models import Anagrafica

# from .models import Anagrafica

class AnagraficaModelForm(forms.ModelForm):
    class Meta:
       model = Anagrafica
       fields = [
        "nome", "indirizzo", "citta", "provincia", "cap", "nome2",
        "indirizzo2", "citta2", "provincia2", "cap2", "telefono",
        "cellurare", "codice_fiscale", "p_iva", "sconto_gen",
        "pagamento", "banca", "iban", "abi", "cab", "fa", "spedizione",
        "pagcorr", "note", "codcpa", "email", "pec", "applicatore"
        ]
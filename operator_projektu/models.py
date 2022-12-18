from django.db import models

# Create your models here.


class OperatorProjektu(models.Model):
    nazwa = models.CharField(max_length=200)
    adres = models.CharField(max_length=200)
    numer_kontaktowy = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nazwa


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nazwa


class Inicjatywa(models.Model):
    kategoria = models.ForeignKey(Kategoria, on_delete=models.SET_NULL, null=True)
    operator = models.ForeignKey(OperatorProjektu, on_delete=models.SET_NULL, null=True)
    nazwa = models.CharField(max_length=50)
    opis = models.TextField(null=True)
    data_rozpoczecia = models.CharField(max_length=20)
    liczba_miejsc = models.IntegerField(null=True)
    lokalizacja = models.CharField(max_length=250)


class Uzytkownik(models.Model):
    username = models.CharField(max_length=50)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    email = models.EmailField()
    numer_tel = models.CharField(max_length=11)
    def __str__(self) -> str:
        return self.username


class Uczestnik(models.Model):
    uzytkownik = models.ForeignKey(Uzytkownik, on_delete=models.SET_NULL, null=True)
    inicjatywa = models.ForeignKey(Inicjatywa, on_delete=models.SET_NULL, null=True)
    zaakceptowany = models.BooleanField(default=False)
    opis_siebie = models.TextField(null=True)
    cv = models.BinaryField(null=True)

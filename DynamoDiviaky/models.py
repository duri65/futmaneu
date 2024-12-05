from django.db import models
from django.contrib.auth.models import User


class Timy(models.Model):
    id =models.AutoField(primary_key=True, unique=True)
    skratka = models.CharField(max_length=5, verbose_name="Skratka", unique = True)
    nazov = models.CharField(max_length=50, verbose_name="Názov")
    start_jesen = models.DateField(verbose_name="Dátum", null=True)
    koniec_jesen = models.DateField(verbose_name="Dátum",  null=True)
    start_jar = models.DateField(verbose_name="Dátum",  null=True)
    koniec_jar = models.DateField(verbose_name="Dátum",  null=True)

    def __str__(self):
        return self.nazov

class Sutaze(models.Model):
    id =models.AutoField(primary_key=True)
    nazov = models.CharField(max_length=60,verbose_name="Názov")
    zvaz = models.CharField(max_length=80,verbose_name="Zväz")

class HraciePlochy(models.Model):
    id =models.AutoField(primary_key=True)
    nazov = models.CharField(max_length=50,verbose_name="Názov")
    umiestnenie = models.CharField(max_length=80,verbose_name="Miesto")

    def __str__(self):
        return f"{self.nazov}"


class TypZapasu(models.Model):
    id =models.AutoField(primary_key=True)
    nazov = models.CharField(max_length=50,verbose_name="Názov")

    def __str__(self):
        return f"{self.nazov}"

class Zaujem(models.Model):
    nazov = models.CharField(max_length=50,verbose_name="Záujem")

    def __str__(self):
        return f"{self.nazov}"


class Rezervacie(models.Model):
    id =models.AutoField(primary_key=True, unique=True)
    tim = models.ForeignKey(Timy, on_delete=models.CASCADE, null=True)
    hracieplochy = models.ForeignKey(HraciePlochy, on_delete=models.CASCADE, null=True, default=0)
    typzapasu = models.ForeignKey(TypZapasu, on_delete=models.CASCADE, null=True, default=0)
    date = models.DateField(verbose_name="Dátum")
    start_time = models.TimeField(verbose_name="Čas od")
    end_time = models.TimeField(verbose_name="Čas do")

    def __str__(self):
        return f"Reservation by {self.user.username} on {self.date}"

class Hraci(models.Model):
    id =models.AutoField(primary_key=True, unique = True)
    tim = models.ForeignKey(Timy, on_delete=models.CASCADE)
#    tim = models.CharField(max_length = 10)
    hrac = models.CharField(max_length=80, verbose_name="Celé meno")
    meno = models.CharField(max_length=80, verbose_name="Meno")
    priezvisko = models.CharField(max_length=80, verbose_name="Priezvisko")
    matersky_klub = models.CharField(max_length=50, verbose_name="Materský klub")
    hostujuci_klub = models.CharField(max_length=50, verbose_name="Hosťujúci klub")
    klubova_prislusnost = models.CharField(max_length=50, verbose_name="Klubová príslušnosť")
    hostovanie = models.CharField(max_length=50, verbose_name="Hosťovanie")
    clenske_od = models.DateField(verbose_name="Členské od")
    clenske_do = models.DateField(verbose_name="Členské do")
    registracne_cislo = models.CharField(max_length=12,unique=True, verbose_name="Registračné číslo")
    datum_narodenia = models.DateField(verbose_name="Dátum narodenia")
    platnost_rp = models.DateField(verbose_name="Platnosť reg.preukazu")
    aktivita = models.CharField(max_length=1, verbose_name="Aktivita")
#    aktivita = models.ForeignKey(Zaujem, on_delete=models.CASCADE)
    stav = models.CharField(max_length=12, verbose_name="Stav")

    def __str__(self):
        return f"{self.hrac}"

#class Players(models.Model):
#    id =models.AutoField(primary_key=True, unique = True)
#    timy = models.ForeignKey(Timy, on_delete=models.CASCADE)
#    tim = models.CharField(max_length = 10)
#    hrac = models.CharField(max_length=80, verbose_name="Celé meno")
#    meno = models.CharField(max_length=80, verbose_name="Meno")
#    priezvisko = models.CharField(max_length=80, verbose_name="Priezvisko")
#    matersky_klub = models.CharField(max_length=50, verbose_name="Materský klub")
#    hostujuci_klub = models.CharField(max_length=50, verbose_name="Hosťujúci klub")
#    klubova_prislusnost = models.CharField(max_length=50, verbose_name="Klubová príslušnosť")
#    hostovanie = models.CharField(max_length=50, verbose_name="Hosťovanie")
#    clenske_od = models.DateField(verbose_name="Členské od")
#    clenske_do = models.DateField(verbose_name="Členské do")
#    registracne_cislo = models.CharField(max_length=12,unique=True, verbose_name="Registračné číslo")
#    datum_narodenia = models.DateField(verbose_name="Dátum narodenia")
#    platnost_rp = models.DateField(verbose_name="Platnosť reg.preukazu")
#    aktivita = models.CharField(max_length=1, verbose_name="Aktivita")
#    aktivita = models.ForeignKey(Zaujem, on_delete=models.CASCADE)
#    stav = models.CharField(max_length=12, verbose_name="Stav")



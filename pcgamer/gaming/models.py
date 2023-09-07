from django.db import models

# Create your models here.


class Game(models.Model):
    product_id = models.CharField(max_length=400)
    name = models.CharField(max_length=400)
    marque = models.CharField(max_length=200)
    modele = models.CharField(max_length=200)
    gamme = models.CharField(max_length=500)
    price_cente = models.FloatField(default=3799.94)
    image = models.CharField(max_length=500)
    image1 = models.CharField(max_length=500)
    image2 = models.CharField(max_length=500)
    image3 = models.CharField(max_length=500)
    marque_processor = models.CharField(max_length=200)
    processor = models.CharField(max_length=400)
    type_of_processor = models.CharField(max_length=400)
    processor_speed = models.CharField(max_length=500)
    number_heart = models.CharField(max_length=200)
    ram = models.CharField(max_length=200)
    number_of_barette = models.CharField(max_length=200)
    type_of_memory = models.CharField(max_length=500)
    frequence_memory = models.CharField(max_length=500)
    max_memory = models.CharField(max_length=400)
    gpu_serie = models.CharField(max_length=500)
    chipset_graphique = models.CharField(max_length=500)
    video_memory = models.CharField(max_length=500)
    type_video_memory = models.CharField(max_length=500)
    nividia_studio= models.CharField(max_length=500)
    screen_type = models.CharField(max_length=500)
    screen_tactile = models.CharField(max_length=500)
    screen_tall = models.CharField(max_length=500)
    refresh_rate = models.CharField(max_length=500)
    storage = models.CharField(max_length=200)
    configuration_disque =  models.CharField(max_length=500)
    disque_type =  models.CharField(max_length=500)
    interface_hard_disque =  models.CharField(max_length=500)
    number_of_disque =  models.CharField(max_length=500)
    card_read =  models.CharField(max_length=500)
    wireless_network_statndard =  models.CharField(max_length=500)
    bluetooth_technologie =  models.CharField(max_length=500)
    sans_fil =  models.CharField(max_length=500)
    webcam =  models.CharField(max_length=500)
    type_of_hp =  models.CharField(max_length=500)
    localisation =  models.CharField(max_length=500)
    keyboard =  models.CharField(max_length=500)
    type_activity =  models.CharField(max_length=500)
    backlit_keypad =  models.CharField(max_length=500)
    keyboard_rgb =  models.CharField(max_length=500)
    numeric_keypad =  models.CharField(max_length=500)
    connector=  models.TextField()
    color =  models.CharField(max_length=500)
    description =  models.TextField(max_length=10000)
    descriptions =  models.TextField(max_length=10000, default="cool")
    descriptions1 =  models.TextField(max_length=10000, default="cool")
    descriptions2 =  models.TextField(max_length=10000, default="cool")

  
    battery =  models.CharField(max_length=500)
    cellules =  models.CharField(max_length=500)
    warrenty =  models.CharField(max_length=500)
    os_langage =models.CharField(max_length=200, default='français')
    titre = models.CharField(max_length=500, default="La station de travail CreatorPro X17 A12UKS-080FR a un objectif simple : vous donner suffisamment de puissance pour réaliser tous vos projets. Carte graphique NVIDIA RTX Quadro, processeur Intel Alder Lake HX, dalle Ultra HD 120 Hz...elle ne lésine pas sur les moyens pour atteindre ses objectifs.")
    












    

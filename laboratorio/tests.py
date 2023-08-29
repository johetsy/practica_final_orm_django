from django.test import TestCase
from .models import Laboratorio

class LaboratorioTest(TestCase):
    def setUp(self):
        
        lab1 =Laboratorio()
        lab1.nombre = "Labo 1"
        lab1.ciudad = "Santiago"
        lab1.pais = "Chile"
        lab1.save()
        
        lab2 =Laboratorio()
        lab2.nombre = "Labo 2"
        lab2.ciudad = "Bio Bio"
        lab2.pais = "Chile"
        lab2.save()
        
        lab3 =Laboratorio()
        lab3.nombre = "Labo 3"
        lab3.ciudad = "Concepción"
        lab3.pais = "Chile"
        lab3.save()
        
    def  test_index(self):
        respuesta = self.client.get("/laboratorio/listar")
        labs = respuesta.context["laboratorios"]
        self.assertEqual(3, labs.count())
        
        numv = respuesta.context["numvisit"]
        self.assertEqual(1, numv)
        
    def test_create(self):
        respuesta = self.client.post("/laboratorio/insertar/", {
            "nombre": "Lab 4",
            "ciudad": "Chile",
            "pais": "Chile"
        }, follow = True)
        
        self.assertEqual(200, respuesta.status_code)
        self.assertTemplateUsed(respuesta, "list.html")  
        
        self.assertEqual(4, Laboratorio.objects.all().count()) 
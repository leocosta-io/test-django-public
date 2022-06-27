from django.test import TestCase
from django.utils import timezone

from .models import Instructor, Language

from django.test import Client
from django.urls import reverse


class InstructorModelTests(TestCase):
    def setUp(self):
        languages = [
            {"name": "Portuguese", "code": "pt"},
            {"name": "Spanish", "code": "es"},
            {"name": "English", "code": "en"},
        ]

        for l in languages:
            language = Language(name=l["name"], code=l["code"])
            language.save()

        instructors = [
            {
                "name": "Leonardo Costa",
                "email": "lcosta@redhat.com",
                "username": "lcosta@redhat.com",
                "certid": "100-062-132",
                "languages": "pt,es,en",
            },
            {
                "name": "Hygor",
                "email": "hygor@gmail.com",
                "username": "hygor@gmail.com",
                "certid": "190-091-504",
                "languages": "pt",
            },
            {
                "name": "Mariano",
                "email": "mariano@gmail.com",
                "username": "mariano@gmail.com",
                "certid": "170-031-900",
                "languages": "es",
            },
        ]

        for i in instructors:
            instructor = Instructor(
                name=i["name"],
                email=i["email"],
                username=i["username"],
                certid=i["certid"],
            )

            instructor.save()

            for l in i["languages"].split(","):
                language = Language.objects.get(code=l)
                instructor.languages.add(language)

            instructor.save()

    def test_list(self):
        """
        If list is accessible and has three instructors.
        """
        response = self.client.get(reverse("instructors:list", args=[""]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Leonardo Costa")
        self.assertContains(response, "Hygor")
        self.assertContains(response, "Mariano")

    def test_filter_language_pt(self):
        """
        If list is able to filter using language pt.
        """
        response = self.client.get(reverse("instructors:list", args=["pt"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Leonardo Costa")
        self.assertContains(response, "Hygor")
        self.assertNotContains(response, "Mariano")

    def test_filter_language_es(self):
        """
        If list is able to filter using language es.
        """
        response = self.client.get(reverse("instructors:list", args=["es"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Leonardo Costa")
        self.assertNotContains(response, "Hygor")
        self.assertContains(response, "Mariano")

    def test_filter_language_en(self):
        """
        If list is able to filter using language en.
        """
        response = self.client.get(reverse("instructors:list", args=["en"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Leonardo Costa")
        self.assertNotContains(response, "Hygor")
        self.assertNotContains(response, "Mariano")

    def test_create_course(self):
        from .models import Course

        course = Course.objects.create(
            name="Red Hat OpenShift I: Containers & Kubernetes",
            sku="DO180",
            page="https://www.redhat.com/en/services/training/do180-red-hat-openshift-I-containers-kubernetes",
        )

        course.save()

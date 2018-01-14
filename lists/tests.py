from django.urls import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):
 
    def test_home_page_returns_corrrect_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

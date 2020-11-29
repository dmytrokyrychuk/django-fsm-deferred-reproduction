from django.test import TestCase

from .models import Article


class DeferredTests(TestCase):
    def setUp(self):
        Article.objects.create()

    def test_access_deferred_fsm_field(self):
        Article.objects.defer("state").first().state
    
    def test_access_different_deferred_field(self):
        Article.objects.defer('large_content').first().large_content

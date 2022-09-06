from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Book, Review

class BookTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="reviewtest",
            email="test@email.com",
            password="testpass123",
        )
        cls.book = Book.objects.create(
            title = "test title",
            author = "test author",
            price = "10.00",
        )
        cls.review = Review.objects.create(
            book = cls.book,
            author = cls.user,
            review = "thats nice",
        )
        
    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "test title")
        self.assertEqual(f"{self.book.author}", "test author")
        self.assertEqual(f"{self.book.price}", "10.00")
        
    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test title")
        self.assertTemplateUsed("books/books_list.html")
    
    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "test title")
        self.assertContains(response, "thats nice")
        self.assertTemplateUsed(response, "books/book_detail.html")
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = "test@londonappedv.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
                email = email,
                password = password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "test@London.com"
        password = "111222333"

        user = get_user_model().objects.create_user(
                email = email,
                password = password,
        )
        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        email = None
        password = "test123"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email, password)

    def test_create_new_superuser(self):
        """test create superuser"""
        user = get_user_model().objects.create_superuser(
                "test@test.com",
                "test1234"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


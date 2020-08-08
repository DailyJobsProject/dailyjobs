from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory

# Create your tests here.
from django.urls import reverse

from users.forms import CompanySignUpForm
from users.models import User, Company, Employee


# class SignUpCompanyPageTests(TestCase):
#     def setUp(self) -> None:
#         self.pk = 1
#         self.user = 'testuser'
#         self.email = 'testuser@email.com'
#         self.password = 'testpass1'
#         self.password1 = 'testpass1'
#         self.name = 'valicorp'
#         self.telephone = '073943234'
#
#     def test_signup_page_url(self):
#         response = self.client.get("signup/company/")
#         self.assertEqual(response.status_code, 404)
#         self.assertTemplateUsed(response, template_name='registration/company_signup_form.html')
#
#     def test_signup_page_view_name(self):
#         response = self.client.get(reverse('users:company_detail',  kwargs={'pk': self.pk}))
#         self.assertEqual(response.status_code, 302)
#         self.assertTemplateUsed(response, template_name='registration/company_signup_form.html')
#
#     def test_signup_form(self):
#         response = self.client.post(reverse('users:company_signup'), data={
#             'username': self.user,
#             'email': self.email,
#             'password1': self.password,
#             'password2': self.password,
#             'valicorp ': self.name,
#             '073943234,': self.telephone,
#         })
#         self.assertEqual(response.status_code, 200)
#
#         users = User().objects.all()
#         self.assertEqual(users.count(), 1)
#
from users.views import CompanyDetailView


class CompanyUserTestCaste(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='vali', email='vali@valicorp.com', password='testpass1')

    def test_details(self):
        request = self.factory.get('users:company_detail')
        request.user = self.user
        request.user = AnonymousUser
        response = CompanyDetailView.as_view()(request)
        self.assertEqual(response.status.code, 200)


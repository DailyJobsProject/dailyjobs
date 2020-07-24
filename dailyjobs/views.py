from django.views.generic import TemplateView

class StartPage(TemplateView):
    template_name = 'start_page.html'

class LoggedOutPage(TemplateView):
    template_name = 'logged_out.html'
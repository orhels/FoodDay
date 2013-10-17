from django.views.generic import TemplateView


class FrontPageView(TemplateView):
    template_name = 'frontpage.html'


class BasePageView(TemplateView):
    template_name = 'base.html'

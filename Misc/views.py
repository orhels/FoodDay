from django.views.generic import TemplateView


class FrontPageView(TemplateView):
    template_name = 'frontpage.html'


class BasePageView(TemplateView):
    template_name = 'base.html'


class FooterPageView(TemplateView):
    template_name = 'footer.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class FaqPageView(TemplateView):
    template_name = 'faq.html'
from django.views.generic import TemplateView, ListView
from .models import TeamMember, Merchandise

class HomePageView(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['merchandise'] = Merchandise.objects.all()  # Pass all items
        return context

class AboutPageView(TemplateView):
    template_name = 'shop/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = TeamMember.objects.all()
        return context

class ShopPageView(ListView):
    model = Merchandise
    template_name = 'shop/shop.html'
    context_object_name = 'merchandise'


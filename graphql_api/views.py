from django.urls import reverse
from django.views.generic import TemplateView

class GraphQLPlaygroundView(TemplateView):
    template_name = 'graphql_api/playground.html'

    def get_context_data(self, **kwargs):
        context = super(GraphQLPlaygroundView, self) \
            .get_context_data(**kwargs)
        context.update(graphql_path=reverse('graphql'))

        return context

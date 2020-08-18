from django.http import HttpResponseRedirect, Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import renderers, permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from administration.models import Setting
from administration.serializers import SettingSerializer


class SettingViewSet(ReadOnlyModelViewSet):
    """
        retrieve:
            Return a setting instance.

        list:
            Return all settings.
    """

    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'


class FaviconRenderer(renderers.BaseRenderer):
    media_type = 'image/*'
    format = 'ico'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data


class FaviconView(APIView):
    renderer_classes = (FaviconRenderer,)

    @swagger_auto_schema(
        operation_id='favicon',
        operation_description='Get favicon from panel settings',
    )
    def get(self, request):
        try:
            favicon = Setting.objects.get(slug='favicon')
            if favicon.image and favicon.image.url:
                return HttpResponseRedirect(favicon.image.url)  # 302
        except Setting.DoesNotExist:
            pass

        raise Http404()

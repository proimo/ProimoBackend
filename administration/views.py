from django.db.models import QuerySet
from django.http import HttpResponseRedirect, Http404, HttpResponseBadRequest
from drf_yasg.utils import swagger_auto_schema
from rest_framework import renderers, permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.core.management import call_command
from django.core.management.commands import dumpdata, loaddata
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect

from common.utils import message_info, message_error
from administration.models import Setting, MenuItem
from administration.serializers import SettingSerializer, MenuItemSerializer


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

    @swagger_auto_schema(operation_id='favicon', operation_description='Get favicon from panel settings', )
    def get(self, request):
        try:
            favicon = Setting.objects.get(slug='favicon')
            if favicon.image and favicon.image.url:
                return HttpResponseRedirect(favicon.image.url)  # 302
        except Setting.DoesNotExist:
            pass

        raise Http404()


class MenuItemViewSet(ReadOnlyModelViewSet):
    queryset: QuerySet[MenuItem] = MenuItem.objects.filter(is_published=True, parent__exact=None)
    serializer_class = MenuItemSerializer
    lookup_field = 'slug'

    def get_object(self):
        obj: MenuItem = super(MenuItemViewSet, self).get_object()
        if obj.parent:
            raise Http404
        return obj


def generate_seed(request: HttpRequest):
    if str(request.user).__eq__("AnonymousUser"):
        return HttpResponseBadRequest()

    if not request.user.is_superuser:
        message_error(request, "You're not allowed to do that, little burglar!")
        return redirect('/api/admin/')

    try:
        with open('data.json', 'w') as f:
            call_command(dumpdata.Command(), '--natural-foreign', '--natural-primary', '--indent=4', stdout=f)
        message_info(request, 'Toate informaţiile din baza de date au fost salvate în fişierul data.json! '
                              'Îl poţi descărca prin "Descarcă seed"')
    except Exception as err:
        message_error(request, f'A apărut o eroare! Datele nu au putut fi exportate. Error stack: {err}')

    return redirect('/api/admin/')


def load_seed(request: HttpRequest):
    if str(request.user).__eq__("AnonymousUser"):
        return HttpResponseBadRequest()

    if not request.user.is_superuser:
        message_error(request, "You're not allowed to do that, little burglar!")
        return redirect('/api/admin/')

    try:
        call_command(loaddata.Command(), 'data.json')
        message_info(request, 'Infromaţiile au fost încărcate în baza de date!')
    except Exception as err:
        message_error(request, f'A apărut o eroare! Datele nu au fost încarcate în baza de date. Error stack: {err}')

    return redirect('/api/admin/')


def download_seed(request: HttpRequest):
    if str(request.user).__eq__("AnonymousUser"):
        return HttpResponseBadRequest()

    if not request.user.is_superuser:
        message_error(request, "You're not allowed to do that, little burglar!")
        return redirect('/api/admin/')

    try:
        with open('data.json', 'r') as f:
            response = HttpResponse(f.read(), content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename=data.json'
            return response
    except Exception as err:
        message_error(request, f'A apărut o eroare! Fişierul nu a putut fi descărcat. Error stack: {err}')

    return redirect('/api/admin/')

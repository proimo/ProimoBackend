from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import renderers, permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from administration.forms import EditProfileForm, ProfileForm
from administration.models import Setting, User
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


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        print(form)
        print(profile_form)

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('/api/admin')
        return redirect('edit-profile')
    else:
        # form = EditProfileForm(instance=request.user)
        # profile_form = ProfileForm(instance=request.user.profile)
        # args = {'form': form, 'profile_form': profile_form}
        return redirect(f'/api/admin/administration/user/{request.user.id}/change')
        # return render(request, 'admin/edit_profile.html', args)


# @login_required
# def current_user(request):
#     return request.user

from django.contrib.admin import AdminSite, site
from django.urls import path

from django_apps.raw_data.views import RawDataView

class BackendAdminSite(AdminSite):
    site_title = 'Sanskrin admin site'
    site_header = 'Sanskrin administration'
    index_title = 'Site adminstration'

    def __init__(self, *args, **kwargs):
        super(BackendAdminSite, self).__init__(*args, **kwargs)
        self._registry.update(site._registry)

    def get_urls(self):
        urls = super(BackendAdminSite, self).get_urls()

        urls += [
            path('raw-data/upload', self.admin_view(RawDataView.as_view()), {'admin_site': self}),
        ]

        return urls

    def each_context(self, request):
        context = super(BackendAdminSite, self).each_context(request)

        context['available_apps'] = self.get_app_list(request)

        return context

    def get_app_list(self, request):
        app_list = super(BackendAdminSite, self).get_app_list(request)

        app_list.append(
            {
                'app_label': 'raw-data',
                'has_module_perms': True,
                'name': 'Raw Data',
                'models': [
                    {
                        'admin_url': '/admin/raw-data/upload',
                        'name': 'Upload Raw Data',
                        'object_name': 'Upload',
                        'perms': {
                            'add': True,
                            'change': True,
                            'delete': True,
                            'view': True
                        },
                        'view_only': True
                        }
                    ]}
            )

        return app_list

admin_site = BackendAdminSite()
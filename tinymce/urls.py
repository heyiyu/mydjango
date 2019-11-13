# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)
from django.urls import path
from . import views
app_name = 'tinymce'
urlpatterns = [
    path(r'^js/textareas/(?P<name>.+)/$', views.textareas_js, name='tinymce-js'),
    path(r'^js/textareas/(?P<name>.+)/(?P<lang>.*)$', views.textareas_js, name='tinymce-js-lang'),
    path(r'^spellchecker/$', views.spell_check),
    path(r'^flatpages_link_list/$', views.flatpages_link_list),
    path(r'^compressor/$', views.compressor, name='tinymce-compressor'),
    path(r'filebrowser/', views.filebrowser, name='tinymce-filebrowser'),
    path(r'^preview/(?P<name>.+)/$', views.preview, name='tinymce-preview'),
]
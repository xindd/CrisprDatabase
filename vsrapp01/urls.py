"""crispr_porject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from vsrapp01 import views
urlpatterns = [
    url(r'^$', views.indexn),
    url(r'^VSR/index/$', views.index),
    url(r'^VSR/browse/(?P<pagename>[\s\S]*)$', views.browse),
    url(r'^VSR/browse_detail/(?P<protein_name>[\s\S]*)$', views.browse_detail),
    url(r'^VSR/browse_VSR_detail/(?P<vsr_name>[\s\S]*)$', views.browse_VSR_detail),
    url(r'^VSR/browse_anti_detail/(?P<anti_name>[\s\S]*)$', views.browse_anti_detail),
    url(r'^VSR/browse_homologs/(?P<protein_name>[\s\S]*)$', views.browse_homologs),
    url(r'^VSR/analyze/$', views.analyze),
    url(r'^VSR/analyze/sequence$', views.analyze_sequence),
    url(r'^VSR/analyze/search$', views.analyze_search),
    url(r'^VSR/analyze_result/$', views.analyze_result),
    url(r'^VSR/analyze_run/(?P<jobid>[\d]*)$', views.analyze_run),
    url(r'^VSR/deposit/(?P<data>[\s\S]*)$', views.deposit),
    url(r'^VSR/download/$', views.download),
    url(r'^VSR/help/$', views.help),
    url(r'^VSR/visualize/(?P<visualname>[\s\S]*)$', views.visualize),
    url(r'^VSR/structure_detail/(?P<pdbid>[\s\S]*)$', views.protein_detail),
    url(r'^VSR/general_align/$', views.general_align),
    url(r'^VSR/browse_phylogenetic/(?P<family_name>[\s\S]*)$', views.browse_phylogenetic),
    url(r'^VSR/search/$', views.search),
    url(r'^VSR/visualdetail/(?P<familyname>[\s\S]*)$', views.visualize_detail),
    url(r'^VSR/blast/$', views.blast),



]

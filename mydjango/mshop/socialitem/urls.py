from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from pollitem import views as pv

urlpatterns = [
    # Examples:
    # url(r'^$', 'socialitem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^poll/(\d+)$', pv.poll, name='poll-url'),
    # url(r'^govote/$', pv.govote),
    # url(r'^addpoll/$', pv.addpoll, name='addpoll-url'),
    # url(r'^updatepollitem/(\d+)$', pv.updatepollitem, name='addpollitem-url'),
    # url(r'^vote/(\d+)/(\d+)$', pv.vote, name='vote-url'),
    url(r'^(\d*)$', pv.index, name='index'),
    url(r'^product/(\d+)$', pv.product, name='product-url'),
    url(r'^cart/$', pv.cart),
    url(r'^additem/(\d+)/(\d+)$', pv.add_to_cart, name='additem-url'),
    url(r'^removeitem\(d+)$', pv.remove_from_cart, name='removeitem-url'),

    # 安装包的URL
    url(r'^filer/$', include('filer.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
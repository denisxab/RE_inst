from django.conf.urls.static import static
from django.urls import path, include

from mainapp.views import RePage
from re_view import settings

urlpatterns = [
		path('', RePage.as_view(), name="main_url"),
]

# Для debug_toolbar и отдачи статических фалов / медиа фалов
if settings.DEBUG:
	# Для отладчика
	import debug_toolbar
	
	urlpatterns.append(
			path('__debug__/', include(debug_toolbar.urls)),
	)
	
	# Для работы static
	urlpatterns += static(settings.STATIC_URL,
	                      document_root=settings.STATIC_ROOT)
	
	# Для работы  media
	urlpatterns += static(settings.MEDIA_URL,
	                      document_root=settings.MEDIA_ROOT)

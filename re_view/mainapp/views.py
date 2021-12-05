from re import sub, search, split, match, findall

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


class RePage(View):
	template_name = "mainapp/re_page.html"  # Путь к шаблону `html`
	http_method_names = ["get", "post", ]  # Список методов HTTP, которые обрабатывает класс.
	
	# Словарь поддерживаемых регулярных функций
	convert_srt_in_fun = {
			"match"  : match,
			"search" : search,
			"split"  : split,
			"sub"    : sub,
			"findall": findall,
	}
	
	def get(self, request: WSGIRequest):
		return render(request,
		              template_name=self.template_name,
		              context={"list_re_fun": self.convert_srt_in_fun.keys()})
	
	def post(self, request: WSGIRequest, *args, **kwargs):
		
		# Регулярная функция
		re_fun = self.convert_srt_in_fun.get(request.POST.get('flag_func_re', 'match'), match)
		# Шаблон для регулярной функции
		templates_re = request.POST.get('templates_re', None)
		# Текст для регулярной функции
		request_text_re = request.POST.get('data_from_form', None)
		# Текст для замены. Используется для регулярной функции `sub`
		replace_templates_re = request.POST.get('replace_templates_re', '')
		
		#  Если есть шаблон текста и регулярная функция.
		res = None
		if templates_re and request_text_re:
			
			#  Если вызвана функция [sub, split].
			if re_fun.__name__ in {"sub", "split", "findall"}:
				if re_fun.__name__ == 'sub':
					res = re_fun(pattern=templates_re, repl=replace_templates_re, string=request_text_re, )
				else:
					res = re_fun(pattern=templates_re, string=request_text_re, )
				
				if res:
					return JsonResponse({"result": True, "data": res})
			
			# Если вызвана функция [match, search]
			elif re_fun.__name__ in {'match', 'search', }:
				res = re_fun(pattern=templates_re, string=request_text_re, )
				if res:
					print(res)
					return JsonResponse({"result": True, "data": res.groups()})
		
		# Если произошли ошибки, то уведомляем об этом.
		return JsonResponse({"result": False, "data": ''})

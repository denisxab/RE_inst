import re

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views import View


class RePage(View):
	template_name = "mainapp/re_page.html"  # Путь к шаблону `html`
	http_method_names = ["get", "post", ]  # Список методов HTTP, которые обрабатывает класс.
	
	context_object_name = 're'
	
	# model =  # Какую модель используем
	# queryset = .objects. # Получаем данные из БД
	
	convert_srt_in_fun = {
			"match"  : re.match,
			"search" : re.search,
			"split"  : re.split,
			"sub"    : re.sub,
			"findall": re.findall,
	}
	
	def get(self, request: WSGIRequest):
		"""
		В методе обрабатывается GET запрос
		request.method == "GET"
		"""
		
		return render(request,
		              template_name=self.template_name,
		              context={"list_re_fun": self.convert_srt_in_fun.keys()}
		              )
	
	def post(self, request: WSGIRequest, *args, **kwargs):
		"""
		В методе обрабатывается POST запрос
		request.method == "POST"
		"""
		
		# Регулярная функция
		re_fun = self.convert_srt_in_fun.get(request.POST.get('flag_func_re', 'match'), re.match)
		# Шаблон для регулярной функции
		templates_re = request.POST.get('templates_re', None)
		# Текст для регулярной функции
		request_text_re = request.POST.get('data_from_form', None)
		# Текст дл замены. Используется для регулярной функции `sub`
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

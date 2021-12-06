from re import sub, search, split, match, findall
from typing import Union, Callable, Optional

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from loguru import logger


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
		re_fun: Callable = self.convert_srt_in_fun.get(request.POST.get('flag_func_re', 'match'), match)
		# Шаблон для регулярной функции
		templates_re: Optional[str] = request.POST.get('templates_re', None)
		# Текст для регулярной функции
		request_text_re: Optional[str] = request.POST.get('data_from_form', None)
		# Текст для замены. Используется для регулярной функции `sub`
		replace_templates_re: str = request.POST.get('replace_templates_re', '')
		
		#  Если есть шаблон текста и регулярная функция.
		res: dict[str:Union[bool, str]] = {"result": False, "data": ''}
		if templates_re and request_text_re:
			#  Если вызвана функция [sub, split].
			if re_fun.__name__ in {"sub", "split", "findall"}:
				if re_fun.__name__ == 'sub':
					_res_text = re_fun(pattern=templates_re, repl=replace_templates_re, string=request_text_re, )
				else:
					_res_text = re_fun(pattern=templates_re, string=request_text_re, )
				if _res_text:
					res = {"result": True, "data": str(_res_text)}
			
			# Если вызвана функция [match, search]
			elif re_fun.__name__ in {'match', 'search', }:
				_res_text = re_fun(pattern=templates_re, string=request_text_re, )
				if _res_text:
					res = {"result": True, "data": str(_res_text.groups())}
		
		# Логирование
		logger.info(
				f"Функция:`{re_fun.__name__}`;Шаблон:`{templates_re}`;Текст:`{request_text_re}`;"
				f"{'Текст для замены: `%s`' % replace_templates_re if replace_templates_re else ''}"
				f"Результат:{res};")
		
		# Если произошли ошибки, то уведомляем об этом.
		return JsonResponse(res)

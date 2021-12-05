//   Когда `html`  документ  загружен
$(document).ready(function () {
	
	//// Меню с регулярными функциями
	// Переменная для хранения выбранной регулярной функции
	let SelectReFun = $('#SelectReFun')[0].options[$(`#SelectReFun`)[0].selectedIndex].value;
	console.log("SelectReFun: " + SelectReFun);
	//  При выборе другого `option` обновить значение переменной `SelectReFun`
	$("#SelectReFun").change(
		function () {
			// location = this.value
			SelectReFun = this['value'];
			console.log(SelectReFun);
			// Проверить нужно ли показывать элемент для замены текста `sub`
			IsShowReplaceTo(SelectReFun)
			
		});
	
	// Проверяет нужно ли показывать элемент для замены текста
	function IsShowReplaceTo(_SelectReFun) {
		if (_SelectReFun === 'sub') {
			$('#ReplaceTo').show(300);
		} else {
			$('#ReplaceTo').hide(300);
		}
	}
	
	// При загрузке элемента проверить необходимость показать элемент
	IsShowReplaceTo(SelectReFun)
	
	////
	
	//// Работа с сервером
	// Отправка данных на сервер, для выполнения регулярных выражения
	function SendDataFromServer_Re() {
		
		// Получаем данные из формы, и создаем объект
		const dataVar = {
			csrfmiddlewaretoken: $('#SendTextFromRE').attr('csrfmiddlewaretoken'), // Специально имя для токена
			// Данные для проверки регулярного выражения
			data_from_form: $('#TextRe').val(),
			// Шаблон регулярного выражения
			templates_re: $('#templates_re').val(),
			// Если существует текст для замены
			replace_templates_re: $(`#replace_templates_re`).length > 0 ? $('#replace_templates_re').val() : '',
			// Регулярная функция
			flag_func_re: SelectReFun,
		};
		
		
		// Отладочная информация
		console.log(dataVar)
		
		
		// Отправляем `ajax` запрос
		$.ajax({
			// Тело сообщения
			method: "POST", // Http Метод отправки данных на сервер
			url: UrlBasketServer, // Берем url из ранее созданной переменной в шаблоне
			data: dataVar, // Данные на сервер
			
			
			// Вызовится если при отправке возникли ошибки
			error: function (response) {
				const exceptionVar = "Ошибка отправки" + response
				alert(exceptionVar);
				console.log(exceptionVar)
			}
		}).done(function (msg) { // Получаем ответ от сервера, и обрабатываем его.
			console.log(msg)
			$('#SendRe').val(msg['data']);
		});
		
		// Остановить перезагрузку страницы
		return false;
	}
	
	// Перехватываем отправку формы
	$("#SendTextFromRE").submit(SendDataFromServer_Re);
	////
	
	//// Работа с текстовым полем
	// Получать данные из формы через указанное количество секунд
	let LastTextIn_TextRe = '';
	
	function GetTextFromFormSendTextFromRE_Interval() {
		let tmp = $('#TextRe').val();
		if (tmp !== LastTextIn_TextRe) {
			LastTextIn_TextRe = tmp;
			console.log(tmp);
			SendDataFromServer_Re(tmp);
		}
	}
	
	setInterval(GetTextFromFormSendTextFromRE_Interval, 500,);
	////
})

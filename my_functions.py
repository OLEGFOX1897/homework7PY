def inp_num(type_num): 
	'''Функция возвращает либо целое, либо вещественное введенное число. Проверяет правильность ввода.
	При вх 1 - проверяет, что введенное число целое.
	При вх 0 - проверяет, что введенное число вещественное, а не буквы или знаки.'''
	ind=0
	while ind==0:
		if type_num==1: #целое
			try:
				num=int(input('n='))
				ind=1
			except:
				ind=0
				print('Повторите ввод')

		elif type_num==0:
			try:
				num=float(input('n='))
				ind=1
			except:
				ind=0
				print('Повторите ввод')
		else:
			print('В функции inp_num указан неверный вх параметр (может быть 0 или 1)')
	return num

def input_list(type): 
	'''Функция возвращает список из целых или вещественных чисел. При вх параметре 0 -целые, при 1 - вещественные. Иначе выдает 
	"Повторный ввод".
	Входной параметр задается на этапе написания программы.'''
	print('Введите количество элементов списка')
	len_list=inp_num(1)
	num_list=[]
	for ind_list in range(len_list):
		print(f'Введите {ind_list+1}-й эл списка')
		el_list=inp_num(type)
		num_list.append(el_list)
	print(f'Ваш список{num_list}')
	return num_list

def num_frac (num):
	'''
	Функция находит дробную часть от вещественного числа до 2 знаков
	'''
	frac=num-int(num)
	return round(frac,2)


def min_max_list(list,param): 
	'''
	Функция определяет в списке (первый входной параметр функции) максимум и минимум.
	При значении второго параметра 0 - возращает минимум.
	При значении второго параметра 1 - возращает максимум.
	'''
	min_l=min(list)
	max_l=max(list)
	if param==0:
		return min_l
	elif param==1: 
		return max_l
	else: print('Ошибка второго параметра или 0 или 1')

def revers_list(list_in):
	'''Функция возвращает обратный список входному.  
	Пример вх: [1,1,2,3,5] - > вых [5,3,2,1,1]'''
	list_out=[]
	for ind in range(len(list_in)-1,-1,-1):
		list_out.append(list_in[ind])
	return list_out

def clean_list(inp_list):
	'''Функция возвращает список, в котором будет только по одному элементу от входного.
    Выходной список будет иметь тот же тип данных, что и входной'''
	out_list=[]
	for x in inp_list:
		if (x in out_list)==0:
			out_list.append(x)
	return out_list

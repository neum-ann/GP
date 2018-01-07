#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Специальная сортировка для двухсвязных списков
def sorted_group(arr):
	# Цикл для каждого элемента массива
	for i in range(1, len(arr), 2):
		# Цикл для проверки с каждым элементом массива
		for j in range(1, len(arr), 2):
			# Если текущий элемент меньше чем основной
			if int(arr[j])<int(arr[i]):
				# Перестановка значения
				temp=arr[i]
				arr[i]=arr[j]
				arr[j]=temp

				# Перестановка ключа
				temp=arr[i-1]
				arr[i-1]=arr[j-1]
				arr[j-1]=temp

	return arr

# Действия если запускается именно этот файл
if __name__=='__main__':
	pass
#функция прдсчетов
def url_count(u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8):
	#задаем начальное кол-во ссылок
	count_u = 0

	if u_1 == "0": count_u = count_u + 0
	else:count_u = count_u + 1

	if u_2 == "0": count_u = count_u + 0
	else:count_u = count_u + 1

	if u_3 == "0": count_u = count_u + 0
	else:count_u = count_u + 1

	if u_4 == "0": count_u = count_u + 0
	else:count_u = count_u + 1

	if u_5 == "0": count_u = count_u + 0
	else:count_u = count_u + 1

	if u_6 == "0": count_u = count_u + 0
	else:count_u = count_u + 1

	if u_7 == "0": count_u = count_u + 0
	else:count_u = count_u + 1

	if u_8 == "0": count_u = count_u + 0
	else:count_u = count_u + 1

	return(count_u)
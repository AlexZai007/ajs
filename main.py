"""
=-=-=-=-=-=-=-=-=-=-=-=-=-
	БЛОК С ГЛОБАЛЬНЫМИ КФГ
=-=-=-=-=-=-=-=-=-=-=-=-=-
"""
#импортируем библиотеки
import webbrowser
import pyautogui
import time
from datetime import datetime

#импортируем конфиги
from config import wait_time
from config import u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8 
from config import t_1, t_2, t_3, t_4, t_5, t_6, t_7, t_8
from config import b_x_join, b_y_join 
from config import b_x_join_inapp, b_y_join_inapp 
from config import b_x_leave_inapp, b_y_leave_inapp
from config import b_x_open, b_y_open



"""
=-=-=-=-=-=-=-=-=-=-=-=-=-
	БЛОК С ЛОКАЛЬНЫМИ КФГ
=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

#импортируем плагины
from plugins.url_count import url_count

#переменные для расчетов(НЕ ТРОГАТЬ!)
reaction = 0

#перемены для удобства
url_count = url_count(u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8)




"""
=-=-=-=-=-=-=-=-=-=-=-=-=-
	БЛОК С ФУНКЦИЯМИ
=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

#функция времени (если есть 0 пропускаем)
def now():
	current_datetime = datetime.now()
	return(str(current_datetime.hour) + ":" +str(current_datetime.minute))

#функция открытия/закрытия урока
def leson_start():
	time.sleep(wait_time)
	pyautogui.click(b_x_join, b_y_join)
	time.sleep(wait_time)
	pyautogui.click(b_x_open, b_y_open)
	time.sleep(wait_time)
	pyautogui.click(b_x_join_inapp, b_y_join_inapp)

def leson_stop():
	time.sleep(wait_time)
	pyautogui.click(b_x_leave_inapp, b_y_leave_inapp)


#главная функция которая управляет открытиями
def main(url, start, end):
	if now() == start:
		#стопим урок
		webbrowser.open(url)
		leson_start()
	if now() == end:
		leson_stop()


"""
=-=-=-=-=-=-=-=-=-=-=-=-=-
	ОСНОВНОЙ БЛОК
=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

while reaction == 0:
	time.sleep(59)

	print("Обробатываю запросы...")


	#блок проверки времени и открытия ссылок
	main(u_1, t_1[0], t_1[1])
	main(u_2, t_2[0], t_2[1])
	main(u_3, t_3[0], t_3[1])
	main(u_4, t_4[0], t_4[1])
	main(u_5, t_5[0], t_5[1])
	main(u_6, t_6[0], t_6[1])
	main(u_7, t_7[0], t_7[1])
	main(u_8, t_8[0], t_8[1])


#функция прости меня :(
if reaction == 1:
	print("Спасибо что воспользовались AJS by alexzai007")


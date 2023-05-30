"""
En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso
del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el
tiempo que queda de trabajo.
"""

import time

current_time = time.localtime()

hora_salir = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday,
                 21, 0, 0,current_time.tm_wday,
                 current_time.tm_yday, current_time.tm_isdst))

if current_time>hora_salir:
    print('Para casa que ya es hora')

while(current_time<hora_salir):
    current_time = time.localtime()
    hh_c = current_time.tm_hour
    mm_c = current_time.tm_min
    ss_c = current_time.tm_sec

    hh_t = hora_salir.tm_hour
    mm_t = hora_salir.tm_min
    ss_t = hora_salir.tm_sec

    queda = (hh_t*3600+mm_t*60+ss_t)-(hh_c*3600+mm_c*60+ss_c)
    hh_quedan = queda//3600
    mm_quedan = (queda%3600)//60
    ss_quedan = queda%60
    print(f'Aún te quedan {str(hh_quedan).zfill(2)}:{str(mm_quedan).zfill(2)}:{str(ss_quedan).zfill(2)}')

    time.sleep(1)
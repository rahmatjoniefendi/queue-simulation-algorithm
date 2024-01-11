def get_arrival_time(inter_arrival_time, index=0, result=0, arrival_time=[]):
    if index == len(inter_arrival_time):
        return arrival_time

    arrival_time.append(result + inter_arrival_time[index])
    return get_arrival_time(inter_arrival_time,
                            index + 1,
                            result + inter_arrival_time[index])

def get_into_time_before_compared(service_time, index=0, result=0, into_time=[]):
    if index == len(service_time):
        return into_time

    if index == 0:
        into_time.append(result)

    into_time.append(result + service_time[index])
    return get_into_time_before_compared(service_time,
                                         index + 1,
                                         result + service_time[index])


def get_into_time(service_time, arrival_time):
    before_compared = get_into_time_before_compared(service_time,
                                                    result=arrival_time[0])

    into_time = []

    for at, bc in zip(arrival_time, before_compared):
        if at > bc:
            into_time.append(at)
        elif at < bc:
            into_time.append(bc)
        else:
            into_time.append(at)
    
    return into_time


def get_front_time(service_time, into_time):
    front_time = []
    for st, it in zip(service_time, into_time):
        front_time.append(st + it)
    return front_time


def get_queue_time(into_time, arrival_time):
    queue_time = []
    for it, at in zip(into_time, arrival_time):
        queue_time.append(it - at)
    return queue_time


def get_idle_time(into_time, front_time):
    idle_time = []
    ft = front_time.copy()
    ft.append(0)
    
    for i in range(len(into_time)):
        idle_time.append(into_time[i] - ft[i-1])
    return idle_time


def get_system_process_time(front_time, arrival_time):
    system_process_time = []
    for ft, at in zip(front_time, arrival_time):
        system_process_time.append(ft - at)
    return system_process_time
    
def get_total_time(front_time):
    return max(front_time)

def get_total_queue_time(queue_time):
    return sum(queue_time)

def get_total_idle_time(idle_time):
    return sum(idle_time)

def get_total_service_time(service_time):
    return sum(service_time)

def get_total_system_process_time(system_process_time):
    return sum(system_process_time)


def get_average_queue_time_with_simulation(arrival_number, total_queue_time):
    number_of_arrival = len(arrival_number)
    return total_queue_time / number_of_arrival

def get_average_queue_time_without_simulation(myu, lmbda):    
    wg = ( myu / (lmbda * (lmbda - myu)) ) * 3600
    return wg


def get_average_system_process_time_with_simulation(arrival_number, total_system_process_time):
    number_of_arrival = len(arrival_number)
    return total_system_process_time / number_of_arrival

def get_average_system_process_time_without_simulation(myu, lmbda):
    w = ( 1 / (lmbda-myu) ) * 3600
    return w

def get_average_queue_length_with_simulation(total_time, total_queue_time):
    return total_queue_time / total_time

def get_average_queue_length_without_simulation(myu, lmbda):
    lg = ( myu ** 2 / (lmbda * (lmbda-myu)) )
    return lg

def get_average_number_in_system_with_simulation(total_time, total_system_process_time):
    return total_system_process_time / total_time

def get_average_number_in_system_without_simulation(myu, lmbda):
    l = myu / (lmbda - myu)
    return l

def get_average_service_point_idle_time_with_simulation(total_time, total_idle_time):
    return total_idle_time / total_time

def get_average_service_point_idle_time_without_simulation(average_service_point_idle_time):
    r = average_service_point_idle_time * 100;
    return r

def mixed_congruent_method(count, a, c, m, z0):
    result = [z0]
    
    for i in range(count):
        z = ((a * result[i]) + c) % m
        result.append(z)

    result.remove(result[0])

    return result

def multiplicative_method(count, a, m, z0):
    result = [z0]
    random_variate = []
    
    for i in range(count+1):
        zi = ((a * result[i])) % m
        r = zi / m
        random_variate.append(r)
        result.append(zi)

    result.remove(result[len(result)-1])

    return result

def show_table(names, items):
    print('+------------------------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+')
    for i in range(len(items)):
        print('|{}'.format(str(names[i])).ljust(25), end='')
        for j in items[i]:
            print('|{}'.format(str(j).ljust(5)), end='')
        print('|')
        print('+------------------------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+')

def demo_1():
    arrival_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    inter_arrival_time   = [38, 3, 41, 20, 57, 10, 46, 99, 87, 221]
    service_time   = [136, 17, 23, 4, 70, 55, 36, 17, 12, 62]

    arrival_time = get_arrival_time(inter_arrival_time.copy())
    into_time = get_into_time(service_time, arrival_time)
    front_time = get_front_time(service_time, into_time)
    queue_time = get_queue_time(into_time, arrival_time)
    idle_time = get_idle_time(into_time, front_time)
    system_process_time = get_system_process_time(front_time, arrival_time)

    total_time = get_total_time(front_time)
    total_queue_time = get_total_queue_time(queue_time)
    total_idle_time = get_total_idle_time(idle_time)
    total_service_time = get_total_service_time(service_time)
    total_system_process_time = get_total_system_process_time(system_process_time)
    

    average_queue_time_with_simulation = get_average_queue_time_with_simulation(arrival_number, total_queue_time)

    average_system_process_time_with_simulation = get_average_system_process_time_with_simulation(arrival_number, total_system_process_time)

    average_queue_length_with_simulation = get_average_queue_length_with_simulation(total_time, total_queue_time)

    average_number_in_system_with_simulation = get_average_number_in_system_with_simulation(total_time, total_system_process_time)
        
    average_service_point_idle_time_with_simulation = get_average_service_point_idle_time_with_simulation(total_time, total_idle_time)
    

    # Diketahui dari soal
    inter_arrival_time_in_minute = 60
    service_time_in_minute = 40

    # Untuk mendapatkan interval arrival time
    myu = 3600 / inter_arrival_time_in_minute

    # Untuk mendapatkan interval service time
    lmbda = 3600 / service_time_in_minute


    average_queue_time_without_simulation = get_average_queue_time_without_simulation(myu, lmbda)
    average_system_process_time_without_simulation = get_average_system_process_time_without_simulation(myu, lmbda)
    average_queue_length_without_simulation = get_average_queue_length_without_simulation(myu, lmbda)
    average_number_in_system_without_simulation = get_average_number_in_system_without_simulation(myu, lmbda)
    average_service_point_idle_time_without_simulation = get_average_service_point_idle_time_without_simulation(
        average_service_point_idle_time_with_simulation)

    print('ARRIVAL NUMBER       : ' + str(arrival_number))
    print('INTER ARRIVAL TIME   : ' + str(inter_arrival_time))
    print('ARRIVAL TIME         : ' + str(arrival_time))
    print('SERVICE TIME         : ' + str(service_time))
    print('INTO TIME            : ' + str(into_time))
    print('FRONT TIME           : ' + str(front_time))
    print('QUEUE TIME           : ' + str(queue_time))
    print('IDLE TIME            : ' + str(idle_time))
    print('SYSTEM PROCESS TIME  : ' + str(system_process_time), end='\n\n\n')

    print('TOTAL TIME                  : ' + str(total_time))
    print('TOTAL QUEUE TIME            : ' + str(total_queue_time))
    print('TOTAL IDLE TIME             : ' + str(total_idle_time))
    print('TOTAL SYSTEM PROCESS TIME   : ' + str(total_system_process_time), end='\n\n\n')

    
    print('AVERAGE QUEUE TIME WITH SIMULATION               : ' + str(average_queue_time_with_simulation))
    print('AVERAGE QUEUE TIME WITHOUT SIMULATION            : ' + str(average_queue_time_without_simulation), end='\n\n')
    
    print('AVERAGE SYSTEM PROCESS TIME WITH SIMULATION      : ' + str(average_system_process_time_with_simulation))
    print('AVERAGE SYSTEM PROCESS TIME WITHOUT SIMULATION   : ' + str(average_system_process_time_without_simulation), end='\n\n')
    
    print('AVERAGE QUEUE LENGTH TIME WITH SIMULATION        : ' + str(average_queue_length_with_simulation))
    print('AVERAGE QUEUE LENGTH TIME WITHOUT SIMULATION     : ' + str(average_queue_length_without_simulation), end='\n\n')
    
    print('AVERAGE NUMBER IN THE SYSTEM WITH SIMULATION     : ' + str(average_number_in_system_with_simulation))
    print('AVERAGE NUMBER IN THE SYSTEM WITHOUT SIMULATION  : ' + str(average_number_in_system_without_simulation), end='\n\n')
    
    print('SERVICE POINT IDLE TIME WITH SIMULATION          : ' + str(average_service_point_idle_time_with_simulation))
    print('SERVICE POINT IDLE TIME WITHOUT SIMULATION       : ' + str(average_service_point_idle_time_without_simulation), end='\n\n\n')
        

def demo_2():
    arrival_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    inter_arrival_time   = [38, 3, 41, 20, 57, 10, 46, 99, 87, 221]
    service_time   = [136, 17, 23, 4, 70, 55, 36, 17, 12, 62]

    arrival_time = get_arrival_time(inter_arrival_time.copy())
    into_time = get_into_time(service_time, arrival_time)
    front_time = get_front_time(service_time, into_time)
    queue_time = get_queue_time(into_time, arrival_time)
    idle_time = get_idle_time(into_time, front_time)
    system_process_time = get_system_process_time(front_time, arrival_time)

    total_time = get_total_time(front_time)
    total_queue_time = get_total_queue_time(queue_time)
    total_idle_time = get_total_idle_time(idle_time)
    total_service_time = get_total_service_time(service_time)
    total_system_process_time = get_total_system_process_time(system_process_time)
    

    average_queue_time_with_simulation = get_average_queue_time_with_simulation(arrival_number, total_queue_time)

    average_system_process_time_with_simulation = get_average_system_process_time_with_simulation(arrival_number, total_system_process_time)

    average_queue_length_with_simulation = get_average_queue_length_with_simulation(total_time, total_queue_time)

    average_number_in_system_with_simulation = get_average_number_in_system_with_simulation(total_time, total_system_process_time)
        
    average_service_point_idle_time_with_simulation = get_average_service_point_idle_time_with_simulation(total_time, total_idle_time)
    

    # Diketahui dari soal
    inter_arrival_time_in_minute = 60
    service_time_in_minute = 40

    # Untuk mendapatkan interval arrival time
    myu = 3600 / inter_arrival_time_in_minute

    # Untuk mendapatkan interval service time
    lmbda = 3600 / service_time_in_minute


    average_queue_time_without_simulation = get_average_queue_time_without_simulation(myu, lmbda)
    average_system_process_time_without_simulation = get_average_system_process_time_without_simulation(myu, lmbda)
    average_queue_length_without_simulation = get_average_queue_length_without_simulation(myu, lmbda)
    average_number_in_system_without_simulation = get_average_number_in_system_without_simulation(myu, lmbda)
    average_service_point_idle_time_without_simulation = get_average_service_point_idle_time_without_simulation(
        average_service_point_idle_time_with_simulation)

    # PROSES

    row_names = ['ARRIVAL NUMBER','INTER ARRIVAL TIME', 'ARRIVAL TIME', 'SERVICE TIME',
                 'INTO TIME', 'FRONT TIME', 'QUEUE TIME','IDLE TIME', 'SYSTEM PROCESS TIME']

    print('\n TABEL 1\n')

    show_table(row_names[0:2], [arrival_number, inter_arrival_time])

    print('\nNILAI t DIDAPATKAN DARI ti = -myu ln Ri, DIMANA : \n\nMYU = {} / {}'
          .format(3600, inter_arrival_time_in_minute))
    print('    = {} % / JAM\n\n'.format(str(myu)))
    print('ti = -{} ln Ri'.format(myu))


    print('\n\n TABEL 2\n')

    show_table(row_names[3:4], [service_time])

    print('\nNILAI t DIDAPATKAN DARI ti = -lambda ln Ri, DIMANA : \n\nLAMBDA = {} / {}'
          .format(3600, service_time_in_minute))
    print('       = {} % / JAM\n\n'.format(str(lmbda)))
    print('ti = -{} ln Ri'.format(lmbda))

    
    print('\n\n TABEL 3\n')

    show_table(row_names, [arrival_number, inter_arrival_time,
                           arrival_time, service_time, into_time,
                           front_time, queue_time, idle_time,
                           system_process_time])

    print('\n\n\n DARI TABEL PERHITUNGAN ANTRIAN DAPAT DIKETAHUI BAHWA : \n')
    print('\tTOTAL TIME                  = {} (NILAI TERTINGGI FRONT TIME)\n'.format(str(total_time)))
    print('\tTOTAL QUEUE TIME            = {}'.format(' + '.join([str(t) for t in queue_time])))
    print('\t                            = {}\n'.format(str(total_queue_time)))
    
    print('\tTOTAL IDLE TIME             = {}'.format(' + '.join([str(t) for t in idle_time])))
    print('\t                            = {}\n'.format(str(total_idle_time)))

    print('\tTOTAL SYSTEM PROCESS TIME   = {}'.format(' + '.join([str(t) for t in system_process_time])))
    print('\t                            = {}\n'.format(str(total_system_process_time)))
    
    print('\tTOTAL SERVICE TIME          = {}'.format(' + '.join([str(t) for t in service_time])))
    print('\t                            = {}\n'.format(str(total_service_time)))



    print('\n\n DARI TABEL 3 DIDAPATKAN : \n')

    print('\t1. AVERAGE QUEUE TIME\n')
    print('\t   A. DENGAN SIMULASI\n')
    print('\t\tQt = queue time / banyak kedatangan')
    print('\t\t   = {} / {}'.format(total_queue_time, str(len(arrival_number))))
    print('\t\t   = {} detik\n\n'.format(average_queue_time_with_simulation))

    print('\t   B. TANPA SIMULASI\n')
    print('\t\tWg = ( myu / (lambda * (lambda - myu)) ) * 3600')
    print('\t\t   = ( {} / ({} * ({} - {})) ) * {}'.format(myu, lmbda, lmbda, myu, 3600))
    print('\t\t   = ({} / {}) * {}'.format(myu, str(lmbda * (lmbda - myu)), 3600))
    print('\t\t   = {} * {}'.format(str(myu / (lmbda * (lmbda - myu))), 3600))
    print('\t\t   = {} detik\n\n'.format(str(average_queue_time_without_simulation)))



    print('\t2. AVERAGE SYSTEM PROCESS TIME\n')
    print('\t   A. DENGAN SIMULASI\n')
    print('\t\tWS = total system process time / banyak kedatangan')
    print('\t\t   = {} / {}'.format(total_system_process_time, str(len(arrival_number))))
    print('\t\t   = {} detik\n\n'.format(average_system_process_time_with_simulation))

    print('\t   B. TANPA SIMULASI\n')
    print('\t\tW  = 1 / (lambda - myu) * 3600')
    print('\t\t   = 1 / ({} - {}) * {}'.format(lmbda, myu, 3600))
    print('\t\t   = {} detik\n\n'.format(str(average_system_process_time_without_simulation)))




    print('\t3. AVERAGE QUEUE LENGTH\n')
    print('\t   A. DENGAN SIMULASI\n')
    print('\t\tLgs = total queue time / total time')
    print('\t\t    = {} / {}'.format(total_queue_time, str(total_time)))
    print('\t\t    = {}\n\n'.format(average_queue_length_with_simulation))

    print('\t   B. TANPA SIMULASI\n')
    print('\t\tLg  = myu^2 / lambda(lambda - myu)')
    print('\t\t    = {}^2 / {}({} - {})'.format(myu, lmbda, lmbda, myu))
    print('\t\t    = {} / {}'.format(myu**2, (lmbda * (lmbda - myu))))
    print('\t\t    = {}\n\n'.format(str(average_queue_length_without_simulation)))





    print('\t4. AVERAGE NUMBER IN THE SYSTEM\n')
    print('\t   A. DENGAN SIMULASI\n')
    print('\t\tls = total system process time / total time')
    print('\t\t   = {} / {}'.format(total_system_process_time, str(total_time)))
    print('\t\t   = {}\n\n'.format(average_number_in_system_with_simulation))

    print('\t   B. TANPA SIMULASI\n')
    print('\t\tl  = myu / (lambda - myu)')
    print('\t\t   = {} /  ({} - {})'.format(myu, lmbda, myu))
    print('\t\t   = {} / {}'.format(myu, (lmbda - myu)))
    print('\t\t   = {}\n\n'.format(str(average_number_in_system_without_simulation)))




    print('\t5. SERVICE POINT IDLE TIME\n')
    print('\t   A. DENGAN SIMULASI\n')
    print('\t\tRatio Idle Time = total idle time / total time')
    print('\t\t                = {} / {}'.format(total_idle_time, str(total_time)))
    print('\t\t                = {}\n\n'.format(average_service_point_idle_time_with_simulation))

    print('\t   B. TANPA SIMULASI\n')
    print('\t\tspi = rit * 100')
    print('\t\t    = {}'.format(average_service_point_idle_time_with_simulation * 100))
    print('\t\t    = {}%\n\n\n\n'.format(str(round(average_service_point_idle_time_with_simulation * 100))))



    print('ARRIVAL NUMBER       : ' + str(arrival_number))
    print('INTER ARRIVAL TIME   : ' + str(inter_arrival_time))
    print('ARRIVAL TIME         : ' + str(arrival_time))
    print('SERVICE TIME         : ' + str(service_time))
    print('INTO TIME            : ' + str(into_time))
    print('FRONT TIME           : ' + str(front_time))
    print('QUEUE TIME           : ' + str(queue_time))
    print('IDLE TIME            : ' + str(idle_time))
    print('SYSTEM PROCESS TIME  : ' + str(system_process_time), end='\n\n\n')

    print('TOTAL TIME                  : ' + str(total_time))
    print('TOTAL QUEUE TIME            : ' + str(total_queue_time))
    print('TOTAL IDLE TIME             : ' + str(total_idle_time))
    print('TOTAL SYSTEM PROCESS TIME   : ' + str(total_system_process_time), end='\n\n\n')

    
    print('AVERAGE QUEUE TIME WITH SIMULATION               : ' + str(average_queue_time_with_simulation))
    print('AVERAGE QUEUE TIME WITHOUT SIMULATION            : ' + str(average_queue_time_without_simulation), end='\n\n')
    
    print('AVERAGE SYSTEM PROCESS TIME WITH SIMULATION      : ' + str(average_system_process_time_with_simulation))
    print('AVERAGE SYSTEM PROCESS TIME WITHOUT SIMULATION   : ' + str(average_system_process_time_without_simulation), end='\n\n')
    
    print('AVERAGE QUEUE LENGTH TIME WITH SIMULATION        : ' + str(average_queue_length_with_simulation))
    print('AVERAGE QUEUE LENGTH TIME WITHOUT SIMULATION     : ' + str(average_queue_length_without_simulation), end='\n\n')
    
    print('AVERAGE NUMBER IN THE SYSTEM WITH SIMULATION     : ' + str(average_number_in_system_with_simulation))
    print('AVERAGE NUMBER IN THE SYSTEM WITHOUT SIMULATION  : ' + str(average_number_in_system_without_simulation), end='\n\n')
    
    print('SERVICE POINT IDLE TIME WITH SIMULATION          : ' + str(average_service_point_idle_time_with_simulation))
    print('SERVICE POINT IDLE TIME WITHOUT SIMULATION       : ' + str(average_service_point_idle_time_without_simulation), end='\n\n\n')



def demo_3():
    arrival_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    inter_arrival_time   = [41, 43, 48, 56, 60, 68, 71, 78, 83, 84]
    
    service_time   = [3, 4, 3, 3, 2, 4, 3, 2, 5, 3]

    arrival_time = get_arrival_time(inter_arrival_time.copy())
    into_time = get_into_time(service_time, arrival_time)
    front_time = get_front_time(service_time, into_time)
    queue_time = get_queue_time(into_time, arrival_time)
    idle_time = get_idle_time(into_time, front_time)
    system_process_time = get_system_process_time(front_time, arrival_time)

    total_time = get_total_time(front_time)
    total_queue_time = get_total_queue_time(queue_time)
    total_idle_time = get_total_idle_time(idle_time)
    total_service_time = get_total_service_time(service_time)
    total_system_process_time = get_total_system_process_time(system_process_time)
    

    average_queue_time_with_simulation = get_average_queue_time_with_simulation(arrival_number, total_queue_time)

    average_system_process_time_with_simulation = get_average_system_process_time_with_simulation(arrival_number, total_system_process_time)

    average_queue_length_with_simulation = get_average_queue_length_with_simulation(total_time, total_queue_time)

    average_number_in_system_with_simulation = get_average_number_in_system_with_simulation(total_time, total_system_process_time)
        
    average_service_point_idle_time_with_simulation = get_average_service_point_idle_time_with_simulation(total_time, total_idle_time)
    

    # Diketahui dari soal
    inter_arrival_time_in_minute = 60
    service_time_in_minute = 40

    # Untuk mendapatkan interval arrival time
    myu = 3600 / inter_arrival_time_in_minute

    # Untuk mendapatkan interval service time
    lmbda = 3600 / service_time_in_minute


    average_queue_time_without_simulation = get_average_queue_time_without_simulation(myu, lmbda)
    average_system_process_time_without_simulation = get_average_system_process_time_without_simulation(myu, lmbda)
    average_queue_length_without_simulation = get_average_queue_length_without_simulation(myu, lmbda)
    average_number_in_system_without_simulation = get_average_number_in_system_without_simulation(myu, lmbda)
    average_service_point_idle_time_without_simulation = get_average_service_point_idle_time_without_simulation(
        average_service_point_idle_time_with_simulation)

    # PROSES

    row_names = ['ARRIVAL NUMBER','INTER ARRIVAL TIME', 'ARRIVAL TIME', 'SERVICE TIME',
                 'INTO TIME', 'FRONT TIME', 'QUEUE TIME','IDLE TIME', 'SYSTEM PROCESS TIME']

    print('\n TABEL 1\n')

    show_table(row_names[0:2], [arrival_number, inter_arrival_time])

    print('\nNILAI t DIDAPATKAN DARI ti = -myu ln Ri, DIMANA : \n\nMYU = {} / {}'
          .format(3600, inter_arrival_time_in_minute))
    print('    = {} % / JAM\n\n'.format(str(myu)))
    print('ti = -{} ln Ri'.format(myu))


    

    print('\n\n TABEL 2\n')

    show_table(row_names[3:4], [service_time])

    print('\nNILAI t DIDAPATKAN DARI ti = -lambda ln Ri, DIMANA : \n\nLAMBDA = {} / {}'
          .format(3600, service_time_in_minute))
    print('       = {} % / JAM\n\n'.format(str(lmbda)))
    print('ti = -{} ln Ri'.format(lmbda))


    

    print('\n\n TABEL 3\n')

    show_table(row_names, [arrival_number, inter_arrival_time,
                           arrival_time, service_time, into_time,
                           front_time, queue_time, idle_time,
                           system_process_time])

    print('\n\n\n DARI TABEL PERHITUNGAN ANTRIAN DAPAT DIKETAHUI BAHWA : \n')
    print('\tTOTAL TIME                  = {} (NILAI TERTINGGI FRONT TIME)\n'.format(str(total_time)))
    print('\tTOTAL QUEUE TIME            = {}'.format(' + '.join([str(t) for t in queue_time])))
    print('\t                            = {}\n'.format(str(total_queue_time)))
    
    print('\tTOTAL IDLE TIME             = {}'.format(' + '.join([str(t) for t in idle_time])))
    print('\t                            = {}\n'.format(str(total_idle_time)))

    print('\tTOTAL SYSTEM PROCESS TIME   = {}'.format(' + '.join([str(t) for t in system_process_time])))
    print('\t                            = {}\n'.format(str(total_system_process_time)))
    
    print('\tTOTAL SERVICE TIME          = {}'.format(' + '.join([str(t) for t in service_time])))
    print('\t                            = {}\n'.format(str(total_service_time)))



    print('\n\n DARI TABEL 3 DIDAPATKAN : \n')

    print('\t1. AVERAGE QUEUE TIME\n')
    print('\t   A. DENGAN SIMULASI\n')
    print('\t\tQt = queue time / banyak kedatangan')
    print('\t\t   = {} / {}'.format(total_queue_time, str(len(arrival_number))))
    print('\t\t   = {} detik\n\n'.format(average_queue_time_with_simulation))

    print('\t   B. TANPA SIMULASI\n')
    print('\t\tWg = ( myu / (lambda * (lambda - myu)) ) * 3600')
    print('\t\t   = ( {} / ({} * ({} - {})) ) * {}'.format(myu, lmbda, lmbda, myu, 3600))
    print('\t\t   = ({} / {}) * {}'.format(myu, str(lmbda * (lmbda - myu)), 3600))
    print('\t\t   = {} * {}'.format(str(myu / (lmbda * (lmbda - myu))), 3600))
    print('\t\t   = {} detik\n\n'.format(str(average_queue_time_without_simulation)))



    print('\t2. AVERAGE SYSTEM PROCESS TIME\n')
    print('\t   A. DENGAN SIMULASI\n')
    print('\t\tWS = total system process time / banyak kedatangan')
    print('\t\t   = {} / {}'.format(total_system_process_time, str(len(arrival_number))))
    print('\t\t   = {} detik\n\n'.format(average_system_process_time_with_simulation))

    print('\t   B. TANPA SIMULASI\n')
    print('\t\tW  = 1 / (lambda - myu) * 3600')
    print('\t\t   = 1 / ({} - {}) * {}'.format(lmbda, myu, 3600))
    print('\t\t   = {} detik\n\n'.format(str(average_system_process_time_without_simulation)))




    print('\t3. AVERAGE QUEUE LENGTH\n')
    print('\t   A. DENGAN SIMULASI\n')
    print('\t\tLgs = total queue time / total time')
    print('\t\t    = {} / {}'.format(total_queue_time, str(total_time)))
    print('\t\t    = {}\n\n'.format(average_queue_length_with_simulation))

    print('\t   B. TANPA SIMULASI\n')
    print('\t\tLg  = myu^2 / lambda(lambda - myu)')
    print('\t\t    = {}^2 / {}({} - {})'.format(myu, lmbda, lmbda, myu))
    print('\t\t    = {} / {}'.format(myu**2, (lmbda * (lmbda - myu))))
    print('\t\t    = {}\n\n'.format(str(average_queue_length_without_simulation)))





    print('\t4. AVERAGE NUMBER IN THE SYSTEM\n')
    print('\t   A. DENGAN SIMULASI\n')
    print('\t\tls = total system process time / total time')
    print('\t\t   = {} / {}'.format(total_system_process_time, str(total_time)))
    print('\t\t   = {}\n\n'.format(average_number_in_system_with_simulation))

    print('\t   B. TANPA SIMULASI\n')
    print('\t\tl  = myu / (lambda - myu)')
    print('\t\t   = {} /  ({} - {})'.format(myu, lmbda, myu))
    print('\t\t   = {} / {}'.format(myu, (lmbda - myu)))
    print('\t\t   = {}\n\n'.format(str(average_number_in_system_without_simulation)))




    print('\t5. SERVICE POINT IDLE TIME\n')
    print('\t   A. DENGAN SIMULASI\n')
    print('\t\tRatio Idle Time = total idle time / total time')
    print('\t\t                = {} / {}'.format(total_idle_time, str(total_time)))
    print('\t\t                = {}\n\n'.format(average_service_point_idle_time_with_simulation))

    print('\t   B. TANPA SIMULASI\n')
    print('\t\tspi = rit * 100')
    print('\t\t    = {}'.format(average_service_point_idle_time_with_simulation * 100))
    print('\t\t    = {}%\n\n\n\n'.format(str(round(average_service_point_idle_time_with_simulation * 100))))



    print('ARRIVAL NUMBER       : ' + str(arrival_number))
    print('INTER ARRIVAL TIME   : ' + str(inter_arrival_time))
    print('ARRIVAL TIME         : ' + str(arrival_time))
    print('SERVICE TIME         : ' + str(service_time))
    print('INTO TIME            : ' + str(into_time))
    print('FRONT TIME           : ' + str(front_time))
    print('QUEUE TIME           : ' + str(queue_time))
    print('IDLE TIME            : ' + str(idle_time))
    print('SYSTEM PROCESS TIME  : ' + str(system_process_time), end='\n\n\n')

    print('TOTAL TIME                  : ' + str(total_time))
    print('TOTAL QUEUE TIME            : ' + str(total_queue_time))
    print('TOTAL IDLE TIME             : ' + str(total_idle_time))
    print('TOTAL SYSTEM PROCESS TIME   : ' + str(total_system_process_time), end='\n\n\n')

    
    print('AVERAGE QUEUE TIME WITH SIMULATION               : ' + str(average_queue_time_with_simulation))
    print('AVERAGE QUEUE TIME WITHOUT SIMULATION            : ' + str(average_queue_time_without_simulation), end='\n\n')
    
    print('AVERAGE SYSTEM PROCESS TIME WITH SIMULATION      : ' + str(average_system_process_time_with_simulation))
    print('AVERAGE SYSTEM PROCESS TIME WITHOUT SIMULATION   : ' + str(average_system_process_time_without_simulation), end='\n\n')
    
    print('AVERAGE QUEUE LENGTH TIME WITH SIMULATION        : ' + str(average_queue_length_with_simulation))
    print('AVERAGE QUEUE LENGTH TIME WITHOUT SIMULATION     : ' + str(average_queue_length_without_simulation), end='\n\n')
    
    print('AVERAGE NUMBER IN THE SYSTEM WITH SIMULATION     : ' + str(average_number_in_system_with_simulation))
    print('AVERAGE NUMBER IN THE SYSTEM WITHOUT SIMULATION  : ' + str(average_number_in_system_without_simulation), end='\n\n')
    
    print('SERVICE POINT IDLE TIME WITH SIMULATION          : ' + str(average_service_point_idle_time_with_simulation))
    print('SERVICE POINT IDLE TIME WITHOUT SIMULATION       : ' + str(average_service_point_idle_time_without_simulation), end='\n\n\n')


def demo_4():
    arrival_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    inter_arrival_time   = [10, 5, 25, 30, 25, 70, 75, 5, 15, 3]
    service_time   = [20, 50, 127, 136, 201, 25, 70, 75, 80, 90]


    arrival_time = get_arrival_time(inter_arrival_time.copy())
    into_time = get_into_time(service_time, arrival_time)
    front_time = get_front_time(service_time, into_time)
    queue_time = get_queue_time(into_time, arrival_time)
    idle_time = get_idle_time(into_time, front_time)
    system_process_time = get_system_process_time(front_time, arrival_time)

    total_time = get_total_time(front_time)
    total_queue_time = get_total_queue_time(queue_time)
    total_idle_time = get_total_idle_time(idle_time)
    total_service_time = get_total_service_time(service_time)
    total_system_process_time = get_total_system_process_time(system_process_time)
    

    average_queue_time_with_simulation = get_average_queue_time_with_simulation(arrival_number, total_queue_time)

    average_system_process_time_with_simulation = get_average_system_process_time_with_simulation(arrival_number, total_system_process_time)

    average_queue_length_with_simulation = get_average_queue_length_with_simulation(total_time, total_queue_time)

    average_number_in_system_with_simulation = get_average_number_in_system_with_simulation(total_time, total_system_process_time)
        
    average_service_point_idle_time_with_simulation = get_average_service_point_idle_time_with_simulation(total_time, total_idle_time)
    

    # Diketahui dari soal
    inter_arrival_time_in_minute = 60
    service_time_in_minute = 40

    # Untuk mendapatkan interval arrival time
    myu = 3600 / inter_arrival_time_in_minute

    # Untuk mendapatkan interval service time
    lmbda = 3600 / service_time_in_minute


    average_queue_time_without_simulation = get_average_queue_time_without_simulation(myu, lmbda)
    average_system_process_time_without_simulation = get_average_system_process_time_without_simulation(myu, lmbda)
    average_queue_length_without_simulation = get_average_queue_length_without_simulation(myu, lmbda)
    average_number_in_system_without_simulation = get_average_number_in_system_without_simulation(myu, lmbda)
    average_service_point_idle_time_without_simulation = get_average_service_point_idle_time_without_simulation(
        average_service_point_idle_time_with_simulation)

    print('ARRIVAL NUMBER       : ' + str(arrival_number))
    print('INTER ARRIVAL TIME   : ' + str(inter_arrival_time))
    print('ARRIVAL TIME         : ' + str(arrival_time))
    print('SERVICE TIME         : ' + str(service_time))
    print('INTO TIME            : ' + str(into_time))
    print('FRONT TIME           : ' + str(front_time))
    print('QUEUE TIME           : ' + str(queue_time))
    print('IDLE TIME            : ' + str(idle_time))
    print('SYSTEM PROCESS TIME  : ' + str(system_process_time), end='\n\n\n')

    print('TOTAL TIME                  : ' + str(total_time))
    print('TOTAL QUEUE TIME            : ' + str(total_queue_time))
    print('TOTAL IDLE TIME             : ' + str(total_idle_time))
    print('TOTAL SYSTEM PROCESS TIME   : ' + str(total_system_process_time), end='\n\n\n')

    
    print('AVERAGE QUEUE TIME WITH SIMULATION               : ' + str(average_queue_time_with_simulation))
    print('AVERAGE QUEUE TIME WITHOUT SIMULATION            : ' + str(average_queue_time_without_simulation), end='\n\n')
    
    print('AVERAGE SYSTEM PROCESS TIME WITH SIMULATION      : ' + str(average_system_process_time_with_simulation))
    print('AVERAGE SYSTEM PROCESS TIME WITHOUT SIMULATION   : ' + str(average_system_process_time_without_simulation), end='\n\n')
    
    print('AVERAGE QUEUE LENGTH TIME WITH SIMULATION        : ' + str(average_queue_length_with_simulation))
    print('AVERAGE QUEUE LENGTH TIME WITHOUT SIMULATION     : ' + str(average_queue_length_without_simulation), end='\n\n')
    
    print('AVERAGE NUMBER IN THE SYSTEM WITH SIMULATION     : ' + str(average_number_in_system_with_simulation))
    print('AVERAGE NUMBER IN THE SYSTEM WITHOUT SIMULATION  : ' + str(average_number_in_system_without_simulation), end='\n\n')
    
    print('SERVICE POINT IDLE TIME WITH SIMULATION          : ' + str(average_service_point_idle_time_with_simulation))
    print('SERVICE POINT IDLE TIME WITHOUT SIMULATION       : ' + str(average_service_point_idle_time_without_simulation), end='\n\n\n')


def demo_5():
    arrival_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    inter_arrival_time   = [38, 28, 75, 66, 62, 3, 75, 41, 88, 78]
    service_time   = [22, 16, 97, 41, 72, 66, 47, 91, 22, 16]

    arrival_time = get_arrival_time(inter_arrival_time.copy())
    into_time = get_into_time(service_time, arrival_time)
    front_time = get_front_time(service_time, into_time)
    queue_time = get_queue_time(into_time, arrival_time)
    idle_time = get_idle_time(into_time, front_time)
    system_process_time = get_system_process_time(front_time, arrival_time)

    total_time = get_total_time(front_time)
    total_queue_time = get_total_queue_time(queue_time)
    total_idle_time = get_total_idle_time(idle_time)
    total_service_time = get_total_service_time(service_time)
    total_system_process_time = get_total_system_process_time(system_process_time)
    

    average_queue_time_with_simulation = get_average_queue_time_with_simulation(arrival_number, total_queue_time)

    average_system_process_time_with_simulation = get_average_system_process_time_with_simulation(arrival_number, total_system_process_time)

    average_queue_length_with_simulation = get_average_queue_length_with_simulation(total_time, total_queue_time)

    average_number_in_system_with_simulation = get_average_number_in_system_with_simulation(total_time, total_system_process_time)
        
    average_service_point_idle_time_with_simulation = get_average_service_point_idle_time_with_simulation(total_time, total_idle_time)
    

    # Diketahui dari soal
    inter_arrival_time_in_minute = 15
    service_time_in_minute = 5

    # Untuk mendapatkan interval arrival time
    myu = 3600 / inter_arrival_time_in_minute

    # Untuk mendapatkan interval service time
    lmbda = 3600 / service_time_in_minute


    average_queue_time_without_simulation = get_average_queue_time_without_simulation(myu, lmbda)
    average_system_process_time_without_simulation = get_average_system_process_time_without_simulation(myu, lmbda)
    average_queue_length_without_simulation = get_average_queue_length_without_simulation(myu, lmbda)
    average_number_in_system_without_simulation = get_average_number_in_system_without_simulation(myu, lmbda)
    average_service_point_idle_time_without_simulation = get_average_service_point_idle_time_without_simulation(
        average_service_point_idle_time_with_simulation)

    # PROSES

    row_names = ['ARRIVAL NUMBER','INTER ARRIVAL TIME', 'ARRIVAL TIME', 'SERVICE TIME',
                 'INTO TIME', 'FRONT TIME', 'QUEUE TIME','IDLE TIME', 'SYSTEM PROCESS TIME']

    print('\n TABEL 1\n')

    show_table(row_names[0:2], [arrival_number, inter_arrival_time])

    print('\nNILAI t DIDAPATKAN DARI ti = -myu ln Ri, DIMANA : \n\nMYU = {} / {}'
          .format(3600, inter_arrival_time_in_minute))
    print('    = {} % / JAM\n\n'.format(str(myu)))
    print('ti = -{} ln Ri'.format(myu))


    

    print('\n\n TABEL 2\n')

    show_table(row_names[3:4], [service_time])

    print('\nNILAI t DIDAPATKAN DARI ti = -lambda ln Ri, DIMANA : \n\nLAMBDA = {} / {}'
          .format(3600, service_time_in_minute))
    print('       = {} % / JAM\n\n'.format(str(lmbda)))
    print('ti = -{} ln Ri'.format(lmbda))


    

    print('\n\n TABEL 3\n')

    show_table(row_names, [arrival_number, inter_arrival_time,
                           arrival_time, service_time, into_time,
                           front_time, queue_time, idle_time,
                           system_process_time])

    print('\n\n\n DARI TABEL PERHITUNGAN ANTRIAN DAPAT DIKETAHUI BAHWA : \n')
    print('\tTOTAL TIME                  = {} (NILAI TERTINGGI FRONT TIME)\n'.format(str(total_time)))
    print('\tTOTAL QUEUE TIME            = {}'.format(' + '.join([str(t) for t in queue_time])))
    print('\t                            = {}\n'.format(str(total_queue_time)))
    
    print('\tTOTAL IDLE TIME             = {}'.format(' + '.join([str(t) for t in idle_time])))
    print('\t                            = {}\n'.format(str(total_idle_time)))

    print('\tTOTAL SYSTEM PROCESS TIME   = {}'.format(' + '.join([str(t) for t in system_process_time])))
    print('\t                            = {}\n'.format(str(total_system_process_time)))
    
    print('\tTOTAL SERVICE TIME          = {}'.format(' + '.join([str(t) for t in service_time])))
    print('\t                            = {}\n'.format(str(total_service_time)))



    print('\n\n DARI TABEL 3 DIDAPATKAN : \n')

    print('\t1. AVERAGE QUEUE TIME\n')
    print('\t   A. DENGAN SIMULASI\n')
    print('\t\tQt = queue time / banyak kedatangan')
    print('\t\t   = {} / {}'.format(total_queue_time, str(len(arrival_number))))
    print('\t\t   = {} detik\n\n'.format(average_queue_time_with_simulation))

    print('\t   B. TANPA SIMULASI\n')
    print('\t\tWg = ( myu / (lambda * (lambda - myu)) ) * 3600')
    print('\t\t   = ( {} / ({} * ({} - {})) ) * {}'.format(myu, lmbda, lmbda, myu, 3600))
    print('\t\t   = ({} / {}) * {}'.format(myu, str(lmbda * (lmbda - myu)), 3600))
    print('\t\t   = {} * {}'.format(str(myu / (lmbda * (lmbda - myu))), 3600))
    print('\t\t   = {} detik\n\n'.format(str(average_queue_time_without_simulation)))



    print('\t2. AVERAGE SYSTEM PROCESS TIME\n')
    print('\t   A. DENGAN SIMULASI\n')
    print('\t\tWS = total system process time / banyak kedatangan')
    print('\t\t   = {} / {}'.format(total_system_process_time, str(len(arrival_number))))
    print('\t\t   = {} detik\n\n'.format(average_system_process_time_with_simulation))

    print('\t   B. TANPA SIMULASI\n')
    print('\t\tW  = 1 / (lambda - myu) * 3600')
    print('\t\t   = 1 / ({} - {}) * {}'.format(lmbda, myu, 3600))
    print('\t\t   = {} detik\n\n'.format(str(average_system_process_time_without_simulation)))




    print('\t3. AVERAGE QUEUE LENGTH\n')
    print('\t   A. DENGAN SIMULASI\n')
    print('\t\tLgs = total queue time / total time')
    print('\t\t    = {} / {}'.format(total_queue_time, str(total_time)))
    print('\t\t    = {}\n\n'.format(average_queue_length_with_simulation))

    print('\t   B. TANPA SIMULASI\n')
    print('\t\tLg  = myu^2 / lambda(lambda - myu)')
    print('\t\t    = {}^2 / {}({} - {})'.format(myu, lmbda, lmbda, myu))
    print('\t\t    = {} / {}'.format(myu**2, (lmbda * (lmbda - myu))))
    print('\t\t    = {}\n\n'.format(str(average_queue_length_without_simulation)))



    print('\t4. AVERAGE NUMBER IN THE SYSTEM\n')
    print('\t   A. DENGAN SIMULASI\n')
    print('\t\tls = total system process time / total time')
    print('\t\t   = {} / {}'.format(total_system_process_time, str(total_time)))
    print('\t\t   = {}\n\n'.format(average_number_in_system_with_simulation))

    print('\t   B. TANPA SIMULASI\n')
    print('\t\tl  = myu / (lambda - myu)')
    print('\t\t   = {} /  ({} - {})'.format(myu, lmbda, myu))
    print('\t\t   = {} / {}'.format(myu, (lmbda - myu)))
    print('\t\t   = {}\n\n'.format(str(average_number_in_system_without_simulation)))


    print('\t5. SERVICE POINT IDLE TIME\n')
    print('\t   A. DENGAN SIMULASI\n')
    print('\t\tRatio Idle Time = total idle time / total time')
    print('\t\t                = {} / {}'.format(total_idle_time, str(total_time)))
    print('\t\t                = {}\n\n'.format(average_service_point_idle_time_with_simulation))

    print('\t   B. TANPA SIMULASI\n')
    print('\t\tspi = rit * 100')
    print('\t\t    = {}'.format(average_service_point_idle_time_with_simulation * 100))
    print('\t\t    = {}%\n\n\n\n'.format(str(round(average_service_point_idle_time_with_simulation * 100))))



    print('ARRIVAL NUMBER       : ' + str(arrival_number))
    print('INTER ARRIVAL TIME   : ' + str(inter_arrival_time))
    print('ARRIVAL TIME         : ' + str(arrival_time))
    print('SERVICE TIME         : ' + str(service_time))
    print('INTO TIME            : ' + str(into_time))
    print('FRONT TIME           : ' + str(front_time))
    print('QUEUE TIME           : ' + str(queue_time))
    print('IDLE TIME            : ' + str(idle_time))
    print('SYSTEM PROCESS TIME  : ' + str(system_process_time), end='\n\n\n')

    print('TOTAL TIME                  : ' + str(total_time))
    print('TOTAL QUEUE TIME            : ' + str(total_queue_time))
    print('TOTAL IDLE TIME             : ' + str(total_idle_time))
    print('TOTAL SYSTEM PROCESS TIME   : ' + str(total_system_process_time), end='\n\n\n')

    
    print('AVERAGE QUEUE TIME WITH SIMULATION               : ' + str(average_queue_time_with_simulation))
    print('AVERAGE QUEUE TIME WITHOUT SIMULATION            : ' + str(average_queue_time_without_simulation), end='\n\n')
    
    print('AVERAGE SYSTEM PROCESS TIME WITH SIMULATION      : ' + str(average_system_process_time_with_simulation))
    print('AVERAGE SYSTEM PROCESS TIME WITHOUT SIMULATION   : ' + str(average_system_process_time_without_simulation), end='\n\n')
    
    print('AVERAGE QUEUE LENGTH TIME WITH SIMULATION        : ' + str(average_queue_length_with_simulation))
    print('AVERAGE QUEUE LENGTH TIME WITHOUT SIMULATION     : ' + str(average_queue_length_without_simulation), end='\n\n')
    
    print('AVERAGE NUMBER IN THE SYSTEM WITH SIMULATION     : ' + str(average_number_in_system_with_simulation))
    print('AVERAGE NUMBER IN THE SYSTEM WITHOUT SIMULATION  : ' + str(average_number_in_system_without_simulation), end='\n\n')
    
    print('SERVICE POINT IDLE TIME WITH SIMULATION          : ' + str(average_service_point_idle_time_with_simulation))
    print('SERVICE POINT IDLE TIME WITHOUT SIMULATION       : ' + str(average_service_point_idle_time_without_simulation), end='\n\n\n')

if __name__ == '__main__':
    demo_5()

   

    

    

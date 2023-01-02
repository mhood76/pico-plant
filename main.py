import utime
from pico_network import connect_network, disconnect_network
from get_measure import get_moisture
from log_measure import log_local, log_remote


def main():
#    disconnect_network()
#    ip = connect_network()
#    result, gpio, ts = get_moisture(28) # returns `round(moisture reading)`
#    
#    result_cal_dic = { '001' : {"dry": 11111, "wet": 99999 },
#                      'gpio' : 28,
#                      'measured_on' : utime.time()}
#    
#    gpio = result_cal_dic['gpio']
#    result_mea = 99999 
#    pico_ts = utime.time()
#    
#    result_mea_dic = {f'001-{pico_ts}' : {'gpio' : gpio,
#                                          'process_step' : 'auto',
#                                          'measure_value' : result_mea}
#                      }
#    
#    log_local(result_mea_dic, 'mea')
#    log_local(result_cal_dic, 'cal')
#    result = "Hello World!"
#    log_remote(result)

if __name__ == "__main__":
    main()
    

import logging as log

# Order:
# Debug
# Info
# Warning
# Error
# Critical

# Minimum Level
# Handler = Manejador
log.basicConfig(level=log.DEBUG, 
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[log.FileHandler('data_layer.log', encoding='UTF-8'),
                          log.StreamHandler()])

if __name__ == '__main__':
  log.debug('Mensaje a nivel de DEBUG')
  log.info('Mensaje a nivel de INFO')
  log.warning('Mensaje a nivel de WARNING')
  log.error('Mensaje a nivel de ERROR')
  log.critical('Mensaje a nivel de CRITICAL')


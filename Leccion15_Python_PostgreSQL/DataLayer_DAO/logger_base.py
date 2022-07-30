import logging as log

# Order:
# Debug
# Info
# Warning
# Error
# Critical

# Minimum Level
log.basicConfig(level=log.DEBUG)

if __name__ == '__main__':
  log.debug('Mensaje a nivel de DEBUG')
  log.info('Mensaje a nivel de INFO')
  log.warning('Mensaje a nivel de WARNING')
  log.error('Mensaje a nivel de ERROR')
  log.critical('Mensaje a nivel de CRITICAL')


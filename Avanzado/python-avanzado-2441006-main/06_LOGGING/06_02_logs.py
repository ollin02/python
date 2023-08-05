import logging

#eligimos el nivel del log para imprimir
logging.basicConfig(level=logging.DEBUG)
#normalmente se guardan en archivos
logging.basicConfig(level=logging.DEBUG, filename="ejemplo_logs.log", filemode="w")

logging.debug("Log de debugging") # no se imprimen estos errore porque no son de primer nivel
logging.info("Log informativo") # no se imprimen estos errore porque no son de primer nivel
logging.warning("Log de advertencia") # WARNNING: root: Log de advertencia
logging.error("Log de error") # ERROR: root: Log de error
logging.critical("Log de error crítico") # CRITICAL: root: Log de error crítico

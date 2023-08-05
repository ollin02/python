#log_handlers hace referencia a controlador de log o de regirstros
#se configuran los logggers
#envia los registros de diferente manera stringhandler para consola 
#y file handler para archivo.
#smpthandler para imails
import logging 

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # se define el nivel del log

handler_consola = logging.StreamHandler() #controlador para la consola
formato_logs = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")#formato del log
handler_consola.setFormatter(formato_logs)#formato de los log
logger.addHandler(handler_consola)#definir el loger al cual pertenece el contolador que estamos creando

handler_archivo = logging.FileHandler("archivo.log")#se almacena el log en un archivo
handler_archivo.setLevel(logging.ERROR)# se define el nivel del log
handler_archivo.setFormatter(formato_logs)#formato de los log
logger.addHandler(handler_archivo)# definimos en donde pertenece

logger.info("registro informativo") #log tipo informativo


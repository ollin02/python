import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",# se pone la s paraa indicar a python que son string
    datefmt="%H:%M:%S"
)

nombre = "Paco"
logging.error(f"{nombre} creó el error")

logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")

try:
    division = 2 / 0
except:
    logging.error("División por cero")

try:
    division = 2 / 0
except:
    logging.exception("División por cero")# Nos indica el tipo de eroror


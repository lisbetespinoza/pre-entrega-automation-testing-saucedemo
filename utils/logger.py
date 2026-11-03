#Armado del log

import pathlib
from datetime import datetime
import logging

logs_dir = pathlib.Path("logs")
logs_dir.mkdir(exist_ok=True)


timestamp = datetime.now().strftime("%d%m%Y_%H%M%S") #paso la fecha/hora a string


logging.basicConfig(
    filename = logs_dir / f"log_{timestamp}.log",
    level = logging.INFO, #contiene los log warning, critico, etc.
    format= "%(asctime)s %(levelname)s %(name)s %(message)s",
    #define la fecha/hora del evento, nivel si es critico si es warning, critico, error, etc, nombre y mensaje.
    force= True
)

logger = logging.getLogger("talento_tech")


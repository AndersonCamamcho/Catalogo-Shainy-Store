import time
import logging

logging.basicConfig(level=logging.DEBUG,  # Establece el nivel de registro
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

inicio_tiempo = time.time()
name = 'ander'
logging.info("Hola, bebe quemaspues?" )
num1 = 3
logging.info("Hola, bebe quemaspues?")
logging.info("Hola, bebe quemaspues?" )
logging.info("Hola, bebe quemaspues?" )
num2 = 5
logging.info("Hola, bebe quemaspues?" )
time.sleep(3)
logging.info("Hola, bebe quemaspues?" )
numsu = num2+num1
logging.info("Hola, bebe quemaspues?" )
logging.info("Hola, bebe quemaspues?" )
fin_tiempo = time.time()
duracion = fin_tiempo - inicio_tiempo

logging.info(f"La ejecución tomó {duracion} segundos.")

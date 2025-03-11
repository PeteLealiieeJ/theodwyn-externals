#!/usr/bin/python3.8
from theodwyn_externals.controllers.gamepad import ExternalXboxGamePad
from rohan.common.logging                   import Logger
from time                                   import sleep

ADDR        = "udp://192.168.1.48:5555"
DATAFORMAT  = "17f"
TOPIC       = "xwc"
if __name__ == "__main__":
    with Logger() as logger, ExternalXboxGamePad( addr=ADDR, data_format=DATAFORMAT, topic=TOPIC, logger=logger) as controller_comm:
        try:
            while True: 
                sleep(60) # TODO: Check that this is resource efficient
                logger.write("Xbox Controller is still Running ... ", process_name="ExCont")
        except KeyboardInterrupt as e:
            logger.write("Xbox Controller is now terminating ... ", process_name="ExCont")
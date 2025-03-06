import json
from theodwyn_externals.controllers.gamepad     import ExternalXboxGamePad
from rohan.common.logging                       import Logger


if __name__ == "__main__":
    
    with open("./config/debug_imcoll.json") as file:
        json_data = json.load(file)
    network_configs = json_data["network"]
    camera_configs  = json_data["camera"]
    gstream_config  = camera_configs["gstream_config"]

    gstream_pipeline = (
        'udpsrc multicast-group={} port={} auto-multicast=true '
        'caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264" ! '
        'rtph264depay ! '
        'avdec_h264 ! '
        'videoconvert ! '
        'appsink drop=1'
    ).format( gstream_config["sink_ip"], gstream_config["sink_port"] )

    try:
        with Logger() as logger:
            with ExternalXboxGamePad( 
                    addr=network_configs[0]["addr"], 
                    data_format=network_configs[0]["data_format"], 
                    topic=network_configs[0]["topic"],
                    gstream_pipeline=gstream_pipeline,
                    logger=logger
            ) as controller_comm:
                while True: pass
    except KeyboardInterrupt as e:
        print("Exiting ... ")

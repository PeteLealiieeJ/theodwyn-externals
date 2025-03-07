ADDR=224.0.0.1
PORT=4444

gst-launch-1.0 udpsrc multicast-group=$ADDR port=$PORT caps="application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264" ! rtph264depay ! avdec_h264 ! videoconvert ! videoscale ! video/x-raw, width=640, height=512 ! ximagesink

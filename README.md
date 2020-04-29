# Indoor-Self-Driving-Vehicle
This repository is the implementation of the paper "Indoor navigation of unmanned grounded vehicle using CNN", International Journal of Recent Technology and Engineering (IJRTE)
ISSN: 2277-3878, Volume-8 Issue-6, March 2020.

Contains both Hardware tested on toy car and simulations. Generate training data- records training images & respective steering angles. Using convolutional neural network(CNN)model can autonomously drive the car.


# About the files
test/<br />
              Real_Vehicle.py: Big RC car control with keyboard<br />
    rc_control_test.py: RC car control with keyboard<br />
    stream_server_test.py: video streaming from Pi to computer<br />
    ultrasonic_server_test.py: sensor data streaming from Pi to computer neural network model in OpenCV3<br />

raspberryPi/<br />
    stream_client.py: stream video frames in jpeg format to the host computer<br />
    ultrasonic_client.py: send distance data measured by sensor to the host computer<br />

arduino/<br />
    rc_keyboard_control.ino: control RC car controller<br />

computer/<br />
    picam_calibration.py: pi camera calibration<br />
    collect_training_data.py: collect images in grayscale, data saved as *.npz<br />
    model.py: neural network model<br />
    model_training.py: model training and validation<br />
    rc_driver_helper.py: helper classes/functions for rc_driver.py<br />
    rc_driver.py: receive data from raspberry pi and drive the RC car based on model prediction<br />
    rc_driver_nn_only.py: simplified rc_driver.py without object detection<br />


![Screenshot 2020-04-30 at 1 37 01 AM](https://user-images.githubusercontent.com/40122399/80641812-1079fb80-8a83-11ea-9e38-f00abf96357b.png)
<br />
About 3000 Images of our college corridor were taken

# Video
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YQQlbH-sbFo/0.jpg)](https://www.youtube.com/watch?v=YQQlbH-sbFo)
<br/>
I have used the black pages as boundary

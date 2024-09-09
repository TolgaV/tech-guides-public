# List of Issues/Errors and Solutions

## Camera Module 3

### PDAF data in unsupported format

**Related Issues**

1. https://github.com/raspberrypi/picamera2/issues/1004
2. https://github.com/raspberrypi/libcamera/issues/61

**Diagnosis**

During capture operation, the `libcamera` application would throw errors:

```bash
[1:08:01.510172440] [2904] ERROR IPARPI cam_helper_imx708.cpp:273 PDAF data in unsupported format
[1:08:01.609986840] [2904] ERROR IPARPI cam_helper_imx708.cpp:273 PDAF data in unsupported format
```

The object producing the error can be seen at: https://git.libcamera.org/libcamera/libcamera.git/tree/src/ipa/rpi/cam_helper/cam_helper_imx708.cpp


Additionally, you can inspect related messages using `dmesg -wL`, which may display the following error:

```bash
[ 4022.981022] bcm2835-codec bcm2835-codec: Failed setting ctrl 00990a67, ret -3
```


**Effect**

When the **ERROR** is thrown by the `libcamera`, one can visually observe purple discolorations in rows of the recorded footage, and the application might occasionally crash.

**Cause**

The issue is likely due to electromagnetic interference (EMI) from the PMU (Power Management Unit) on the board. \
This can be verified by bringing the camera's ribbon cable close to the PMU while the `libcamera` application is running.

**Solution**

1. Secure the ribbon cable in an appropriate position.
2. Use a shielded alternative cable or apply copper/aluminum tape to shield the existing cable.

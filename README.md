# Bean Cloud Compiler Libraries

This repo describes the Bean Cloud Compiler library ecosystem, and allows for community-provided libraries. Anyone using a mobile Bean Loader application (Android or iOS) is a user of the Bean Cloud Compiler.

**The cloud compiler currently supports libraries coming from three different sources:**

1. Libraries distributed directly with the [Bean Arduino Core](https://github.com/PunchThrough/bean-arduino-core). These libraries usually need to be modified to explicitly work with the Bean.

    ```c
    #include <EEPROM.h>
    #include <PinChangeInt.h>
    #include <SoftwareSerial.h>
    #include <SPI.h>
    #include <Wire.h>
    ```

2. Libraries provided by [PlatformIO Library Manager](http://docs.platformio.org/en/stable/librarymanager/).

    We use two search terms to filter PlatformIO libraries. Additionally, we have hand picked out certain libraries that cause compilation conflicts or errors.

    Search Terms:

    * `platform=atmelavr`
    * `framework=arduino`

    Libraries:

    * [List of 867 PlatformIO Libraries supported by the Bean Cloud Compiler](https://github.com/PunchThrough/bean-cloud-compiler-libraries/blob/master/platformio-libraries.md)


3. Finally, libraries [in this repo](libraries/). These are "community" provided libraries that are not on PlatformIO and are not provide by the `bean-arduino-core`  

    ```c
    #include <Adafruit_MCP9808.h>
    #include <Adafruit_NeoPixel.h>
    #include <CapacitiveSensor.h>
    #include <NewPing.h>
    #include <SFE_MicroOLED.h>
    #include <SoftPWM.h>
    #include <SparkFunISL29125.h>
    #include <Grove_LED_Bar.h>
    #include <Servo.h>
    ```

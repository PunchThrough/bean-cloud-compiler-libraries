# Bean Cloud Compiler Libraries

This repo contains a collection of libraries that are available to the Bean Cloud Compiler users. Anyone using a mobile Bean Loader application (Android or iOS) is a user of the Bean Cloud Compiler.

The following libraries are available:

```c
#include <Adafruit_MCP9808.h>
#include <Adafruit_NeoPixel.h>
#include <CapacitiveSensor.h>
#include <NewPing.h>
#include <SFE_MicroOLED.h>
#include <SoftPWM.h>
#include <SparkFunISL29125.h>
#include <Grove_LED_Bar.h>
```

In addition to the libraries in this repo, some libraries are distributed directly with the [Bean Arduino Core](https://github.com/PunchThrough/bean-arduino-core). These libraries usually need to be modified to explicitly work with the Bean. The following libraries are included directly in the Bean Arduino Core:

```c
#include <EEPROM.h>
#include <PinChangeInt.h>
#include <SoftwareSerial.h>
#include <SPI.h>
#include <Wire.h>
```

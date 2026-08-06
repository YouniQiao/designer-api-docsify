# @system.sensor

The **Sensor** module provides APIs for querying the sensor list, subscribing to or unsubscribing from sensor data,
 and executing control commands.
 The sensors are classified into the following categories based on their functions: motion, environment, orientation,
 light, body, and other categories (such as Hall effect sensors). Each category includes different sensor types. A
 sensor type may be a single hardware sensor or a composite of multiple hardware sensors.
 > **NOTE**
 >
 > - Module maintenance policy:
 > >     - For lite wearables, this module is constantly maintained and available.
 > >     - For other device types, this module is no longer maintained since API version 8, and You are advised to use
 > the new [@ohos.sensor](arkts-sensor.md) module.
 > - The initial APIs of this module are supported since API version 3.
 > Newly added APIs will be marked with a superscript to indicate their earliest API version.
 > - This module requires hardware support and can only be debugged on real devices.


## Summary

### Classes

| Name | Description |
| --- | --- |
| [Sensor](arkts-sensorservice-sensor-sensor-c.md) |  |

### Interfaces

| Name | Description |
| --- | --- |
| [AccelerometerResponse](arkts-sensorservice-sensor-accelerometerresponse-i.md) | Defines the callback invoked when the acceleration sensor data changes. |
| [BarometerResponse](arkts-sensorservice-sensor-barometerresponse-i.md) | Defines a **BarometerResponse** object. |
| [CompassResponse](arkts-sensorservice-sensor-compassresponse-i.md) | Defines a **CompassResponse** object. |
| [DeviceOrientationResponse](arkts-sensorservice-sensor-deviceorientationresponse-i.md) | Defines a **DeviceOrientationResponse** object. |
| [GetOnBodyStateOptions](arkts-sensorservice-sensor-getonbodystateoptions-i.md) | Defines the callback invoked upon change in the wearing state of the device that houses the sensor. |
| [GyroscopeResponse](arkts-sensorservice-sensor-gyroscoperesponse-i.md) | Defines a **GyroscopeResponse** object. |
| [HeartRateResponse](arkts-sensorservice-sensor-heartrateresponse-i.md) | Defines a **HeartRateResponse** object. |
| [LightResponse](arkts-sensorservice-sensor-lightresponse-i.md) | Defines a **LightResponse** object. |
| [OnBodyStateResponse](arkts-sensorservice-sensor-onbodystateresponse-i.md) | Specifies whether the device that houses the sensor is worn. |
| [ProximityResponse](arkts-sensorservice-sensor-proximityresponse-i.md) | Callback invoked when the proximity sensor data changes. |
| [StepCounterResponse](arkts-sensorservice-sensor-stepcounterresponse-i.md) | Callback invoked when the step counter sensor data changes. |
| [SubscribeBarometerOptions](arkts-sensorservice-sensor-subscribebarometeroptions-i.md) | Defines the type of data to return for a subscription to data changes of the barometer sensor. |
| [SubscribeCompassOptions](arkts-sensorservice-sensor-subscribecompassoptions-i.md) | Defines the type of data to return for a subscription to data changes of the compass sensor. |
| [SubscribeDeviceOrientationOptions](arkts-sensorservice-sensor-subscribedeviceorientationoptions-i.md) | Defines the type of data to return for a subscription to data changes of the device orientation sensor. |
| [SubscribeGyroscopeOptions](arkts-sensorservice-sensor-subscribegyroscopeoptions-i.md) | Defines the type of data to return for a subscription to data changes of the gyroscope sensor. |
| [SubscribeHeartRateOptions](arkts-sensorservice-sensor-subscribeheartrateoptions-i.md) | Defines the type of data to return for a subscription to data changes of the heart rate sensor. |
| [SubscribeLightOptions](arkts-sensorservice-sensor-subscribelightoptions-i.md) | Defines the type of data to return for a subscription to data changes of the ambient light sensor. |
| [SubscribeOnBodyStateOptions](arkts-sensorservice-sensor-subscribeonbodystateoptions-i.md) | Defines the callback invoked upon change in the wearing state of the device that houses the sensor. |
| [SubscribeProximityOptions](arkts-sensorservice-sensor-subscribeproximityoptions-i.md) | Defines the type of data to return for a subscription to data changes of the proximity sensor. |
| [SubscribeStepCounterOptions](arkts-sensorservice-sensor-subscribestepcounteroptions-i.md) | Defines the type of data to return for a subscription to data changes of the step counter sensor. |
| [subscribeAccelerometerOptions](arkts-sensorservice-sensor-subscribeaccelerometeroptions-i.md) | Defines the type of data to return for a subscription to data changes of the acceleration sensor. |


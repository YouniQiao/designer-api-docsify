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


## Modules to Import

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from 'kits/@kit.SensorServiceKit';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Sensor](arkts-sensorservice-system-sensor-sensor-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AccelerometerResponse](arkts-sensorservice-system-sensor-accelerometerresponse-i.md) |
| [BarometerResponse](arkts-sensorservice-system-sensor-barometerresponse-i.md) |
| [CompassResponse](arkts-sensorservice-system-sensor-compassresponse-i.md) |
| [DeviceOrientationResponse](arkts-sensorservice-system-sensor-deviceorientationresponse-i.md) |
| [GetOnBodyStateOptions](arkts-sensorservice-system-sensor-getonbodystateoptions-i.md) |
| [GyroscopeResponse](arkts-sensorservice-system-sensor-gyroscoperesponse-i.md) |
| [HeartRateResponse](arkts-sensorservice-system-sensor-heartrateresponse-i.md) |
| [LightResponse](arkts-sensorservice-system-sensor-lightresponse-i.md) |
| [OnBodyStateResponse](arkts-sensorservice-system-sensor-onbodystateresponse-i.md) |
| [ProximityResponse](arkts-sensorservice-system-sensor-proximityresponse-i.md) |
| [StepCounterResponse](arkts-sensorservice-system-sensor-stepcounterresponse-i.md) |
| [SubscribeBarometerOptions](arkts-sensorservice-system-sensor-subscribebarometeroptions-i.md) |
| [SubscribeCompassOptions](arkts-sensorservice-system-sensor-subscribecompassoptions-i.md) |
| [SubscribeDeviceOrientationOptions](arkts-sensorservice-system-sensor-subscribedeviceorientationoptions-i.md) |
| [SubscribeGyroscopeOptions](arkts-sensorservice-system-sensor-subscribegyroscopeoptions-i.md) |
| [SubscribeHeartRateOptions](arkts-sensorservice-system-sensor-subscribeheartrateoptions-i.md) |
| [SubscribeLightOptions](arkts-sensorservice-system-sensor-subscribelightoptions-i.md) |
| [SubscribeOnBodyStateOptions](arkts-sensorservice-system-sensor-subscribeonbodystateoptions-i.md) |
| [SubscribeProximityOptions](arkts-sensorservice-system-sensor-subscribeproximityoptions-i.md) |
| [SubscribeStepCounterOptions](arkts-sensorservice-system-sensor-subscribestepcounteroptions-i.md) |
| [subscribeAccelerometerOptions](arkts-sensorservice-system-sensor-subscribeaccelerometeroptions-i.md) |

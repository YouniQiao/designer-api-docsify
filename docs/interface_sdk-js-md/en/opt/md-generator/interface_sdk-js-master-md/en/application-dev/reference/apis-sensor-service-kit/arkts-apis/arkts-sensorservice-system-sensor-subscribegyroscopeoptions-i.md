# SubscribeGyroscopeOptions

Defines the type of data to return for a subscription to data changes of the gyroscope sensor.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor.SensorId#GYROSCOPE

**Required permissions:** ohos.permission.GYROSCOPE

<!--Device-unnamed-export interface SubscribeGyroscopeOptions--><!--Device-unnamed-export interface SubscribeGyroscopeOptions-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from 'kits/@kit.SensorServiceKit';
```

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

Callback invoked when an API call fails.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#on

**Required permissions:** ohos.permission.GYROSCOPE

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeGyroscopeOptions-fail?: (data: string, code: number) => void--><!--Device-SubscribeGyroscopeOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string | Yes |
| code | number | Yes |

## success

```TypeScript
success: (data: GyroscopeResponse) => void
```

Callback invoked when the gyroscope sensor data changes.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#on

**Required permissions:** ohos.permission.GYROSCOPE

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeGyroscopeOptions-success: (data: GyroscopeResponse) => void--><!--Device-SubscribeGyroscopeOptions-success: (data: GyroscopeResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [GyroscopeResponse](arkts-sensorservice-sensor-gyroscoperesponse-i.md) | Yes |

## interval

```TypeScript
interval: string
```

Interval at which the callback is invoked to return the gyroscope sensor data.

The default value is **normal**. The options are as follows:

- **game**: called at an interval of 20 ms, which is applicable to gaming scenarios.  
- **ui**: called at an interval of 60 ms, which is applicable to UI updating scenarios.  
- **normal**: called at an interval of 200 ms, which is applicable to power-saving scenarios.

**Type:** string

**Since:** 6

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#Options.interval

**Required permissions:** ohos.permission.GYROSCOPE

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeGyroscopeOptions-interval: string--><!--Device-SubscribeGyroscopeOptions-interval: string-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

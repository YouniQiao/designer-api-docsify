# SubscribeCompassOptions

Defines the type of data to return for a subscription to data changes of the compass sensor.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor.SensorId#ORIENTATION

<!--Device-unnamed-export interface SubscribeCompassOptions--><!--Device-unnamed-export interface SubscribeCompassOptions-End-->

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

**Since:** 3

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#on

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeCompassOptions-fail?: (data: string, code: number) => void--><!--Device-SubscribeCompassOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string | Yes |
| code | number | Yes |

## success

```TypeScript
success: (data: CompassResponse) => void
```

Callback invoked when the compass sensor data changes.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#on

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeCompassOptions-success: (data: CompassResponse) => void--><!--Device-SubscribeCompassOptions-success: (data: CompassResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [CompassResponse](arkts-sensorservice-system-sensor-compassresponse-i.md) | Yes |

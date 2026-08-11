# GetOnBodyStateOptions

Defines the callback invoked upon change in the wearing state of the device that houses the sensor.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor.SensorId#WEAR_DETECTION

<!--Device-unnamed-export interface GetOnBodyStateOptions--><!--Device-unnamed-export interface GetOnBodyStateOptions-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from 'kits/@kit.SensorServiceKit';
```

## complete

```TypeScript
complete?: () => void
```

Callback invoked when the API call is complete.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#once

**Model restriction:** This API can be used only in the FA model.

<!--Device-GetOnBodyStateOptions-complete?: () => void--><!--Device-GetOnBodyStateOptions-complete?: () => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

Callback invoked when an API call fails.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#once

**Model restriction:** This API can be used only in the FA model.

<!--Device-GetOnBodyStateOptions-fail?: (data: string, code: number) => void--><!--Device-GetOnBodyStateOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string | Yes |
| code | number | Yes |

## success

```TypeScript
success: (data: OnBodyStateResponse) => void
```

Callback upon a successful API call.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#once

**Model restriction:** This API can be used only in the FA model.

<!--Device-GetOnBodyStateOptions-success: (data: OnBodyStateResponse) => void--><!--Device-GetOnBodyStateOptions-success: (data: OnBodyStateResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [OnBodyStateResponse](arkts-sensorservice-system-sensor-onbodystateresponse-i.md) | Yes |

# SubscribeStepCounterOptions

Defines the type of data to return for a subscription to data changes of the step counter sensor.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** [PEDOMETER](arkts-sensorservice-sensor-sensorid-e.md#PEDOMETER)

**Required permissions:** ohos.permission.ACTIVITY_MOTION

<!--Device-unnamed-export interface SubscribeStepCounterOptions--><!--Device-unnamed-export interface SubscribeStepCounterOptions-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from '@kit.SensorServiceKit';
```

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

Callback invoked when an API call fails.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** [on](ohos.sensor/sensor#on)

**Required permissions:** ohos.permission.ACTIVITY_MOTION

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeStepCounterOptions-fail?: (data: string, code: number) => void--><!--Device-SubscribeStepCounterOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success: (data: StepCounterResponse) => void
```

Defines a **StepCounterResponse** object.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** [on](ohos.sensor/sensor#on)

**Required permissions:** ohos.permission.ACTIVITY_MOTION

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeStepCounterOptions-success: (data: StepCounterResponse) => void--><!--Device-SubscribeStepCounterOptions-success: (data: StepCounterResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [StepCounterResponse](arkts-sensorservice-system-sensor-stepcounterresponse-i.md) | Yes |  |


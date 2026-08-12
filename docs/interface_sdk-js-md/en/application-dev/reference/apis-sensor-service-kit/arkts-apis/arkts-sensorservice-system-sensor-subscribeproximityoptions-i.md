# SubscribeProximityOptions

Defines the type of data to return for a subscription to data changes of the proximity sensor.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** [PROXIMITY](arkts-sensorservice-sensor-sensorid-e.md#PROXIMITY)

<!--Device-unnamed-export interface SubscribeProximityOptions--><!--Device-unnamed-export interface SubscribeProximityOptions-End-->

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

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeProximityOptions-fail?: (data: string, code: number) => void--><!--Device-SubscribeProximityOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success: (data: ProximityResponse) => void
```

Defines a **ProximityResponse** object.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** [on](ohos.sensor/sensor#on)

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeProximityOptions-success: (data: ProximityResponse) => void--><!--Device-SubscribeProximityOptions-success: (data: ProximityResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [ProximityResponse](arkts-sensorservice-system-sensor-proximityresponse-i.md) | Yes |  |


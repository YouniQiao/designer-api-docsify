# SubscribeBarometerOptions

Defines the type of data to return for a subscription to data changes of the barometer sensor.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [BAROMETER](arkts-sensorservice-sensor-sensorid-e.md#barometer)

<!--Device-unnamed-export interface SubscribeBarometerOptions--><!--Device-unnamed-export interface SubscribeBarometerOptions-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { Sensor, AccelerometerResponse, BarometerResponse, CompassResponse, DeviceOrientationResponse, GetOnBodyStateOptions, GyroscopeResponse, HeartRateResponse, LightResponse, OnBodyStateResponse, ProximityResponse, StepCounterResponse, SubscribeBarometerOptions, SubscribeCompassOptions, SubscribeDeviceOrientationOptions, SubscribeGyroscopeOptions, SubscribeHeartRateOptions, SubscribeLightOptions, SubscribeOnBodyStateOptions, SubscribeProximityOptions, SubscribeStepCounterOptions, subscribeAccelerometerOptions } from '@kit.SensorServiceKit';
```

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

Callback invoked when an API call fails.

**Type:** (data: string, code: number) =&gt; void

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [on](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#on_sensoridcolor)

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeBarometerOptions-fail?: (data: string, code: number) => void--><!--Device-SubscribeBarometerOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## success

```TypeScript
success: (data: BarometerResponse) => void
```

Callback invoked when the barometer sensor data changes.

**Type:** (data: BarometerResponse) =&gt; void

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [on](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#on_sensoridcolor)

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeBarometerOptions-success: (data: BarometerResponse) => void--><!--Device-SubscribeBarometerOptions-success: (data: BarometerResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


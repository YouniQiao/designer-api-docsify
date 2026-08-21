# SubscribeDeviceOrientationOptions

Defines the type of data to return for a subscription to data changes of the device orientation sensor.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** [ORIENTATION](arkts-sensorservice-sensor-sensorid-e.md#orientation)

<!--Device-unnamed-export interface SubscribeDeviceOrientationOptions--><!--Device-unnamed-export interface SubscribeDeviceOrientationOptions-End-->

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

**Since:** 6

**Deprecated since:** 8

**Substitutes:** [on](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#on_sensoridcolor)

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeDeviceOrientationOptions-fail?: (data: string, code: number) => void--><!--Device-SubscribeDeviceOrientationOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## interval

```TypeScript
interval: string
```

Interval at which the callback is invoked to return the device orientation sensor data.

The default value is **normal**. The options are as follows:

- **game**: called at an interval of 20 ms, which is applicable to gaming scenarios. - **ui**: called at an interval of 60 ms, which is applicable to UI updating scenarios. - **normal**: called at an interval of 200 ms, which is applicable to power-saving scenarios.

**Type:** string

**Since:** 6

**Deprecated since:** 8

**Substitutes:** [interval](arkts-sensorservice-sensor-options-i.md#interval)

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeDeviceOrientationOptions-interval: string--><!--Device-SubscribeDeviceOrientationOptions-interval: string-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## success

```TypeScript
success: (data: DeviceOrientationResponse) => void
```

Callback invoked when the device orientation sensor data changes.

**Type:** (data: DeviceOrientationResponse) =&gt; void

**Since:** 6

**Deprecated since:** 8

**Substitutes:** [on](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#on_sensoridcolor)

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeDeviceOrientationOptions-success: (data: DeviceOrientationResponse) => void--><!--Device-SubscribeDeviceOrientationOptions-success: (data: DeviceOrientationResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


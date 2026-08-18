# subscribeAccelerometerOptions

Defines the type of data to return for a subscription to data changes of the acceleration sensor.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [ACCELEROMETER](arkts-sensorservice-sensor-sensorid-e.md#accelerometer)

**Required permissions:** ohos.permission.ACCELEROMETER

<!--Device-unnamed-export interface subscribeAccelerometerOptions--><!--Device-unnamed-export interface subscribeAccelerometerOptions-End-->

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

**Required permissions:** ohos.permission.ACCELEROMETER

**Model restriction:** This API can be used only in the FA model.

<!--Device-subscribeAccelerometerOptions-fail?: (data: string, code: number) => void--><!--Device-subscribeAccelerometerOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## interval

```TypeScript
interval: string
```

Execution frequency of the callback for returning the acceleration sensor data. The default value is **normal**. The options are as follows: - **game**: called at an interval of 20 ms, which is applicable to gaming scenarios. - **ui**: called at an interval of 60 ms, which is applicable to UI updating scenarios. - **normal**: called at an interval of 200 ms, which is applicable to power-saving scenarios.

**Type:** string

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [interval](arkts-sensorservice-sensor-options-i.md#interval)

**Required permissions:** ohos.permission.ACCELEROMETER

**Model restriction:** This API can be used only in the FA model.

<!--Device-subscribeAccelerometerOptions-interval: string--><!--Device-subscribeAccelerometerOptions-interval: string-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## success

```TypeScript
success: (data: AccelerometerResponse) => void
```

Callback invoked when the acceleration sensor data changes.

**Type:** (data: AccelerometerResponse) =&gt; void

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [on](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#on_sensoridcolor)

**Required permissions:** ohos.permission.ACCELEROMETER

**Model restriction:** This API can be used only in the FA model.

<!--Device-subscribeAccelerometerOptions-success: (data: AccelerometerResponse) => void--><!--Device-subscribeAccelerometerOptions-success: (data: AccelerometerResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


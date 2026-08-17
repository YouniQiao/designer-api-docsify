# SubscribeGyroscopeOptions

Defines the type of data to return for a subscription to data changes of the gyroscope sensor.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** [GYROSCOPE](arkts-sensorservice-sensor-sensorid-e.md#gyroscope)

**Required permissions:** ohos.permission.GYROSCOPE

<!--Device-unnamed-export interface SubscribeGyroscopeOptions--><!--Device-unnamed-export interface SubscribeGyroscopeOptions-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { AccelerometerResponse } from 'AccelerometerResponse';
import { BarometerResponse } from 'BarometerResponse';
import { CompassResponse } from 'CompassResponse';
import { DeviceOrientationResponse } from 'DeviceOrientationResponse';
import { GetOnBodyStateOptions } from 'GetOnBodyStateOptions';
import { GyroscopeResponse } from 'GyroscopeResponse';
import { HeartRateResponse } from 'HeartRateResponse';
import { LightResponse } from 'LightResponse';
import { OnBodyStateResponse } from 'OnBodyStateResponse';
import { ProximityResponse } from 'ProximityResponse';
import { StepCounterResponse } from 'StepCounterResponse';
import { SubscribeBarometerOptions } from 'SubscribeBarometerOptions';
import { SubscribeCompassOptions } from 'SubscribeCompassOptions';
import { SubscribeDeviceOrientationOptions } from 'SubscribeDeviceOrientationOptions';
import { SubscribeGyroscopeOptions } from 'SubscribeGyroscopeOptions';
import { SubscribeHeartRateOptions } from 'SubscribeHeartRateOptions';
import { SubscribeLightOptions } from 'SubscribeLightOptions';
import { SubscribeOnBodyStateOptions } from 'SubscribeOnBodyStateOptions';
import { SubscribeProximityOptions } from 'SubscribeProximityOptions';
import { SubscribeStepCounterOptions } from 'SubscribeStepCounterOptions';
import { subscribeAccelerometerOptions } from 'subscribeAccelerometerOptions';
```

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

Callback invoked when an API call fails.

**Type:** (data: string, code: number) =&gt; void

**Since:** 6

**Deprecated since:** 8

**Substitutes:** [on](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#onsensoridcolor)

**Required permissions:** ohos.permission.GYROSCOPE

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeGyroscopeOptions-fail?: (data: string, code: number) => void--><!--Device-SubscribeGyroscopeOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## interval

```TypeScript
interval: string
```

Interval at which the callback is invoked to return the gyroscope sensor data. The default value is **normal**. The options are as follows: - **game**: called at an interval of 20 ms, which is applicable to gaming scenarios. - **ui**: called at an interval of 60 ms, which is applicable to UI updating scenarios. - **normal**: called at an interval of 200 ms, which is applicable to power-saving scenarios.

**Type:** string

**Since:** 6

**Deprecated since:** 8

**Substitutes:** [interval](arkts-sensorservice-sensor-options-i.md#interval)

**Required permissions:** ohos.permission.GYROSCOPE

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeGyroscopeOptions-interval: string--><!--Device-SubscribeGyroscopeOptions-interval: string-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## success

```TypeScript
success: (data: GyroscopeResponse) => void
```

Callback invoked when the gyroscope sensor data changes.

**Type:** (data: GyroscopeResponse) =&gt; void

**Since:** 6

**Deprecated since:** 8

**Substitutes:** [on](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#onsensoridcolor)

**Required permissions:** ohos.permission.GYROSCOPE

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeGyroscopeOptions-success: (data: GyroscopeResponse) => void--><!--Device-SubscribeGyroscopeOptions-success: (data: GyroscopeResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


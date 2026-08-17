# SubscribeHeartRateOptions

Defines the type of data to return for a subscription to data changes of the heart rate sensor.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [HEART_RATE](arkts-sensorservice-sensor-sensorid-e.md#heartrate)

**Required permissions:** ohos.permission.READ_HEALTH_DATA

<!--Device-unnamed-export interface SubscribeHeartRateOptions--><!--Device-unnamed-export interface SubscribeHeartRateOptions-End-->

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

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [on](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#onsensoridcolor)

**Required permissions:** ohos.permission.READ_HEALTH_DATA

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeHeartRateOptions-fail?: (data: string, code: number) => void--><!--Device-SubscribeHeartRateOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## success

```TypeScript
success: (data: HeartRateResponse) => void
```

Callback invoked when the heart rate sensor data changes. This callback is invoked every five seconds.

**Type:** (data: HeartRateResponse) =&gt; void

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [on](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#onsensoridcolor)

**Required permissions:** ohos.permission.READ_HEALTH_DATA

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeHeartRateOptions-success: (data: HeartRateResponse) => void--><!--Device-SubscribeHeartRateOptions-success: (data: HeartRateResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


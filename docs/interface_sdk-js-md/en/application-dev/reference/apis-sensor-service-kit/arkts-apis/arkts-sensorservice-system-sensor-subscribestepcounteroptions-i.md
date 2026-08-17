# SubscribeStepCounterOptions

Defines the type of data to return for a subscription to data changes of the step counter sensor.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** PEDOMETER

**Required permissions:** ohos.permission.ACTIVITY_MOTION

<!--Device-unnamed-export interface SubscribeStepCounterOptions--><!--Device-unnamed-export interface SubscribeStepCounterOptions-End-->

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

**Required permissions:** ohos.permission.ACTIVITY_MOTION

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeStepCounterOptions-fail?: (data: string, code: number) => void--><!--Device-SubscribeStepCounterOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## success

```TypeScript
success: (data: StepCounterResponse) => void
```

Defines a **StepCounterResponse** object.

**Type:** (data: StepCounterResponse) =&gt; void

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [on](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#onsensoridcolor)

**Required permissions:** ohos.permission.ACTIVITY_MOTION

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeStepCounterOptions-success: (data: StepCounterResponse) => void--><!--Device-SubscribeStepCounterOptions-success: (data: StepCounterResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


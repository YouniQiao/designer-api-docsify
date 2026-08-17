# GetOnBodyStateOptions

Defines the callback invoked upon change in the wearing state of the device that houses the sensor.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [WEAR_DETECTION](arkts-sensorservice-sensor-sensorid-e.md#weardetection)

<!--Device-unnamed-export interface GetOnBodyStateOptions--><!--Device-unnamed-export interface GetOnBodyStateOptions-End-->

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

## complete

```TypeScript
complete?: () => void
```

Callback invoked when the API call is complete.

**Type:** () =&gt; void

**Since:** 3

**Deprecated since:** 8

**Substitutes:** once

**Model restriction:** This API can be used only in the FA model.

<!--Device-GetOnBodyStateOptions-complete?: () => void--><!--Device-GetOnBodyStateOptions-complete?: () => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

Callback invoked when an API call fails.

**Type:** (data: string, code: number) =&gt; void

**Since:** 3

**Deprecated since:** 8

**Substitutes:** once

**Model restriction:** This API can be used only in the FA model.

<!--Device-GetOnBodyStateOptions-fail?: (data: string, code: number) => void--><!--Device-GetOnBodyStateOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## success

```TypeScript
success: (data: OnBodyStateResponse) => void
```

Callback upon a successful API call.

**Type:** (data: OnBodyStateResponse) =&gt; void

**Since:** 3

**Deprecated since:** 8

**Substitutes:** once

**Model restriction:** This API can be used only in the FA model.

<!--Device-GetOnBodyStateOptions-success: (data: OnBodyStateResponse) => void--><!--Device-GetOnBodyStateOptions-success: (data: OnBodyStateResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


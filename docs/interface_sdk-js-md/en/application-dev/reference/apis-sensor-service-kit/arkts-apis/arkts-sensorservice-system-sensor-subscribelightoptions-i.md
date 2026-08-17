# SubscribeLightOptions

Defines the type of data to return for a subscription to data changes of the ambient light sensor.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [AMBIENT_LIGHT](arkts-sensorservice-sensor-sensorid-e.md#ambientlight)

<!--Device-unnamed-export interface SubscribeLightOptions--><!--Device-unnamed-export interface SubscribeLightOptions-End-->

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

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeLightOptions-fail?: (data: string, code: number) => void--><!--Device-SubscribeLightOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## success

```TypeScript
success: (data: LightResponse) => void
```

Callback invoked when the ambient light sensor data changes.

**Type:** (data: LightResponse) =&gt; void

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [on](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#onsensoridcolor)

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeLightOptions-success: (data: LightResponse) => void--><!--Device-SubscribeLightOptions-success: (data: LightResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


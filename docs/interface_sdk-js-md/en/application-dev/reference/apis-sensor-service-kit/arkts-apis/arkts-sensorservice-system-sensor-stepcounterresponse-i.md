# StepCounterResponse

Callback invoked when the step counter sensor data changes.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [PedometerResponse](arkts-sensorservice-sensor-pedometerresponse-i.md#pedometerresponse)

**Required permissions:** ohos.permission.ACTIVITY_MOTION

<!--Device-unnamed-export interface StepCounterResponse--><!--Device-unnamed-export interface StepCounterResponse-End-->

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

## steps

```TypeScript
steps: number
```

Number of counted steps after the sensor is restarted.

**Type:** number

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [steps](arkts-sensorservice-sensor-pedometerresponse-i.md#steps)

**Required permissions:** ohos.permission.ACTIVITY_MOTION

**Model restriction:** This API can be used only in the FA model.

<!--Device-StepCounterResponse-steps: number--><!--Device-StepCounterResponse-steps: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


# CompassResponse

Defines a **CompassResponse** object.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [OrientationResponse](arkts-sensorservice-sensor-orientationresponse-i.md#orientationresponse)

<!--Device-unnamed-export interface CompassResponse--><!--Device-unnamed-export interface CompassResponse-End-->

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

## direction

```TypeScript
direction: number
```

Direction of the device, in degrees.

**Type:** number

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [alpha](arkts-sensorservice-sensor-orientationresponse-i.md#alpha)

**Model restriction:** This API can be used only in the FA model.

<!--Device-CompassResponse-direction: number--><!--Device-CompassResponse-direction: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


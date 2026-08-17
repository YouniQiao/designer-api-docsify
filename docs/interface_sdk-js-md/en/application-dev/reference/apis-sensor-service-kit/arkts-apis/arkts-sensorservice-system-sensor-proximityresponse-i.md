# ProximityResponse

Callback invoked when the proximity sensor data changes.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [ProximityResponse](arkts-sensorservice-sensor-proximityresponse-i.md#proximityresponse)

<!--Device-unnamed-export interface ProximityResponse--><!--Device-unnamed-export interface ProximityResponse-End-->

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

## distance

```TypeScript
distance: number
```

Distance between a visible object and the device screen.

**Type:** number

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [distance](arkts-sensorservice-sensor-proximityresponse-i.md#distance)

**Model restriction:** This API can be used only in the FA model.

<!--Device-ProximityResponse-distance: number--><!--Device-ProximityResponse-distance: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


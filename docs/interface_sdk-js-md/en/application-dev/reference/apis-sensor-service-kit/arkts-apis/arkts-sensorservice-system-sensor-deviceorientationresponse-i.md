# DeviceOrientationResponse

Defines a **DeviceOrientationResponse** object.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [OrientationResponse](arkts-sensorservice-sensor-orientationresponse-i.md#OrientationResponse)

<!--Device-unnamed-export interface DeviceOrientationResponse--><!--Device-unnamed-export interface DeviceOrientationResponse-End-->

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

## alpha

```TypeScript
alpha: number
```

Rotation angle around the Z axis when the X/Y axis of the device coincides with the X/Y axis of the earth.

**Type:** number

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [alpha](arkts-sensorservice-sensor-orientationresponse-i.md#alpha)

**Model restriction:** This API can be used only in the FA model.

<!--Device-DeviceOrientationResponse-alpha: number--><!--Device-DeviceOrientationResponse-alpha: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## beta

```TypeScript
beta: number
```

Rotation angle around the X axis when the Y/Z axis of the device coincides with the Y/Z axis of the earth.

**Type:** number

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [beta](arkts-sensorservice-sensor-orientationresponse-i.md#beta)

**Model restriction:** This API can be used only in the FA model.

<!--Device-DeviceOrientationResponse-beta: number--><!--Device-DeviceOrientationResponse-beta: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## gamma

```TypeScript
gamma: number
```

Rotation angle around the Y axis when the X/Z axis of the device coincides with the X/Z axis of the earth.

**Type:** number

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [gamma](arkts-sensorservice-sensor-orientationresponse-i.md#gamma)

**Model restriction:** This API can be used only in the FA model.

<!--Device-DeviceOrientationResponse-gamma: number--><!--Device-DeviceOrientationResponse-gamma: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


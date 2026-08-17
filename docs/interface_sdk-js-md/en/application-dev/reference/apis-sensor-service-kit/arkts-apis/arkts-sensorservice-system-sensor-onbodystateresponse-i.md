# OnBodyStateResponse

Specifies whether the device that houses the sensor is worn.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [WearDetectionResponse](arkts-sensorservice-sensor-weardetectionresponse-i.md#weardetectionresponse)

<!--Device-unnamed-export interface OnBodyStateResponse--><!--Device-unnamed-export interface OnBodyStateResponse-End-->

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

## value

```TypeScript
value: boolean
```

Boolean value indicating whether the device is worn. The value **true** indicates that the device is worn, and the value **false** indicates the opposite.

**Type:** boolean

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [value](arkts-sensorservice-sensor-weardetectionresponse-i.md#value)

**Model restriction:** This API can be used only in the FA model.

<!--Device-OnBodyStateResponse-value: boolean--><!--Device-OnBodyStateResponse-value: boolean-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


# CompassResponse

Defines a **CompassResponse** object.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** OrientationResponse

<!--Device-unnamed-export interface CompassResponse--><!--Device-unnamed-export interface CompassResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from '@kit.SensorServiceKit';
```

## direction

```TypeScript
direction: number
```

Direction of the device, in degrees.

**Type:** number

**Since:** 3

**Deprecated since:** 8

**Substitutes:** OrientationResponse.alpha

**Model restriction:** This API can be used only in the FA model.

<!--Device-CompassResponse-direction: number--><!--Device-CompassResponse-direction: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


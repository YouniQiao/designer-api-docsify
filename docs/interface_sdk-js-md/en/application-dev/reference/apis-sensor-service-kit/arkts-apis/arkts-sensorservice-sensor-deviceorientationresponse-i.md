# DeviceOrientationResponse

Defines a **DeviceOrientationResponse** object.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** OrientationResponse

<!--Device-unnamed-export interface DeviceOrientationResponse--><!--Device-unnamed-export interface DeviceOrientationResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from '@kit.SensorServiceKit';
```

## alpha

```TypeScript
alpha: number
```

Rotation angle around the Z axis when the X/Y axis of the device coincides with the X/Y axis of the earth.

**Type:** number

**Since:** 6

**Deprecated since:** 8

**Substitutes:** OrientationResponse.alpha

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

**Deprecated since:** 8

**Substitutes:** OrientationResponse.beta

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

**Deprecated since:** 8

**Substitutes:** OrientationResponse.gamma

**Model restriction:** This API can be used only in the FA model.

<!--Device-DeviceOrientationResponse-gamma: number--><!--Device-DeviceOrientationResponse-gamma: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


# ProximityResponse

Callback invoked when the proximity sensor data changes.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** ProximityResponse

<!--Device-unnamed-export interface ProximityResponse--><!--Device-unnamed-export interface ProximityResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from '@kit.SensorServiceKit';
```

## distance

```TypeScript
distance: number
```

Distance between a visible object and the device screen.

**Type:** number

**Since:** 3

**Deprecated since:** 8

**Substitutes:** ProximityResponse.distance

**Model restriction:** This API can be used only in the FA model.

<!--Device-ProximityResponse-distance: number--><!--Device-ProximityResponse-distance: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


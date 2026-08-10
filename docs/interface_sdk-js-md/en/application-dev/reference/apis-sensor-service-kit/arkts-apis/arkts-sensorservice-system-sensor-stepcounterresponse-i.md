# StepCounterResponse

计步传感器数据改变后的回调函数的响应对象，包含计步传感器重启后累计记录的步数数据。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#PedometerResponse

**Required permissions:** ohos.permission.ACTIVITY_MOTION

<!--Device-unnamed-export interface StepCounterResponse--><!--Device-unnamed-export interface StepCounterResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from 'kits/@kit.SensorServiceKit';
```

## steps

```TypeScript
steps: number
```

计步传感器重启后累计记录的步数。取值范围：大于等于0的整数，取值为实际上报物理量。传感器重启后步数从0重新开始累计。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#PedometerResponse.steps

**Required permissions:** ohos.permission.ACTIVITY_MOTION

**Model restriction:** This API can be used only in the FA model.

<!--Device-StepCounterResponse-steps: number--><!--Device-StepCounterResponse-steps: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


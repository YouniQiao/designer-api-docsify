# HeartRateResponse

心率传感器数据改变后的回调函数的响应对象，包含心率值数据。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#HeartRateResponse

**Required permissions:** ohos.permission.READ_HEALTH_DATA

<!--Device-unnamed-export interface HeartRateResponse--><!--Device-unnamed-export interface HeartRateResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from 'kits/@kit.SensorServiceKit';
```

## heartRate

```TypeScript
heartRate: number
```

心率值。单位：次/分钟（bpm）。取值范围：取值为实际上报物理量，由硬件传感器决定。正常成人静息心率约为60-100 bpm。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#HeartRateResponse.heartRate

**Required permissions:** ohos.permission.READ_HEALTH_DATA

**Model restriction:** This API can be used only in the FA model.

<!--Device-HeartRateResponse-heartRate: number--><!--Device-HeartRateResponse-heartRate: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


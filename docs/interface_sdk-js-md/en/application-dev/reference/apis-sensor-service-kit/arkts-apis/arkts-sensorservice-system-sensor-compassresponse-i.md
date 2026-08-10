# CompassResponse

罗盘数据改变后的回调函数的响应对象，包含设备面对的方向度数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#OrientationResponse

<!--Device-unnamed-export interface CompassResponse--><!--Device-unnamed-export interface CompassResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from 'kits/@kit.SensorServiceKit';
```

## direction

```TypeScript
direction: number
```

设备面对的方向度数。单位：度（°）。取值范围：[0, 360)，0表示朝北。取值为实际上报物理量。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#OrientationResponse.alpha

**Model restriction:** This API can be used only in the FA model.

<!--Device-CompassResponse-direction: number--><!--Device-CompassResponse-direction: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


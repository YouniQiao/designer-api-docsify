# LightResponse

光线感应数据改变后的回调函数的响应对象，包含环境光线强度数据。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#LightResponse

<!--Device-unnamed-export interface LightResponse--><!--Device-unnamed-export interface LightResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from 'kits/@kit.SensorServiceKit';
```

## intensity

```TypeScript
intensity: number
```

环境光线强度。单位：lux。取值范围：取值为实际上报物理量，由硬件传感器决定。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#LightResponse.intensity

**Model restriction:** This API can be used only in the FA model.

<!--Device-LightResponse-intensity: number--><!--Device-LightResponse-intensity: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


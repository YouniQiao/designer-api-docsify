# BarometerResponse

气压计传感器数据改变后的回调函数的响应对象，包含气压值数据。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#BarometerResponse

<!--Device-unnamed-export interface BarometerResponse--><!--Device-unnamed-export interface BarometerResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from 'kits/@kit.SensorServiceKit';
```

## pressure

```TypeScript
pressure: number
```

气压值。单位：帕斯卡（Pa）。取值范围：取值为实际上报物理量，由硬件传感器决定。标准大气压约为101325 Pa。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#BarometerResponse.pressure

**Model restriction:** This API can be used only in the FA model.

<!--Device-BarometerResponse-pressure: number--><!--Device-BarometerResponse-pressure: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


# GyroscopeResponse

陀螺仪传感器数据变化后的回调函数的响应对象，包含设备在x、y、z三轴方向的旋转角速度数据。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#GyroscopeResponse

**Required permissions:** ohos.permission.GYROSCOPE

<!--Device-unnamed-export interface GyroscopeResponse--><!--Device-unnamed-export interface GyroscopeResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from 'kits/@kit.SensorServiceKit';
```

## x

```TypeScript
x: number
```

x轴的旋转角速度。单位：rad/s。取值范围：取值为实际上报物理量，由硬件传感器决定。

**Type:** number

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#GyroscopeResponse.x

**Required permissions:** ohos.permission.GYROSCOPE

**Model restriction:** This API can be used only in the FA model.

<!--Device-GyroscopeResponse-x: number--><!--Device-GyroscopeResponse-x: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## y

```TypeScript
y: number
```

y轴的旋转角速度。单位：rad/s。取值范围：取值为实际上报物理量，由硬件传感器决定。

**Type:** number

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#GyroscopeResponse.y

**Required permissions:** ohos.permission.GYROSCOPE

**Model restriction:** This API can be used only in the FA model.

<!--Device-GyroscopeResponse-y: number--><!--Device-GyroscopeResponse-y: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## z

```TypeScript
z: number
```

z轴的旋转角速度。单位：rad/s。取值范围：取值为实际上报物理量，由硬件传感器决定。

**Type:** number

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#GyroscopeResponse.z

**Required permissions:** ohos.permission.GYROSCOPE

**Model restriction:** This API can be used only in the FA model.

<!--Device-GyroscopeResponse-z: number--><!--Device-GyroscopeResponse-z: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


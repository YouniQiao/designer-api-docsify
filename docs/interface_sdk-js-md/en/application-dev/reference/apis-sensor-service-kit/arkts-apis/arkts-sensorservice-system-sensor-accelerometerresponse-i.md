# AccelerometerResponse

感应到加速度数据变化后的回调函数的响应对象，包含设备在x、y、z三轴方向上的加速度数据。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#AccelerometerResponse

**Required permissions:** ohos.permission.ACCELEROMETER

<!--Device-unnamed-export interface AccelerometerResponse--><!--Device-unnamed-export interface AccelerometerResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from 'kits/@kit.SensorServiceKit';
```

## x

```TypeScript
x: number
```

施加在设备x轴的加速度。单位：m/s²。取值范围：取值为实际上报物理量，由硬件传感器决定。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#AccelerometerResponse.x

**Required permissions:** ohos.permission.ACCELEROMETER

**Model restriction:** This API can be used only in the FA model.

<!--Device-AccelerometerResponse-x: number--><!--Device-AccelerometerResponse-x: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## y

```TypeScript
y: number
```

施加在设备y轴的加速度。单位：m/s²。取值范围：取值为实际上报物理量，由硬件传感器决定。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#AccelerometerResponse.y

**Required permissions:** ohos.permission.ACCELEROMETER

**Model restriction:** This API can be used only in the FA model.

<!--Device-AccelerometerResponse-y: number--><!--Device-AccelerometerResponse-y: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## z

```TypeScript
z: number
```

施加在设备z轴的加速度。单位：m/s²。取值范围：取值为实际上报物理量，由硬件传感器决定。静止状态下z轴加速度约为9.8 m/s²（重力加速度）。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#AccelerometerResponse.z

**Required permissions:** ohos.permission.ACCELEROMETER

**Model restriction:** This API can be used only in the FA model.

<!--Device-AccelerometerResponse-z: number--><!--Device-AccelerometerResponse-z: number-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


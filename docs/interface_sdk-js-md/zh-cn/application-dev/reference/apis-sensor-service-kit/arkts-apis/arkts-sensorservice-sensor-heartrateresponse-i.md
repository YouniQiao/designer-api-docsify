# HeartRateResponse

心率传感器数据改变后的回调函数的响应对象，包含心率值数据。

**起始版本：** 3

**废弃版本：** 8

**替代接口：** HeartRateResponse

**需要权限：** ohos.permission.READ_HEALTH_DATA

<!--Device-unnamed-export interface HeartRateResponse--><!--Device-unnamed-export interface HeartRateResponse-End-->

**系统能力：** SystemCapability.Sensors.Sensor.Lite

## 导入模块

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from '@kit.SensorServiceKit';
```

## heartRate

```TypeScript
heartRate: number
```

心率值。单位：次/分钟（bpm）。取值范围：取值为实际上报物理量，由硬件传感器决定。正常成人静息心率约为60-100 bpm。

**类型：** number

**起始版本：** 3

**废弃版本：** 8

**替代接口：** HeartRateResponse.heartRate

**需要权限：** ohos.permission.READ_HEALTH_DATA

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-HeartRateResponse-heartRate: number--><!--Device-HeartRateResponse-heartRate: number-End-->

**系统能力：** SystemCapability.Sensors.Sensor.Lite


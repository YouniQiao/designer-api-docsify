# LightResponse

光线感应数据改变后的回调函数的响应对象，包含环境光线强度数据。

**起始版本：** 3

**废弃版本：** 8

**替代接口：** LightResponse

<!--Device-unnamed-export interface LightResponse--><!--Device-unnamed-export interface LightResponse-End-->

**系统能力：** SystemCapability.Sensors.Sensor.Lite

## 导入模块

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from '@kit.SensorServiceKit';
```

## intensity

```TypeScript
intensity: number
```

环境光线强度。单位：lux。取值范围：取值为实际上报物理量，由硬件传感器决定。

**类型：** number

**起始版本：** 3

**废弃版本：** 8

**替代接口：** LightResponse.intensity

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-LightResponse-intensity: number--><!--Device-LightResponse-intensity: number-End-->

**系统能力：** SystemCapability.Sensors.Sensor.Lite


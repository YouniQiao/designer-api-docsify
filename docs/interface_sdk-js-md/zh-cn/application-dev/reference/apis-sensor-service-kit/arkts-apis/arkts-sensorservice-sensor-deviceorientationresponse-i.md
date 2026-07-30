# DeviceOrientationResponse

设备方向传感器数据变化后的回调函数的响应对象，包含设备方向的三个旋转角度数据。

**起始版本：** 6

**废弃版本：** 8

**替代接口：** OrientationResponse

<!--Device-unnamed-export interface DeviceOrientationResponse--><!--Device-unnamed-export interface DeviceOrientationResponse-End-->

**系统能力：** SystemCapability.Sensors.Sensor.Lite

## 导入模块

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from '@kit.SensorServiceKit';
```

## alpha

```TypeScript
alpha: number
```

当设备坐标X/Y和地球X/Y重合时，绕着Z轴转动的夹角。单位：度（°）。取值范围：[0, 360)。

**类型：** number

**起始版本：** 6

**废弃版本：** 8

**替代接口：** OrientationResponse.alpha

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DeviceOrientationResponse-alpha: number--><!--Device-DeviceOrientationResponse-alpha: number-End-->

**系统能力：** SystemCapability.Sensors.Sensor.Lite

## beta

```TypeScript
beta: number
```

当设备坐标Y/Z和地球Y/Z重合时，绕着X轴转动的夹角。单位：度（°）。取值范围：[-180, 180)。

**类型：** number

**起始版本：** 6

**废弃版本：** 8

**替代接口：** OrientationResponse.beta

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DeviceOrientationResponse-beta: number--><!--Device-DeviceOrientationResponse-beta: number-End-->

**系统能力：** SystemCapability.Sensors.Sensor.Lite

## gamma

```TypeScript
gamma: number
```

当设备X/Z和地球X/Z重合时，绕着Y轴转动的夹角。单位：度（°）。取值范围：[-90, 90)。

**类型：** number

**起始版本：** 6

**废弃版本：** 8

**替代接口：** OrientationResponse.gamma

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DeviceOrientationResponse-gamma: number--><!--Device-DeviceOrientationResponse-gamma: number-End-->

**系统能力：** SystemCapability.Sensors.Sensor.Lite


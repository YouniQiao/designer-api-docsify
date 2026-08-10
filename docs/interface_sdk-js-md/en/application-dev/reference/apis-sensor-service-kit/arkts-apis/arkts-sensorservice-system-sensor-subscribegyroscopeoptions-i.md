# SubscribeGyroscopeOptions

用于设置陀螺仪传感器订阅的参数，包括回调频率和回调函数。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor.SensorId#GYROSCOPE

**Required permissions:** ohos.permission.GYROSCOPE

<!--Device-unnamed-export interface SubscribeGyroscopeOptions--><!--Device-unnamed-export interface SubscribeGyroscopeOptions-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from 'kits/@kit.SensorServiceKit';
```

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

接口调用失败的回调函数。回调参数为(data: string, code: number)，其中data为错误信息，code为错误码。不填写时，接口调用失败无回调通知。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#on

**Required permissions:** ohos.permission.GYROSCOPE

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeGyroscopeOptions-fail?: (data: string, code: number) => void--><!--Device-SubscribeGyroscopeOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success: (data: GyroscopeResponse) => void
```

感应到陀螺仪数据变化后的回调函数，回调参数为GyroscopeResponse对象。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#on

**Required permissions:** ohos.permission.GYROSCOPE

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeGyroscopeOptions-success: (data: GyroscopeResponse) => void--><!--Device-SubscribeGyroscopeOptions-success: (data: GyroscopeResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [GyroscopeResponse](arkts-sensorservice-sensor-gyroscoperesponse-i.md) | Yes |  |

## interval

```TypeScript
interval: string
```

频率参数，陀螺仪的回调函数执行频率。

默认值：'normal'。

可选值：

-'game'：极高的回调频率，20ms/次，适用于游戏场景。

-'ui'：较高的回调频率，60ms/次，适用于UI更新场景。

-'normal'：普通的回调频率，200ms/次，适用于低功耗场景。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#Options.interval

**Required permissions:** ohos.permission.GYROSCOPE

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeGyroscopeOptions-interval: string--><!--Device-SubscribeGyroscopeOptions-interval: string-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


# subscribeAccelerometerOptions

用于设置加速度传感器订阅的参数，包括回调频率和回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor.SensorId#ACCELEROMETER

**Required permissions:** ohos.permission.ACCELEROMETER

<!--Device-unnamed-export interface subscribeAccelerometerOptions--><!--Device-unnamed-export interface subscribeAccelerometerOptions-End-->

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

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#on

**Required permissions:** ohos.permission.ACCELEROMETER

**Model restriction:** This API can be used only in the FA model.

<!--Device-subscribeAccelerometerOptions-fail?: (data: string, code: number) => void--><!--Device-subscribeAccelerometerOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success: (data: AccelerometerResponse) => void
```

当加速度传感器数据发生变化时的回调函数，回调参数为AccelerometerResponse对象。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#on

**Required permissions:** ohos.permission.ACCELEROMETER

**Model restriction:** This API can be used only in the FA model.

<!--Device-subscribeAccelerometerOptions-success: (data: AccelerometerResponse) => void--><!--Device-subscribeAccelerometerOptions-success: (data: AccelerometerResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [AccelerometerResponse](arkts-sensorservice-system-sensor-accelerometerresponse-i.md) | Yes |  |

## interval

```TypeScript
interval: string
```

频率参数，加速度的回调函数执行频率。

默认值：'normal'。

可选值：

-'game'：极高的回调频率，20ms/次，适用于游戏场景。

-'ui'：较高的回调频率，60ms/次，适用于UI更新场景。

-'normal'：普通的回调频率，200ms/次，适用于低功耗场景。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#Options.interval

**Required permissions:** ohos.permission.ACCELEROMETER

**Model restriction:** This API can be used only in the FA model.

<!--Device-subscribeAccelerometerOptions-interval: string--><!--Device-subscribeAccelerometerOptions-interval: string-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


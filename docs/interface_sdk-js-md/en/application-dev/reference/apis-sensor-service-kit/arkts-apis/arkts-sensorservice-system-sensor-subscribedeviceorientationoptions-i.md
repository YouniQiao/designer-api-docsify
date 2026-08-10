# SubscribeDeviceOrientationOptions

用于设置设备方向传感器订阅的参数，包括回调频率和回调函数。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor.SensorId#ORIENTATION

<!--Device-unnamed-export interface SubscribeDeviceOrientationOptions--><!--Device-unnamed-export interface SubscribeDeviceOrientationOptions-End-->

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

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeDeviceOrientationOptions-fail?: (data: string, code: number) => void--><!--Device-SubscribeDeviceOrientationOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success: (data: DeviceOrientationResponse) => void
```

感应到设备方向传感器数据变化后的回调函数，回调参数为DeviceOrientationResponse对象。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#on

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeDeviceOrientationOptions-success: (data: DeviceOrientationResponse) => void--><!--Device-SubscribeDeviceOrientationOptions-success: (data: DeviceOrientationResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [DeviceOrientationResponse](arkts-sensorservice-system-sensor-deviceorientationresponse-i.md) | Yes |  |

## interval

```TypeScript
interval: string
```

频率参数，设备方向传感器的回调函数执行频率。

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

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeDeviceOrientationOptions-interval: string--><!--Device-SubscribeDeviceOrientationOptions-interval: string-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite


# onceGravityChange

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## onceGravityChange

```TypeScript
function onceGravityChange(callback: Callback<GravityResponse>): void
```

Subscribe to gravity sensor data once, {@code SensorId.GRAVITY}.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-sensor-function onceGravityChange(callback: Callback<GravityResponse>): void--><!--Device-sensor-function onceGravityChange(callback: Callback<GravityResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;GravityResponse&gt; | 是 | callback gravity data. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 14500101 | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |


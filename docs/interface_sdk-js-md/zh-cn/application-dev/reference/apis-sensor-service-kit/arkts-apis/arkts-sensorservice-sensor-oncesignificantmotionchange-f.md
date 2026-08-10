# onceSignificantMotionChange

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## onceSignificantMotionChange

```TypeScript
function onceSignificantMotionChange(callback: Callback<SignificantMotionResponse>): void
```

Subscribe to significant motion sensor data once, {@code SensorId.SIGNIFICANT_MOTION}.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-sensor-function onceSignificantMotionChange(callback: Callback<SignificantMotionResponse>): void--><!--Device-sensor-function onceSignificantMotionChange(callback: Callback<SignificantMotionResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SignificantMotionResponse&gt; | 是 | callback significant motion data. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 14500101 | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |


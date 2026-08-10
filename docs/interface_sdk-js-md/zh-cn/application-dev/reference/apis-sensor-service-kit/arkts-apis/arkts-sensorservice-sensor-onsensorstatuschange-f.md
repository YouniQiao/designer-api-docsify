# onSensorStatusChange

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## onSensorStatusChange

```TypeScript
function onSensorStatusChange(callback: Callback<SensorStatusEvent>): void
```

Start listening on device status changes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-sensor-function onSensorStatusChange(callback: Callback<SensorStatusEvent>): void--><!--Device-sensor-function onSensorStatusChange(callback: Callback<SensorStatusEvent>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SensorStatusEvent&gt; | 是 | callback of sensor status. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 14500101 | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |


# onSensorStatusChange

## onSensorStatusChange

```TypeScript
function onSensorStatusChange(callback: Callback<SensorStatusEvent>): void
```

Start listening on device status changes.

**起始版本：** 23

**废弃版本：** -1

<!--Device-sensor-function onSensorStatusChange(callback: Callback<SensorStatusEvent>): void--><!--Device-sensor-function onSensorStatusChange(callback: Callback<SensorStatusEvent>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SensorStatusEvent](arkts-sensorservice-sensor-sensorstatusevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

# onceSignificantMotionChange

## onceSignificantMotionChange

```TypeScript
function onceSignificantMotionChange(callback: Callback<SignificantMotionResponse>): void
```

Subscribe to significant motion sensor data once, {@code SensorId.SIGNIFICANT_MOTION}.

**起始版本：** 23

**废弃版本：** -1

<!--Device-sensor-function onceSignificantMotionChange(callback: Callback<SignificantMotionResponse>): void--><!--Device-sensor-function onceSignificantMotionChange(callback: Callback<SignificantMotionResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SignificantMotionResponse](arkts-sensorservice-sensor-significantmotionresponse-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

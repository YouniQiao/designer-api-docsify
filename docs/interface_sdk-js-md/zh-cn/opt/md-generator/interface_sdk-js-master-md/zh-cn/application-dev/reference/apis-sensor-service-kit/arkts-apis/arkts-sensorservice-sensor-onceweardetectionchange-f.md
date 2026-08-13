# onceWearDetectionChange

## onceWearDetectionChange

```TypeScript
function onceWearDetectionChange(callback: Callback<WearDetectionResponse>): void
```

Subscribe to wear detection sensor data once, {@code SensorId.WEAR_DETECTION}.

**起始版本：** 23

**废弃版本：** -1

<!--Device-sensor-function onceWearDetectionChange(callback: Callback<WearDetectionResponse>): void--><!--Device-sensor-function onceWearDetectionChange(callback: Callback<WearDetectionResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WearDetectionResponse](arkts-sensorservice-sensor-weardetectionresponse-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

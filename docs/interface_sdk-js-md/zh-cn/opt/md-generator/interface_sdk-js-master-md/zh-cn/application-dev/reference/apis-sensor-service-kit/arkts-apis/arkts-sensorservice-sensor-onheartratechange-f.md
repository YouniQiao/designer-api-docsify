# onHeartRateChange

## onHeartRateChange

```TypeScript
function onHeartRateChange(callback: Callback<HeartRateResponse>, options?: Options): void
```

Subscribe to heart rate sensor data, {@code SensorId.HEART_RATE}.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.READ_HEALTH_DATA

<!--Device-sensor-function onHeartRateChange(callback: Callback<HeartRateResponse>, options?: Options): void--><!--Device-sensor-function onHeartRateChange(callback: Callback<HeartRateResponse>, options?: Options): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;HeartRateResponse&gt; | 是 |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

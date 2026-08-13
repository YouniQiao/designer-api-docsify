# onGravityChange

## onGravityChange

```TypeScript
function onGravityChange(callback: Callback<GravityResponse>, options?: Options): void
```

Subscribe to gravity sensor data, {@code SensorId.GRAVITY}.

**起始版本：** 23

**废弃版本：** -1

<!--Device-sensor-function onGravityChange(callback: Callback<GravityResponse>, options?: Options): void--><!--Device-sensor-function onGravityChange(callback: Callback<GravityResponse>, options?: Options): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[GravityResponse](arkts-sensorservice-sensor-gravityresponse-i.md)&gt; | 是 |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

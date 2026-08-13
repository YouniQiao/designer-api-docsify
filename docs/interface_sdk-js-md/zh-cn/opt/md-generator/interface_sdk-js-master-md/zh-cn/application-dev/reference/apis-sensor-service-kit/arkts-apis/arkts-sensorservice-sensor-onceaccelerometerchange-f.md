# onceAccelerometerChange

## onceAccelerometerChange

```TypeScript
function onceAccelerometerChange(callback: Callback<AccelerometerResponse>): void
```

Subscribe to accelerometer sensor data once, {@code SensorId.ACCELEROMETER}.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCELEROMETER

<!--Device-sensor-function onceAccelerometerChange(callback: Callback<AccelerometerResponse>): void--><!--Device-sensor-function onceAccelerometerChange(callback: Callback<AccelerometerResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AccelerometerResponse&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

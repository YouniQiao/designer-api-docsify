# oncePedometerChange

## oncePedometerChange

```TypeScript
function oncePedometerChange(callback: Callback<PedometerResponse>): void
```

Subscribe to pedometer sensor data once, {@code SensorId.PEDOMETER}.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACTIVITY_MOTION

<!--Device-sensor-function oncePedometerChange(callback: Callback<PedometerResponse>): void--><!--Device-sensor-function oncePedometerChange(callback: Callback<PedometerResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PedometerResponse](arkts-sensorservice-sensor-pedometerresponse-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

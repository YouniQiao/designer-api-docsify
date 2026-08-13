# onceMagneticFieldChange

## onceMagneticFieldChange

```TypeScript
function onceMagneticFieldChange(callback: Callback<MagneticFieldResponse>): void
```

Subscribe to magnetic field sensor data once, {@code SensorId.MAGNETIC_FIELD}.

**起始版本：** 23

**废弃版本：** -1

<!--Device-sensor-function onceMagneticFieldChange(callback: Callback<MagneticFieldResponse>): void--><!--Device-sensor-function onceMagneticFieldChange(callback: Callback<MagneticFieldResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MagneticFieldResponse](arkts-sensorservice-sensor-magneticfieldresponse-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

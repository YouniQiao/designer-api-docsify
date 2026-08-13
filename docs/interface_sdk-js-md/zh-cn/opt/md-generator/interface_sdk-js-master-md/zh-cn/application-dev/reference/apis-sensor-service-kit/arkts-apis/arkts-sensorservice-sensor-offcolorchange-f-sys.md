# offColorChange（系统接口）

## offColorChange

```TypeScript
function offColorChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<ColorResponse>): void
```

Unsubscribe to color sensor data, {@code SensorId.COLOR}.

**起始版本：** 23

**废弃版本：** -1

<!--Device-sensor-function offColorChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<ColorResponse>): void--><!--Device-sensor-function offColorChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<ColorResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [sensorInfoParam](arkts-sensorservice-sensor-options-i.md) | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | 否 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ColorResponse](arkts-sensorservice-sensor-colorresponse-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

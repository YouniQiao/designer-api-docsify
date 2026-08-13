# onAmbientTemperatureChange

## onAmbientTemperatureChange

```TypeScript
function onAmbientTemperatureChange(callback: Callback<AmbientTemperatureResponse>, options?: Options): void
```

Subscribe to ambient temperature sensor data, {@code SensorId.AMBIENT_TEMPERATURE}.

**起始版本：** 23

**废弃版本：** -1

<!--Device-sensor-function onAmbientTemperatureChange(callback: Callback<AmbientTemperatureResponse>, options?: Options): void--><!--Device-sensor-function onAmbientTemperatureChange(callback: Callback<AmbientTemperatureResponse>, options?: Options): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AmbientTemperatureResponse](arkts-sensorservice-sensor-ambienttemperatureresponse-i.md)&gt; | 是 |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

# onceHumidityChange

## 导入模块

```TypeScript
```

## onceHumidityChange

```TypeScript
function onceHumidityChange(callback: Callback<HumidityResponse>): void
```

Subscribe to humidity sensor data once, {@code SensorId.HUMIDITY}.

**起始版本：** 23

<!--Device-sensor-function onceHumidityChange(callback: Callback<HumidityResponse>): void--><!--Device-sensor-function onceHumidityChange(callback: Callback<HumidityResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HumidityResponse](arkts-sensorservice-sensor-humidityresponse-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

# onceBarometerChange

## 导入模块

```TypeScript
```

## onceBarometerChange

```TypeScript
function onceBarometerChange(callback: Callback<BarometerResponse>): void
```

Subscribe to barometer sensor data once, {@code SensorId.BAROMETER}.

**起始版本：** 23

<!--Device-sensor-function onceBarometerChange(callback: Callback<BarometerResponse>): void--><!--Device-sensor-function onceBarometerChange(callback: Callback<BarometerResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BarometerResponse&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

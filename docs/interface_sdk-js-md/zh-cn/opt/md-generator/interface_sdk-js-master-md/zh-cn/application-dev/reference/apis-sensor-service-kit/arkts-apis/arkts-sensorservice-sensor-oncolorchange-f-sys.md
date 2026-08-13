# onColorChange（系统接口）

## onColorChange

```TypeScript
function onColorChange(callback: Callback<ColorResponse>, options?: Options): void
```

Subscribe to color sensor data, {@code SensorId.COLOR}.

**起始版本：** 23

**废弃版本：** -1

<!--Device-sensor-function onColorChange(callback: Callback<ColorResponse>, options?: Options): void--><!--Device-sensor-function onColorChange(callback: Callback<ColorResponse>, options?: Options): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ColorResponse](arkts-sensorservice-sensor-colorresponse-i-sys.md)&gt; | 是 |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

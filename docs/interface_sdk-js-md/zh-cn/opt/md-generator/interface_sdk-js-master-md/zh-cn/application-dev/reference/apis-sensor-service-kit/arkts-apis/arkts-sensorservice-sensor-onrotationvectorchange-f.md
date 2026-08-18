# onRotationVectorChange

## 导入模块

```TypeScript
```

## onRotationVectorChange

```TypeScript
function onRotationVectorChange(callback: Callback<RotationVectorResponse>, options?: Options): void
```

Subscribe to rotation vector sensor data, {@code SensorId.ROTATION_VECTOR}.

**起始版本：** 23

<!--Device-sensor-function onRotationVectorChange(callback: Callback<RotationVectorResponse>, options?: Options): void--><!--Device-sensor-function onRotationVectorChange(callback: Callback<RotationVectorResponse>, options?: Options): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RotationVectorResponse](arkts-sensorservice-sensor-rotationvectorresponse-i.md)&gt; | 是 |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

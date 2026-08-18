# onceGyroscopeUncalibratedChange

## 导入模块

```TypeScript
```

## onceGyroscopeUncalibratedChange

```TypeScript
function onceGyroscopeUncalibratedChange(callback: Callback<GyroscopeUncalibratedResponse>): void
```

Subscribe to uncalibrated gyroscope sensor data once, {@code SensorId.GYROSCOPE_UNCALIBRATED}.

**起始版本：** 23

**需要权限：** ohos.permission.GYROSCOPE

<!--Device-sensor-function onceGyroscopeUncalibratedChange(callback: Callback<GyroscopeUncalibratedResponse>): void--><!--Device-sensor-function onceGyroscopeUncalibratedChange(callback: Callback<GyroscopeUncalibratedResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[GyroscopeUncalibratedResponse](arkts-sensorservice-sensor-gyroscopeuncalibratedresponse-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

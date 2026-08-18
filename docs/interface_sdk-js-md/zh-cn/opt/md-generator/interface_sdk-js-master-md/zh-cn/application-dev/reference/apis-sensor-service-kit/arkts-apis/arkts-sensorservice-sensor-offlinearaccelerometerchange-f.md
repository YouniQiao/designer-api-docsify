# offLinearAccelerometerChange

## 导入模块

```TypeScript
```

## offLinearAccelerometerChange

```TypeScript
function offLinearAccelerometerChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<LinearAccelerometerResponse>): void
```

Unsubscribe to linear acceleration sensor data, {@code SensorId.LINEAR_ACCELEROMETER}.

**起始版本：** 23

**需要权限：** ohos.permission.ACCELEROMETER

<!--Device-sensor-function offLinearAccelerometerChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<LinearAccelerometerResponse>): void--><!--Device-sensor-function offLinearAccelerometerChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<LinearAccelerometerResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [sensorInfoParam](arkts-sensorservice-sensor-options-i.md) | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | 否 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LinearAccelerometerResponse](arkts-sensorservice-sensor-linearaccelerometerresponse-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

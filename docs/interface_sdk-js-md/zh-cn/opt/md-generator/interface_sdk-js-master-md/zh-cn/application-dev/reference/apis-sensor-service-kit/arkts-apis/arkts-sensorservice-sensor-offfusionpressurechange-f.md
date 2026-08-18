# offFusionPressureChange

## 导入模块

```TypeScript
```

## offFusionPressureChange

```TypeScript
function offFusionPressureChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<FusionPressureResponse>): void
```

Unsubscribe to fusion pressure sensor data, {@code SensorId.FUSION_PRESSURE}.

**起始版本：** 23

<!--Device-sensor-function offFusionPressureChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<FusionPressureResponse>): void--><!--Device-sensor-function offFusionPressureChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<FusionPressureResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [sensorInfoParam](arkts-sensorservice-sensor-options-i.md) | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | 否 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FusionPressureResponse](arkts-sensorservice-sensor-fusionpressureresponse-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

# on_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION

## on_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION

```TypeScript
function on(type: SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION, callback: Callback<LinearAccelerometerResponse>,
    options?: Options): void
```

监听线性加速度传感器的数据变化。适用于需要获取排除重力影响的线性加速度数据的场景。如果多次调用该接口，仅最后一次调用生效。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [on](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#on_SensorId.COLOR)(type: SensorId.LINEAR_ACCELEROMETER, callback: Callback&lt;LinearAccelerometerResponse&gt;, options?: Options)

**需要权限：** ohos.permission.ACCELEROMETER

<!--Device-sensor-function on(type: SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION, callback: Callback<LinearAccelerometerResponse>,    options?: Options): void--><!--Device-sensor-function on(type: SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION, callback: Callback<LinearAccelerometerResponse>,    options?: Options): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LinearAccelerometerResponse](arkts-sensorservice-sensor-linearaccelerometerresponse-i.md)&gt; | 是 |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 否 |

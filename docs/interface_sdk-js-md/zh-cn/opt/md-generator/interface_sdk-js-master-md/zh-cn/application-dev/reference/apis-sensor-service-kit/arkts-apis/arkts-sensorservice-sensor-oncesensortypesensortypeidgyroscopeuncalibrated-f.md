# once_SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED

## once_SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED

```TypeScript
function once(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, callback: Callback<GyroscopeUncalibratedResponse>): void
```

监听未校准陀螺仪传感器的数据变化一次。适用于仅需一次性获取当前未校准陀螺仪数据的场景。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** once(type: SensorId.GYROSCOPE_UNCALIBRATED, callback: Callback&lt;GyroscopeUncalibratedResponse&gt;)

**需要权限：** ohos.permission.GYROSCOPE

<!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, callback: Callback<GyroscopeUncalibratedResponse>): void--><!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, callback: Callback<GyroscopeUncalibratedResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[GyroscopeUncalibratedResponse](arkts-sensorservice-sensor-gyroscopeuncalibratedresponse-i.md)&gt; | 是 |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, (data: sensor.GyroscopeUncalibratedResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
    console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
    console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
});
```

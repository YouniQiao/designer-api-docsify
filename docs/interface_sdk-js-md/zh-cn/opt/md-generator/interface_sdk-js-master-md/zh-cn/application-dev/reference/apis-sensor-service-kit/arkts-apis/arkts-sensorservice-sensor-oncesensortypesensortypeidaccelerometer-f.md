# once_SensorType.SENSOR_TYPE_ID_ACCELEROMETER

## once_SensorType.SENSOR_TYPE_ID_ACCELEROMETER

```TypeScript
function once(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback: Callback<AccelerometerResponse>): void
```

监听加速度传感器的数据变化一次。适用于仅需一次性获取当前加速度数据的场景。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** once(type: SensorId.ACCELEROMETER, callback: Callback&lt;AccelerometerResponse&gt;)

**需要权限：** ohos.permission.ACCELEROMETER

<!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback: Callback<AccelerometerResponse>): void--><!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback: Callback<AccelerometerResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_ACCELEROMETER | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AccelerometerResponse&gt; | 是 |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
  console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
});
```

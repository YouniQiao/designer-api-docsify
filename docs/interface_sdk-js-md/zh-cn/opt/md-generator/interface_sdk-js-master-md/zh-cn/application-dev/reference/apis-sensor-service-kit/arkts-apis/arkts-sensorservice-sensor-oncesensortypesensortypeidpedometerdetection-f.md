# once_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION

## once_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION

```TypeScript
function once(type: SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>): void
```

监听计步检测传感器数据变化一次。适用于仅需一次性获取当前计步检测数据的场景。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** once(type: SensorId.PEDOMETER_DETECTION, callback: Callback&lt;PedometerDetectionResponse&gt;)

**需要权限：** ohos.permission.ACTIVITY_MOTION

<!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>): void--><!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PedometerDetectionResponse](arkts-sensorservice-sensor-pedometerdetectionresponse-i.md)&gt; | 是 |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, (data: sensor.PedometerDetectionResponse) => {
  console.info('Succeeded in invoking once. Scalar data: ' + data.scalar);
});
```

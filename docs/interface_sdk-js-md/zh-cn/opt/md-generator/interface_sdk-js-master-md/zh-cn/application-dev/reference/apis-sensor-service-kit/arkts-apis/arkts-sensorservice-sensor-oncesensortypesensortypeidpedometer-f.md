# once_SensorType.SENSOR_TYPE_ID_PEDOMETER

## once_SensorType.SENSOR_TYPE_ID_PEDOMETER

```TypeScript
function once(type: SensorType.SENSOR_TYPE_ID_PEDOMETER, callback: Callback<PedometerResponse>): void
```

监听计步器传感器数据变化一次。适用于仅需一次性获取当前计步数据的场景。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** once(type: SensorId.PEDOMETER, callback: Callback&lt;PedometerResponse&gt;)

**需要权限：** ohos.permission.ACTIVITY_MOTION

<!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_PEDOMETER, callback: Callback<PedometerResponse>): void--><!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_PEDOMETER, callback: Callback<PedometerResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_PEDOMETER | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PedometerResponse](arkts-sensorservice-sensor-pedometerresponse-i.md)&gt; | 是 |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_PEDOMETER, (data: sensor.PedometerResponse) => {
  console.info('Succeeded in invoking once. Steps: ' + data.steps);
});
```

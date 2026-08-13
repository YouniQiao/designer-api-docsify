# off_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION

## off_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION

```TypeScript
function off(type: SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback?: Callback<PedometerDetectionResponse>): void
```

取消订阅计步检测传感器数据。off取消订阅必须与on订阅成对出现。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [off](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#off_SensorId.COLOR)(type: SensorId.PEDOMETER_DETECTION, callback?: Callback&lt;PedometerDetectionResponse&gt;)

**需要权限：** ohos.permission.ACTIVITY_MOTION

<!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback?: Callback<PedometerDetectionResponse>): void--><!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback?: Callback<PedometerDetectionResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PedometerDetectionResponse](arkts-sensorservice-sensor-pedometerdetectionresponse-i.md)&gt; | 否 |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.PedometerDetectionResponse) {
  console.info('Succeeded in invoking off. Scalar data: ' + data.scalar);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback);
```

# off_SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED

## off_SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED

```TypeScript
function off(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, callback?: Callback<GyroscopeUncalibratedResponse>): void
```

取消订阅未校准陀螺仪传感器数据。off取消订阅必须与on订阅成对出现。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [off](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#off_SensorId.COLOR)(type: SensorId.GYROSCOPE_UNCALIBRATED, callback?: Callback&lt;GyroscopeUncalibratedResponse&gt;)

**需要权限：** ohos.permission.GYROSCOPE

<!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, callback?: Callback<GyroscopeUncalibratedResponse>): void--><!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, callback?: Callback<GyroscopeUncalibratedResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[GyroscopeUncalibratedResponse](arkts-sensorservice-sensor-gyroscopeuncalibratedresponse-i.md)&gt; | 否 |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.GyroscopeUncalibratedResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, callback);
```

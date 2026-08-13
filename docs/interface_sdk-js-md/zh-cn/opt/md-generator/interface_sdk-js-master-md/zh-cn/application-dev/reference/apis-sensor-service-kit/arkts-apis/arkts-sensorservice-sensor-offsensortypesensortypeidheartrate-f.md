# off_SensorType.SENSOR_TYPE_ID_HEART_RATE

## off_SensorType.SENSOR_TYPE_ID_HEART_RATE

```TypeScript
function off(type: SensorType.SENSOR_TYPE_ID_HEART_RATE, callback?: Callback<HeartRateResponse>): void
```

取消订阅心率传感器数据。off取消订阅必须与on订阅成对出现。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [off](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#off_SensorId.COLOR)(type: SensorId.HEART_RATE, callback?: Callback&lt;HeartRateResponse&gt;)

**需要权限：** ohos.permission.HEALTH_DATA

<!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_HEART_RATE, callback?: Callback<HeartRateResponse>): void--><!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_HEART_RATE, callback?: Callback<HeartRateResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_HEART_RATE | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;HeartRateResponse&gt; | 否 |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.HeartRateResponse) {
  console.info('Succeeded in invoking off. Heart rate: ' + data.heartRate);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_HEART_RATE, callback);
```

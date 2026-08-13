# off_SensorType.SENSOR_TYPE_ID_GRAVITY

## off_SensorType.SENSOR_TYPE_ID_GRAVITY

```TypeScript
function off(type: SensorType.SENSOR_TYPE_ID_GRAVITY, callback?: Callback<GravityResponse>): void
```

取消订阅重力传感器数据。off取消订阅必须与on订阅成对出现。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [off](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#off_SensorId.COLOR)(type: SensorId.GRAVITY, callback?: Callback&lt;GravityResponse&gt;)

<!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_GRAVITY, callback?: Callback<GravityResponse>): void--><!--Device-sensor-function off(type: SensorType.SENSOR_TYPE_ID_GRAVITY, callback?: Callback<GravityResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_GRAVITY | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[GravityResponse](arkts-sensorservice-sensor-gravityresponse-i.md)&gt; | 否 |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.GravityResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
}

sensor.off(sensor.SensorType.SENSOR_TYPE_ID_GRAVITY, callback);
```

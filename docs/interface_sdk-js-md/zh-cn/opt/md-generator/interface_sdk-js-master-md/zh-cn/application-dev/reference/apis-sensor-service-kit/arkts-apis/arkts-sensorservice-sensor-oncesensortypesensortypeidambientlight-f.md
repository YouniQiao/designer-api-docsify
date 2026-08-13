# once_SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT

## once_SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT

```TypeScript
function once(type: SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT, callback: Callback<LightResponse>): void
```

监听环境光传感器数据变化一次。适用于仅需一次性获取当前环境光数据的场景。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** once(type: SensorId.AMBIENT_LIGHT, callback: Callback&lt;LightResponse&gt;)

<!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT, callback: Callback<LightResponse>): void--><!--Device-sensor-function once(type: SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT, callback: Callback<LightResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;LightResponse&gt; | 是 |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT, (data: sensor.LightResponse) => {
  console.info('Succeeded in invoking once. Illumination: ' + data.intensity);
});
```

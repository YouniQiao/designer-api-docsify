# once_SensorId.MAGNETIC_FIELD

## once_SensorId.MAGNETIC_FIELD

```TypeScript
function once(type: SensorId.MAGNETIC_FIELD, callback: Callback<MagneticFieldResponse>): void
```

获取一次磁场传感器数据。适用于仅需一次性获取当前磁场分量的场景。调用后，callback仅触发一次，自动取消订阅。

**起始版本：** 9

**废弃版本：** -1

<!--Device-sensor-function once(type: SensorId.MAGNETIC_FIELD, callback: Callback<MagneticFieldResponse>): void--><!--Device-sensor-function once(type: SensorId.MAGNETIC_FIELD, callback: Callback<MagneticFieldResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorId.MAGNETIC_FIELD | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MagneticFieldResponse](arkts-sensorservice-sensor-magneticfieldresponse-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.MAGNETIC_FIELD, (data: sensor.MagneticFieldResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

# once_SensorId.PEDOMETER_DETECTION

## once_SensorId.PEDOMETER_DETECTION

```TypeScript
function once(type: SensorId.PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>): void
```

获取一次计步检测器传感器数据。适用于仅需一次性检测计步事件的场景。调用后，callback仅触发一次，自动取消订阅。

**起始版本：** 9

**废弃版本：** -1

**需要权限：** ohos.permission.ACTIVITY_MOTION

<!--Device-sensor-function once(type: SensorId.PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>): void--><!--Device-sensor-function once(type: SensorId.PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorId.PEDOMETER_DETECTION | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PedometerDetectionResponse](arkts-sensorservice-sensor-pedometerdetectionresponse-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.once(sensor.SensorId.PEDOMETER_DETECTION, (data: sensor.PedometerDetectionResponse) => {
    console.info('Succeeded in invoking once. Scalar data: ' + data.scalar);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

# on_SensorId.SIGNIFICANT_MOTION

## on_SensorId.SIGNIFICANT_MOTION

```TypeScript
function on(type: SensorId.SIGNIFICANT_MOTION, callback: Callback<SignificantMotionResponse>,
    options?: Options): void
```

订阅有效运动传感器数据，用于检测用户拿起设备、明显移动或剧烈摇晃等有效运动事件。适用于需要根据用户活动状态唤醒设备、启动应用或切换模式的场景。

**起始版本：** 9

**废弃版本：** -1

<!--Device-sensor-function on(type: SensorId.SIGNIFICANT_MOTION, callback: Callback<SignificantMotionResponse>,    options?: Options): void--><!--Device-sensor-function on(type: SensorId.SIGNIFICANT_MOTION, callback: Callback<SignificantMotionResponse>,    options?: Options): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorId.SIGNIFICANT_MOTION | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SignificantMotionResponse](arkts-sensorservice-sensor-significantmotionresponse-i.md)&gt; | 是 |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 否 |

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
  sensor.on(sensor.SensorId.SIGNIFICANT_MOTION, (data: sensor.SignificantMotionResponse) => {
    console.info('Succeeded in invoking on. Scalar data: ' + data.scalar);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.SIGNIFICANT_MOTION);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

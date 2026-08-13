# on_SensorId.PROXIMITY

## on_SensorId.PROXIMITY

```TypeScript
function on(type: SensorId.PROXIMITY, callback: Callback<ProximityResponse>, options?: Options): void
```

订阅接近光传感器数据。接近光传感器用于检测物体与设备的距离状态，常用于通话时自动关闭屏幕以防止误触。当接近光事件被触发得较为频繁时，可通过options参数限定事件上报频率。 调用后，系统会通过callback持续上报接近状态数据。

**起始版本：** 9

**废弃版本：** -1

<!--Device-sensor-function on(type: SensorId.PROXIMITY, callback: Callback<ProximityResponse>, options?: Options): void--><!--Device-sensor-function on(type: SensorId.PROXIMITY, callback: Callback<ProximityResponse>, options?: Options): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorId.PROXIMITY | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ProximityResponse&gt; | 是 |
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
  // 订阅接近光传感器数据
  sensor.on(sensor.SensorId.PROXIMITY, (data: sensor.ProximityResponse) => {
    // 输出距离值
    console.info('Succeeded in invoking on. Distance: ' + data.distance);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.PROXIMITY);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

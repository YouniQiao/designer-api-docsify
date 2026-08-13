# on_SensorId.HUMIDITY

## on_SensorId.HUMIDITY

```TypeScript
function on(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>,
    options?: Options): void
```

订阅湿度传感器数据。湿度传感器用于测量周围环境的相对湿度，适用于环境湿度监测、智能家居联动等场景。调用后，系统会按设定频率通过callback持续上报湿度数据。

**起始版本：** 9

**废弃版本：** -1

<!--Device-sensor-function on(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>,    options?: Options): void--><!--Device-sensor-function on(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>,    options?: Options): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorId.HUMIDITY | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HumidityResponse](arkts-sensorservice-sensor-humidityresponse-i.md)&gt; | 是 |
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
  // 订阅湿度传感器数据
  sensor.on(sensor.SensorId.HUMIDITY, (data: sensor.HumidityResponse) => {
    // 输出湿度值
    console.info('Succeeded in invoking on. Humidity: ' + data.humidity);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.HUMIDITY);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

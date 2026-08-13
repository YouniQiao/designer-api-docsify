# on_SensorId.COLOR（系统接口）

## on_SensorId.COLOR

```TypeScript
function on(type: SensorId.COLOR, callback: Callback<ColorResponse>, options?: Options): void
```

订阅颜色传感器数据变化。通过回调函数异步上报颜色传感器数据，数据格式为ColorResponse对象，包含lightIntensity（光照强度）和colorTemperature（色温）两个number类型字段。

**起始版本：** 10

**废弃版本：** -1

<!--Device-sensor-function on(type: SensorId.COLOR, callback: Callback<ColorResponse>, options?: Options): void--><!--Device-sensor-function on(type: SensorId.COLOR, callback: Callback<ColorResponse>, options?: Options): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorId.COLOR | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ColorResponse](arkts-sensorservice-sensor-colorresponse-i-sys.md)&gt; | 是 |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try{
  sensor.on(sensor.SensorId.COLOR, (data: sensor.ColorResponse) => {
    console.info('Succeeded in getting the intensity of light: ' + data.lightIntensity);
    console.info('Succeeded in getting the color temperature: ' + data.colorTemperature);
  }, { interval: 100000000 });
  setTimeout(() => {
        sensor.off(sensor.SensorId.COLOR);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

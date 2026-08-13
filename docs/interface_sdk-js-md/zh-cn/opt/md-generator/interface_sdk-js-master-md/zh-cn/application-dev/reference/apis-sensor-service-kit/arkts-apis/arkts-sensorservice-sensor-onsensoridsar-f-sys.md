# on_SensorId.SAR（系统接口）

## on_SensorId.SAR

```TypeScript
function on(type: SensorId.SAR, callback: Callback<SarResponse>, options?: Options): void
```

订阅吸收比率传感器数据变化。通过回调函数异步上报SAR传感器数据，数据格式为SarResponse对象，包含absorptionRatio（吸收率）一个number类型字段。

**起始版本：** 10

**废弃版本：** -1

<!--Device-sensor-function on(type: SensorId.SAR, callback: Callback<SarResponse>, options?: Options): void--><!--Device-sensor-function on(type: SensorId.SAR, callback: Callback<SarResponse>, options?: Options): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorId.SAR | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SarResponse](arkts-sensorservice-sensor-sarresponse-i-sys.md)&gt; | 是 |
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

try {
  sensor.on(sensor.SensorId.SAR, (data: sensor.SarResponse) => {
    console.info('Succeeded in getting specific absorption rate : ' + data.absorptionRatio);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.SAR);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

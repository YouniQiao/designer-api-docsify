# onFusionPressureChange

## 导入模块

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onFusionPressureChange

```TypeScript
function onFusionPressureChange(callback: Callback<FusionPressureResponse>, options?: Options): void
```

Subscribe to fusion pressure sensor data, {@code SensorId.FUSION_PRESSURE}.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FusionPressureResponse](arkts-sensorservice-sensor-fusionpressureresponse-i.md)&gt; | 是 |
| options | [Options](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

**示例**

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.onFusionPressureChange((data: sensor.FusionPressureResponse) => {
    console.info('Succeeded in invoking onFusionPressureChange. fusionPressure: ' + data.fusionPressure);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.offFusionPressureChange();
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke onFusionPressureChange. Code: ${e.code}, message: ${e.message}`);
}
```

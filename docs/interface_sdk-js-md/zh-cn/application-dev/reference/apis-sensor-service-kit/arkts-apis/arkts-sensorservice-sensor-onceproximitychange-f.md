# onceProximityChange

## 导入模块

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onceProximityChange

```TypeScript
function onceProximityChange(callback: Callback<ProximityResponse>): void
```

Subscribe to proximity sensor data once, {@code SensorId.PROXIMITY}.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ProximityResponse&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sensor } from '@kit.SensorServiceKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.onceProximityChange((data: sensor.ProximityResponse) => {
    console.info('Succeeded in invoking onceProximityChange. Distance: ' + data.distance);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke onceProximityChange. Code: ${e.code}, message: ${e.message}`);
}
```

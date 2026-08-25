# onRotationVectorChange

## 导入模块

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onRotationVectorChange

```TypeScript
function onRotationVectorChange(callback: Callback<RotationVectorResponse>, options?: Options): void
```

Subscribe to rotation vector sensor data, {@code SensorId.ROTATION_VECTOR}.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RotationVectorResponse](arkts-sensorservice-sensor-rotationvectorresponse-i.md)&gt; | 是 |
| options | [Options](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 否 |

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
  sensor.onRotationVectorChange((data: sensor.RotationVectorResponse) => {
    console.info('Succeeded in invoking onRotationVectorChange. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking onRotationVectorChange. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking onRotationVectorChange. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking onRotationVectorChange. Scalar quantity: ' + data.w);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.offRotationVectorChange();
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke onRotationVectorChange. Code: ${e.code}, message: ${e.message}`);
}
```

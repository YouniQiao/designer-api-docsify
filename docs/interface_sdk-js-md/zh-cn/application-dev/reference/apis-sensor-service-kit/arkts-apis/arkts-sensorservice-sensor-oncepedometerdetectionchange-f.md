# oncePedometerDetectionChange

## 导入模块

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## oncePedometerDetectionChange

```TypeScript
function oncePedometerDetectionChange(callback: Callback<PedometerDetectionResponse>): void
```

Subscribe to pedometer detection sensor data once, {@code SensorId.PEDOMETER_DETECTION}.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ACTIVITY_MOTION

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PedometerDetectionResponse](arkts-sensorservice-sensor-pedometerdetectionresponse-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sensor } from '@kit.SensorServiceKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.oncePedometerDetectionChange((data: sensor.PedometerDetectionResponse) => {
    console.info('Succeeded in invoking oncePedometerDetectionChange. Scalar data: ' + data.scalar);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke oncePedometerDetectionChange. Code: ${e.code}, message: ${e.message}`);
}
```

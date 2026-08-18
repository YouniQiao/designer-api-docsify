# getSensorListSync

## 导入模块

```TypeScript
```

## getSensorListSync

```TypeScript
function getSensorListSync(): Array<Sensor>
```

获取设备上的所有传感器信息，使用同步方式返回结果。

**起始版本：** 23

<!--Device-sensor-function getSensorListSync(): Array<Sensor>--><!--Device-sensor-function getSensorListSync(): Array<Sensor>-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**返回值：**

| 类型 |
| --- |
| Array & lt;Sensor & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

**示例**

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let ret = sensor.getSensorListSync()
  for (let i = 0; i < ret.length; i++) {
    console.info('Succeeded in getting sensor: ' + JSON.stringify(ret[i]));
  }
} catch(error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to get singleSensor . Code: ${e.code}, message: ${e.message}`);
}
```

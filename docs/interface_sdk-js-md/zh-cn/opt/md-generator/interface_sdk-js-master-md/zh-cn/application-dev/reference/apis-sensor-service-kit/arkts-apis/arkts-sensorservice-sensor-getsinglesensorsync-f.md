# getSingleSensorSync

## 导入模块

```TypeScript
```

## getSingleSensorSync

```TypeScript
function getSingleSensorSync(type: SensorId): Sensor
```

获取指定类型的传感器信息，使用同步方式返回结果。

**起始版本：** 23

<!--Device-sensor-function getSingleSensorSync(type: SensorId): Sensor--><!--Device-sensor-function getSingleSensorSync(type: SensorId): Sensor-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [SensorId](arkts-sensorservice-sensor-sensorid-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Sensor](arkts-sensorservice-system-sensor-sensor-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |
| [14500102](../errorcode-sensor.md#14500102-设备不支持该传感器) |

**示例**

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let ret = sensor.getSingleSensorSync(sensor.SensorId.ACCELEROMETER);
  console.info('Succeeded in getting sensor: ' + JSON.stringify(ret));
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get singleSensor . Code: ${e.code}, message: ${e.message}`);
}
```

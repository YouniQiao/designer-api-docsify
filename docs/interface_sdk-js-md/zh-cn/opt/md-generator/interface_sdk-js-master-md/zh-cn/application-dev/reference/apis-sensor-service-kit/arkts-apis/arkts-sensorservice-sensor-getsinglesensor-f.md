# getSingleSensor

## getSingleSensor

```TypeScript
function getSingleSensor(type: SensorId, callback: AsyncCallback<Sensor>): void
```

获取指定传感器类型的属性信息，使用Callback异步方式返回结果。

**起始版本：** 9

<!--Device-sensor-function getSingleSensor(type: SensorId, callback: AsyncCallback<Sensor>): void--><!--Device-sensor-function getSingleSensor(type: SensorId, callback: AsyncCallback<Sensor>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [SensorId](arkts-sensorservice-sensor-sensorid-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Sensor&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |
| [14500102](../errorcode-sensor.md#14500102-设备不支持该传感器) |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.getSingleSensor(sensor.SensorId.ACCELEROMETER, (err: BusinessError, data: sensor.Sensor) => {
    if (err) {
      console.error(`Failed to get singleSensor. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in getting sensor: ' + JSON.stringify(data));
    sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
      console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
      console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
      console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
    }, { interval: 100000000 });
    setTimeout(() => {
      sensor.off(sensor.SensorId.ACCELEROMETER);
    }, 500);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get singleSensor. Code: ${e.code}, message: ${e.message}`);
}
```


## getSingleSensor

```TypeScript
function getSingleSensor(type: SensorId): Promise<Sensor>
```

获取指定类型的传感器信息，使用Promise异步方式返回结果。

**起始版本：** 9

<!--Device-sensor-function getSingleSensor(type: SensorId): Promise<Sensor>--><!--Device-sensor-function getSingleSensor(type: SensorId): Promise<Sensor>-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [SensorId](arkts-sensorservice-sensor-sensorid-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Sensor&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |
| [14500102](../errorcode-sensor.md#14500102-设备不支持该传感器) |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.getSingleSensor(sensor.SensorId.ACCELEROMETER).then((data: sensor.Sensor) => {
    console.info('Succeeded in getting sensor: ' + JSON.stringify(data));
  }, (err: BusinessError) => {
    console.error(`Failed to get singleSensor . Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get singleSensor . Code: ${e.code}, message: ${e.message}`);
}
```

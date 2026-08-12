# getSensorList

## getSensorList

```TypeScript
function getSensorList(callback: AsyncCallback<Array<Sensor>>): void
```

获取设备上的所有传感器信息，使用Callback异步方式返回结果。

**起始版本：** 9

<!--Device-sensor-function getSensorList(callback: AsyncCallback<Array<Sensor>>): void--><!--Device-sensor-function getSensorList(callback: AsyncCallback<Array<Sensor>>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Sensor&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14500101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-sensor-service-kit/errorcode-sensor.md#14500101-传感器服务异常) |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.getSensorList((err: BusinessError, data: Array<sensor.Sensor>) => {
    if (err) {
      console.error(`Failed to get sensorList. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data[' + i + ']: ' + JSON.stringify(data[i]));
    }
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
}
```


## getSensorList

```TypeScript
function getSensorList(): Promise<Array<Sensor>>
```

获取设备上的所有传感器信息，使用Promise异步方式返回结果。

**起始版本：** 9

<!--Device-sensor-function getSensorList(): Promise<Array<Sensor>>--><!--Device-sensor-function getSensorList(): Promise<Array<Sensor>>-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;Sensor & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14500101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-sensor-service-kit/errorcode-sensor.md#14500101-传感器服务异常) |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  sensor.getSensorList().then((data: Array<sensor.Sensor>) => {
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data[' + i + ']: ' + JSON.stringify(data[i]));
    }
  }, (err: BusinessError) => {
    console.error(`Failed to get sensorList. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
}
```

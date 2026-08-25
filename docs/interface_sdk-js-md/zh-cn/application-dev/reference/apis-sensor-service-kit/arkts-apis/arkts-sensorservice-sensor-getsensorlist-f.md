# getSensorList

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## getSensorList

```TypeScript
function getSensorList(callback: AsyncCallback<Array<Sensor>>): void
```

获取设备上的所有传感器信息。使用callback异步回调。如果需要同步获取传感器列表，请使用getSensorListSync。

**起始版本：** 9

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Sensor&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |


## getSensorList

```TypeScript
function getSensorList(): Promise<Array<Sensor>>
```

获取设备上的所有传感器信息。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Sensors.Sensor

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;Sensor & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

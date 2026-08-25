# getSingleSensor

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## getSingleSensor

```TypeScript
function getSingleSensor(type: SensorId, callback: AsyncCallback<Sensor>): void
```

获取指定传感器类型的属性信息。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [SensorId](arkts-sensorservice-sensor-sensorid-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Sensor&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |
| [14500102](../errorcode-sensor.md#14500102-设备不支持该传感器) |


## getSingleSensor

```TypeScript
function getSingleSensor(type: SensorId): Promise<Sensor>
```

获取指定类型的传感器信息。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [SensorId](arkts-sensorservice-sensor-sensorid-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Sensor & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |
| [14500102](../errorcode-sensor.md#14500102-设备不支持该传感器) |

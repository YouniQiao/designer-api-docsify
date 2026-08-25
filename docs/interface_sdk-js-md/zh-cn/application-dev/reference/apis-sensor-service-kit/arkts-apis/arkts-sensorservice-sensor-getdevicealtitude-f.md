# getDeviceAltitude

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## getDeviceAltitude

```TypeScript
function getDeviceAltitude(seaPressure: number, currentPressure: number, callback: AsyncCallback<number>): void
```

根据气压值获取海拔高度。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| seaPressure | number | 是 |
| currentPressure | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |


## getDeviceAltitude

```TypeScript
function getDeviceAltitude(seaPressure: number, currentPressure: number): Promise<number>
```

根据气压值获取海拔高度。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| seaPressure | number | 是 |
| currentPressure | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |

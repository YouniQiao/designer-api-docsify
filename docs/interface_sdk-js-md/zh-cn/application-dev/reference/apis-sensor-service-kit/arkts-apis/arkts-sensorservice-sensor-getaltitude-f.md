# getAltitude

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## getAltitude

```TypeScript
function getAltitude(seaPressure: number, currentPressure: number, callback: AsyncCallback<number>): void
```

根据气压值获取设备所在的海拔高度。使用callback异步回调。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md)(seaPressure: double, currentPressure: double, callback: AsyncCallback&lt;double&gt;)

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| seaPressure | number | 是 |
| currentPressure | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |


## getAltitude

```TypeScript
function getAltitude(seaPressure: number, currentPressure: number): Promise<number>
```

根据气压值获取设备所在的海拔高度。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md)(seaPressure: double, currentPressure: double)

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

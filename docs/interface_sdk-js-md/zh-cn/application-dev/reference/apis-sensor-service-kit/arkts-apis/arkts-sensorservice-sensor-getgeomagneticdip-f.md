# getGeomagneticDip

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## getGeomagneticDip

```TypeScript
function getGeomagneticDip(inclinationMatrix: Array<number>, callback: AsyncCallback<number>): void
```

根据倾斜矩阵计算地磁倾斜角。使用callback异步回调。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.getInclination](arkts-sensorservice-sensor-getinclination-f.md)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getInclination](arkts-sensorservice-sensor-getinclination-f.md)(inclinationMatrix: Array&lt;double&gt;, callback: AsyncCallback&lt;double&gt;)

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inclinationMatrix | Array & lt;number & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |


## getGeomagneticDip

```TypeScript
function getGeomagneticDip(inclinationMatrix: Array<number>): Promise<number>
```

根据倾斜矩阵计算地磁倾斜角。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.getInclination](arkts-sensorservice-sensor-getinclination-f.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getInclination](arkts-sensorservice-sensor-getinclination-f.md)(inclinationMatrix: Array&lt;double&gt;)

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inclinationMatrix | Array & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

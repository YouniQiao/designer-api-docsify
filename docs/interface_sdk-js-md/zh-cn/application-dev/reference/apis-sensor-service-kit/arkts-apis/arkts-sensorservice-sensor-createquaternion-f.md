# createQuaternion

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## createQuaternion

```TypeScript
function createQuaternion(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void
```

将旋转矢量转换为四元数。使用callback异步回调。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.getQuaternion](arkts-sensorservice-sensor-getquaternion-f.md)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getQuaternion](arkts-sensorservice-sensor-getquaternion-f.md)(rotationVector: Array&lt;double&gt;, callback: AsyncCallback&lt;Array&lt;double&gt;&gt;)

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rotationVector | Array & lt;number & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | 是 |


## createQuaternion

```TypeScript
function createQuaternion(rotationVector: Array<number>): Promise<Array<number>>
```

将旋转矢量转换为四元数。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.getQuaternion](arkts-sensorservice-sensor-getquaternion-f.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getQuaternion](arkts-sensorservice-sensor-getquaternion-f.md)(rotationVector: Array&lt;double&gt;)

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rotationVector | Array & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

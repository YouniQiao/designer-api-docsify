# createRotationMatrix

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## createRotationMatrix

```TypeScript
function createRotationMatrix(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void
```

将旋转矢量转换为旋转矩阵。使用callback异步回调。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md)(rotationVector: Array&lt;double&gt;, callback: AsyncCallback&lt;Array&lt;double&gt;&gt;)

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rotationVector | Array & lt;number & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | 是 |


## createRotationMatrix

```TypeScript
function createRotationMatrix(rotationVector: Array<number>): Promise<Array<number>>
```

将旋转矢量转换为旋转矩阵。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md)(rotationVector: Array&lt;double&gt;)

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rotationVector | Array & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |


## createRotationMatrix

```TypeScript
function createRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>, callback: AsyncCallback<RotationMatrixResponse>): void
```

根据重力矢量和地磁矢量计算旋转矩阵。使用callback异步回调。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md)(gravity: Array&lt;double&gt;, geomagnetic: Array&lt;double&gt;, callback: AsyncCallback&lt;RotationMatrixResponse&gt;)

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| gravity | Array & lt;number & gt; | 是 |
| geomagnetic | Array & lt;number & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RotationMatrixResponse](arkts-sensorservice-sensor-rotationmatrixresponse-i.md)&gt; | 是 |


## createRotationMatrix

```TypeScript
function createRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>,): Promise<RotationMatrixResponse>
```

根据重力矢量和地磁矢量计算旋转矩阵。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md)(gravity: Array&lt;double&gt;, geomagnetic: Array&lt;double&gt;)

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| gravity | Array & lt;number & gt; | 是 |
| geomagnetic | Array & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[RotationMatrixResponse](arkts-sensorservice-sensor-rotationmatrixresponse-i.md)&gt; |

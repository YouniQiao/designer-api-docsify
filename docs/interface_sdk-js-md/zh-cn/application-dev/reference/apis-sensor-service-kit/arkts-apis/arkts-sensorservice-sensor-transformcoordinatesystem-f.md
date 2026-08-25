# transformCoordinateSystem

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## transformCoordinateSystem

```TypeScript
function transformCoordinateSystem(inRotationVector: Array<number>, coordinates: CoordinatesOptions,
    callback: AsyncCallback<Array<number>>): void
```

旋转提供的旋转矩阵，使其可以以不同的方式表示坐标系。使用callback异步回调。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.transformRotationMatrix]
> [transformRotationMatrix](arkts-sensorservice-sensor-transformrotationmatrix-f.md)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [transformRotationMatrix](arkts-sensorservice-sensor-transformrotationmatrix-f.md)(inRotationVector: Array&lt;double&gt;, coordinates: CoordinatesOptions, callback: AsyncCallback&lt;Array&lt;double&gt;&gt;)

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inRotationVector | Array & lt;number & gt; | 是 |
| [coordinates](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-fontvariationinstance-i.md) | [CoordinatesOptions](arkts-sensorservice-sensor-coordinatesoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | 是 |


## transformCoordinateSystem

```TypeScript
function transformCoordinateSystem(inRotationVector: Array<number>, coordinates: CoordinatesOptions): Promise<Array<number>>
```

旋转提供的旋转矩阵，使其可以以不同的方式表示坐标系。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.transformRotationMatrix](arkts-sensorservice-sensor-transformrotationmatrix-f.md)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [transformRotationMatrix](arkts-sensorservice-sensor-transformrotationmatrix-f.md)(inRotationVector: Array&lt;double&gt;, coordinates: CoordinatesOptions)

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inRotationVector | Array & lt;number & gt; | 是 |
| [coordinates](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-fontvariationinstance-i.md) | [CoordinatesOptions](arkts-sensorservice-sensor-coordinatesoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

# getGeomagneticDip

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## getGeomagneticDip

```TypeScript
function getGeomagneticDip(inclinationMatrix: Array<number>, callback: AsyncCallback<number>): void
```

根据倾斜矩阵计算地磁倾斜角，使用Callback异步方式返回结果。

> **说明：**
> 
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.getInclination](arkts-sensorservice-sensor-getinclination-f.md#getinclination)
> 替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [sensor.getInclination](arkts-sensorservice-sensor-getinclination-f.md#getinclination)(inclinationMatrix:

<!--Device-sensor-function getGeomagneticDip(inclinationMatrix: Array<number>, callback: AsyncCallback<number>): void--><!--Device-sensor-function getGeomagneticDip(inclinationMatrix: Array<number>, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inclinationMatrix | Array&lt;number&gt; | Yes | 表示倾斜矩阵。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | 异步返回地磁倾斜角，单位为弧度。 |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.getGeomagneticDip([1, 0, 0, 0, 1, 0, 0, 0, 1], (err: BusinessError, data: number) => {
  if (err) {
    console.error(`Failed to register data. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info("Succeeded in getting getGeomagneticDip interface get data: " + data);
})
```


## getGeomagneticDip

```TypeScript
function getGeomagneticDip(inclinationMatrix: Array<number>): Promise<number>
```

根据倾斜矩阵计算地磁倾斜角，使用Promise异步方式返回结果。

> **说明：**
> 
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.getInclination](arkts-sensorservice-sensor-getinclination-f.md#getinclination)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [sensor.getInclination](arkts-sensorservice-sensor-getinclination-f.md#getinclination)(inclinationMatrix:

<!--Device-sensor-function getGeomagneticDip(inclinationMatrix: Array<number>): Promise<number>--><!--Device-sensor-function getGeomagneticDip(inclinationMatrix: Array<number>): Promise<number>-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inclinationMatrix | Array&lt;number&gt; | Yes | 表示倾斜矩阵。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | 使用异步方式返回地磁倾斜角，单位为弧度。 |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.getGeomagneticDip([1, 0, 0, 0, 1, 0, 0, 0, 1]);
promise.then((data: number) => {
  console.info('Succeeded in get GeomagneticDip_promise', data);
}).catch((err: BusinessError) => {
  console.error(`Failed to operate.`);
})
```


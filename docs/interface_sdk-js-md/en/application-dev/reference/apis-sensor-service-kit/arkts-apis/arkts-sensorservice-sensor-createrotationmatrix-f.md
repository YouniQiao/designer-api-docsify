# createRotationMatrix

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## createRotationMatrix

```TypeScript
function createRotationMatrix(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void
```

Converts a rotation vector into a rotation matrix. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md)(rotationVector: Array&lt;double&gt;, callback: AsyncCallback&lt;Array&lt;double&gt;&gt;)

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rotationVector | Array & lt;number & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | Yes |


## createRotationMatrix

```TypeScript
function createRotationMatrix(rotationVector: Array<number>): Promise<Array<number>>
```

Converts a rotation vector into a rotation matrix. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md)(rotationVector: Array&lt;double&gt;)

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rotationVector | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |


## createRotationMatrix

```TypeScript
function createRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>, callback: AsyncCallback<RotationMatrixResponse>): void
```

Obtains the rotation matrix based on a gravity vector and geomagnetic vector. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md)(gravity: Array&lt;double&gt;, geomagnetic: Array&lt;double&gt;, callback: AsyncCallback&lt;RotationMatrixResponse&gt;)

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| gravity | Array & lt;number & gt; | Yes |
| geomagnetic | Array & lt;number & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RotationMatrixResponse](arkts-sensorservice-sensor-rotationmatrixresponse-i.md)&gt; | Yes |


## createRotationMatrix

```TypeScript
function createRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>,): Promise<RotationMatrixResponse>
```

Obtains the rotation matrix based on a gravity vector and geomagnetic vector. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md)(gravity: Array&lt;double&gt;, geomagnetic: Array&lt;double&gt;)

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| gravity | Array & lt;number & gt; | Yes |
| geomagnetic | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[RotationMatrixResponse](arkts-sensorservice-sensor-rotationmatrixresponse-i.md)&gt; |

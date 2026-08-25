# getGeomagneticDip

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## getGeomagneticDip

```TypeScript
function getGeomagneticDip(inclinationMatrix: Array<number>, callback: AsyncCallback<number>): void
```

Obtains the magnetic dip based on the inclination matrix. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getInclination](arkts-sensorservice-sensor-getinclination-f.md)(inclinationMatrix: Array&lt;double&gt;, callback: AsyncCallback&lt;double&gt;)

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inclinationMatrix | Array & lt;number & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |


## getGeomagneticDip

```TypeScript
function getGeomagneticDip(inclinationMatrix: Array<number>): Promise<number>
```

Obtains the magnetic dip based on the inclination matrix. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getInclination](arkts-sensorservice-sensor-getinclination-f.md)(inclinationMatrix: Array&lt;double&gt;)

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inclinationMatrix | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

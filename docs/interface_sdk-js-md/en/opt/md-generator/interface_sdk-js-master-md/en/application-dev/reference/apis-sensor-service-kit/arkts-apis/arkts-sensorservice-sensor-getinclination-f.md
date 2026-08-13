# getInclination

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## getInclination

```TypeScript
function getInclination(inclinationMatrix: Array<number>, callback: AsyncCallback<number>): void
```

Obtains the magnetic dip based on the inclination matrix. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-sensor-function getInclination(inclinationMatrix: Array<double>, callback: AsyncCallback<double>): void--><!--Device-sensor-function getInclination(inclinationMatrix: Array<double>, callback: AsyncCallback<double>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inclinationMatrix | Array & lt;number & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // inclinationMatrix can be 3*3 or 4*4.
  let inclinationMatrix = [
    1, 0, 0,
    0, 1, 0,
    0, 0, 1
  ]
  sensor.getInclination(inclinationMatrix, (err: BusinessError, data: number) => {
    if (err) {
      console.error(`Failed to get inclination. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in getting inclination: ' + data);
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get inclination. Code: ${e.code}, message: ${e.message}`);
}
```


## getInclination

```TypeScript
function getInclination(inclinationMatrix: Array<number>): Promise<number>
```

Obtains the magnetic dip based on the inclination matrix. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-sensor-function getInclination(inclinationMatrix: Array<double>): Promise<double>--><!--Device-sensor-function getInclination(inclinationMatrix: Array<double>): Promise<double>-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inclinationMatrix | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // inclinationMatrix can be 3*3 or 4*4.
  let inclinationMatrix = [
    1, 0, 0,
    0, 1, 0,
    0, 0, 1
  ]
  const promise = sensor.getInclination(inclinationMatrix);
  promise.then((data: number) => {
    console.info('Succeeded in getting inclination: ' + data);
  }, (err: BusinessError) => {
    console.error(`Failed to get inclination. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get inclination. Code: ${e.code}, message: ${e.message}`);
}
```

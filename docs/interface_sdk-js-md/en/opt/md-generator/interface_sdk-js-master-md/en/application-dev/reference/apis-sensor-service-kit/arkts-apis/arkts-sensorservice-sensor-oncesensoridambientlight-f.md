# once_SensorId.AMBIENT_LIGHT

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## once_SensorId.AMBIENT_LIGHT

```TypeScript
function once(type: SensorId.AMBIENT_LIGHT, callback: Callback<LightResponse>): void
```

Obtains data of the ambient light sensor once.

**Since:** 9

**Deprecated since:** -1

<!--Device-sensor-function once(type: SensorId.AMBIENT_LIGHT, callback: Callback<LightResponse>): void--><!--Device-sensor-function once(type: SensorId.AMBIENT_LIGHT, callback: Callback<LightResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | SensorId.AMBIENT_LIGHT | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;LightResponse&gt; | Yes |

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
  sensor.once(sensor.SensorId.AMBIENT_LIGHT, (data: sensor.LightResponse) => {
    console.info('Succeeded in invoking once. the ambient light intensity: ' + data.intensity);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke once. Code: ${e.code}, message: ${e.message}`);
}
```

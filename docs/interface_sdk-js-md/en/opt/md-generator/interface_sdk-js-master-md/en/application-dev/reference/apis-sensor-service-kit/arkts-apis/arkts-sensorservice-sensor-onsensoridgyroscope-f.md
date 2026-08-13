# on_SensorId.GYROSCOPE

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## on_SensorId.GYROSCOPE

```TypeScript
function on(type: SensorId.GYROSCOPE, callback: Callback<GyroscopeResponse>,
    options?: Options): void
```

Subscribes to data of the gyroscope sensor.

**Since:** 9

**Deprecated since:** -1

**Required permissions:** ohos.permission.GYROSCOPE

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-sensor-function on(type: SensorId.GYROSCOPE, callback: Callback<GyroscopeResponse>,    options?: Options): void--><!--Device-sensor-function on(type: SensorId.GYROSCOPE, callback: Callback<GyroscopeResponse>,    options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | SensorId.GYROSCOPE | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;GyroscopeResponse&gt; | Yes |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.GYROSCOPE, (data: sensor.GyroscopeResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.GYROSCOPE);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

# on_SensorId.HEART_RATE

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## on_SensorId.HEART_RATE

```TypeScript
function on(type: SensorId.HEART_RATE, callback: Callback<HeartRateResponse>,
    options?: Options): void
```

Subscribes to data of the heart rate sensor.

**Since:** 9

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_HEALTH_DATA

<!--Device-sensor-function on(type: SensorId.HEART_RATE, callback: Callback<HeartRateResponse>,    options?: Options): void--><!--Device-sensor-function on(type: SensorId.HEART_RATE, callback: Callback<HeartRateResponse>,    options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | SensorId.HEART_RATE | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;HeartRateResponse&gt; | Yes |
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
  sensor.on(sensor.SensorId.HEART_RATE, (data: sensor.HeartRateResponse) => {
    console.info('Succeeded in invoking on. Heart rate: ' + data.heartRate);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.HEART_RATE);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

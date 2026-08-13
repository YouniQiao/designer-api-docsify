# on_SensorId.HUMIDITY

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## on_SensorId.HUMIDITY

```TypeScript
function on(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>,
    options?: Options): void
```

Subscribes to data of the humidity sensor.

**Since:** 9

**Deprecated since:** -1

<!--Device-sensor-function on(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>,    options?: Options): void--><!--Device-sensor-function on(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>,    options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | SensorId.HUMIDITY | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HumidityResponse](arkts-sensorservice-sensor-humidityresponse-i.md)&gt; | Yes |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No |

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
  sensor.on(sensor.SensorId.HUMIDITY, (data: sensor.HumidityResponse) => {
    console.info('Succeeded in invoking on. Humidity: ' + data.humidity);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.HUMIDITY);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```

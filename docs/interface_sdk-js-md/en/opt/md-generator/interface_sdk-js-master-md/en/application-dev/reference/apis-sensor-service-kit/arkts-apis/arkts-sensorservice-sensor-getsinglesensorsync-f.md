# getSingleSensorSync

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## getSingleSensorSync

```TypeScript
function getSingleSensorSync(type: SensorId): Sensor
```

Obtains information about the sensor of a specific type. This API returns the result synchronously.

**Since:** 12

<!--Device-sensor-function getSingleSensorSync(type: SensorId): Sensor--><!--Device-sensor-function getSingleSensorSync(type: SensorId): Sensor-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [SensorId](arkts-sensorservice-sensor-sensorid-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Sensor](arkts-sensorservice-system-sensor-sensor-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |
| [14500102](../errorcode-sensor.md#14500102-sensor-not-supported-by-the-device) |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  let ret = sensor.getSingleSensorSync(sensor.SensorId.ACCELEROMETER);
  console.info('Succeeded in getting sensor: ' + JSON.stringify(ret));
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get singleSensor . Code: ${e.code}, message: ${e.message}`);
}
```

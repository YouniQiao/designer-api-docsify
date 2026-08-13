# getSensorListSync

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## getSensorListSync

```TypeScript
function getSensorListSync(): Array<Sensor>
```

Obtains information about all sensors on the device. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** -1

<!--Device-sensor-function getSensorListSync(): Array<Sensor>--><!--Device-sensor-function getSensorListSync(): Array<Sensor>-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;Sensor & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  let ret = sensor.getSensorListSync()
  for (let i = 0; i < ret.length; i++) {
    console.info('Succeeded in getting sensor: ' + JSON.stringify(ret[i]));
  }
} catch(error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Failed to get singleSensor . Code: ${e.code}, message: ${e.message}`);
}
```

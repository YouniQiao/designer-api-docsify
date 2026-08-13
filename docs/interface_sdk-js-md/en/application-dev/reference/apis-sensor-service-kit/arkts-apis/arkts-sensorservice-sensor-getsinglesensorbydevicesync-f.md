# getSingleSensorByDeviceSync

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## getSingleSensorByDeviceSync

```TypeScript
function getSingleSensorByDeviceSync(type: SensorId, deviceId?: int): Array<Sensor>
```

Obtains information about the sensor of a specific type.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-sensor-function getSingleSensorByDeviceSync(type: SensorId, deviceId?: int): Array<Sensor>--><!--Device-sensor-function getSingleSensorByDeviceSync(type: SensorId, deviceId?: int): Array<Sensor>-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [SensorId](arkts-sensorservice-sensor-sensorid-e.md) | Yes | Sensor type. |
| deviceId | int | No | Device ID. The default value is **-1**, indicating the local device. You can use [getSensorList](arkts-sensorservice-sensor-getsensorlist-f.md#getSensorList) or [sensorStatusChange](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#on_SensorId.COLOR) to obtain the device ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;Sensor&gt; | Sensor attribute list. |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const deviceId = 1;
  // The second deviceId is optional.
  const sensorList: sensor.Sensor[] = sensor.getSingleSensorByDeviceSync(sensor.SensorId.ACCELEROMETER, deviceId);
  console.info(`sensorList length: ${sensorList.length}`);
  console.info(`sensorList Json: ${JSON.stringify(sensorList)}`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
}
```


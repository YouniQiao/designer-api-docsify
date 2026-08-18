# offSensorStatusChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## offSensorStatusChange

```TypeScript
function offSensorStatusChange(callback?: Callback<SensorStatusEvent>): void
```

Stop listening on device status changes.

**Since:** 23

<!--Device-sensor-function offSensorStatusChange(callback?: Callback<SensorStatusEvent>): void--><!--Device-sensor-function offSensorStatusChange(callback?: Callback<SensorStatusEvent>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[SensorStatusEvent](arkts-sensorservice-sensor-sensorstatusevent-i.md)&gt; | No | callback of sensor status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |


# onSensorStatusChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onSensorStatusChange

```TypeScript
function onSensorStatusChange(callback: Callback<SensorStatusEvent>): void
```

Start listening on device status changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-sensor-function onSensorStatusChange(callback: Callback<SensorStatusEvent>): void--><!--Device-sensor-function onSensorStatusChange(callback: Callback<SensorStatusEvent>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[SensorStatusEvent](arkts-sensorservice-sensor-sensorstatusevent-i.md)&gt; | Yes | callback of sensor status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14500101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-sensor-service-kit/errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |


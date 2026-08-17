# offMagneticFieldChange

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## offMagneticFieldChange

```TypeScript
function offMagneticFieldChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldResponse>): void
```

Unsubscribe to magnetic field sensor data, {@code SensorId.MAGNETIC_FIELD}.

**Since:** 23

<!--Device-sensor-function offMagneticFieldChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldResponse>): void--><!--Device-sensor-function offMagneticFieldChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensorInfoParam | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No | Parameters of sensor on the device. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MagneticFieldResponse](arkts-sensorservice-sensor-magneticfieldresponse-i.md)&gt; | No | callback magnetic field data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |


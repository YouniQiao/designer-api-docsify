# onceMagneticFieldChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onceMagneticFieldChange

```TypeScript
function onceMagneticFieldChange(callback: Callback<MagneticFieldResponse>): void
```

Subscribe to magnetic field sensor data once, {@code SensorId.MAGNETIC_FIELD}.

**Since:** 23

<!--Device-sensor-function onceMagneticFieldChange(callback: Callback<MagneticFieldResponse>): void--><!--Device-sensor-function onceMagneticFieldChange(callback: Callback<MagneticFieldResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MagneticFieldResponse](arkts-sensorservice-sensor-magneticfieldresponse-i.md)&gt; | Yes | callback magnetic field data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |


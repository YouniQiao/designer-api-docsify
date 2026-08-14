# onMagneticFieldChange

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## onMagneticFieldChange

```TypeScript
function onMagneticFieldChange(callback: Callback<MagneticFieldResponse>, options?: Options): void
```

Subscribe to magnetic field sensor data, {@code SensorId.MAGNETIC_FIELD}.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-sensor-function onMagneticFieldChange(callback: Callback<MagneticFieldResponse>, options?: Options): void--><!--Device-sensor-function onMagneticFieldChange(callback: Callback<MagneticFieldResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MagneticFieldResponse](arkts-sensorservice-sensor-magneticfieldresponse-i.md)&gt; | Yes | callback magnetic field data. |
| options | Options | No | Optional parameters specifying the interval at which sensor data is reported, <br> {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |


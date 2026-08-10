# onceMagneticFieldChange

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## onceMagneticFieldChange

```TypeScript
function onceMagneticFieldChange(callback: Callback<MagneticFieldResponse>): void
```

Subscribe to magnetic field sensor data once, {@code SensorId.MAGNETIC_FIELD}.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-sensor-function onceMagneticFieldChange(callback: Callback<MagneticFieldResponse>): void--><!--Device-sensor-function onceMagneticFieldChange(callback: Callback<MagneticFieldResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MagneticFieldResponse&gt; | Yes | callback magnetic field data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 14500101 | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |


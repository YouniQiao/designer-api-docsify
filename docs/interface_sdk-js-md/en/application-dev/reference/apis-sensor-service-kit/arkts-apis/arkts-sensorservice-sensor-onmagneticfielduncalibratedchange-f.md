# onMagneticFieldUncalibratedChange

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## onMagneticFieldUncalibratedChange

```TypeScript
function onMagneticFieldUncalibratedChange(callback: Callback<MagneticFieldUncalibratedResponse>, options?: Options): void
```

Subscribe to uncalibrated magnetic field sensor data, {@code SensorId.MAGNETIC_FIELD_UNCALIBRATED}.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-sensor-function onMagneticFieldUncalibratedChange(callback: Callback<MagneticFieldUncalibratedResponse>, options?: Options): void--><!--Device-sensor-function onMagneticFieldUncalibratedChange(callback: Callback<MagneticFieldUncalibratedResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MagneticFieldUncalibratedResponse&gt; | Yes | callback uncalibrated magnetic field data. |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No | Optional parameters specifying the interval at which sensor data is reported, &lt;br&gt; {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |


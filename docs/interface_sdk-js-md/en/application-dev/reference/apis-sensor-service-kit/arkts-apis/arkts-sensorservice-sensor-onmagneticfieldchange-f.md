# onMagneticFieldChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onMagneticFieldChange

```TypeScript
function onMagneticFieldChange(callback: Callback<MagneticFieldResponse>, options?: Options): void
```

Subscribe to magnetic field sensor data, {@code SensorId.MAGNETIC_FIELD}.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-sensor-function onMagneticFieldChange(callback: Callback<MagneticFieldResponse>, options?: Options): void--><!--Device-sensor-function onMagneticFieldChange(callback: Callback<MagneticFieldResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[MagneticFieldResponse](arkts-sensorservice-sensor-magneticfieldresponse-i.md)&gt; | Yes | callback magnetic field data. |
| options | Options | No | Optional parameters specifying the interval at which sensor data is reported, &lt;br&gt; {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [14500101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-sensor-service-kit/errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |


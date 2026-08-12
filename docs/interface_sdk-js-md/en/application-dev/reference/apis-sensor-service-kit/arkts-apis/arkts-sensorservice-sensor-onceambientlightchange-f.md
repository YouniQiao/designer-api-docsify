# onceAmbientLightChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onceAmbientLightChange

```TypeScript
function onceAmbientLightChange(callback: Callback<LightResponse>): void
```

Subscribe to ambient light sensor data once, {@code SensorId.AMBIENT_LIGHT}.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-sensor-function onceAmbientLightChange(callback: Callback<LightResponse>): void--><!--Device-sensor-function onceAmbientLightChange(callback: Callback<LightResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;LightResponse&gt; | Yes | callback ambient light data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [14500101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-sensor-service-kit/errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |


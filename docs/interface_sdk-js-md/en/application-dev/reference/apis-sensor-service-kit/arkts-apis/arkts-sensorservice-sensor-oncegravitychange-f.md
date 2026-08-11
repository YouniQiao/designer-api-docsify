# onceGravityChange

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## onceGravityChange

```TypeScript
function onceGravityChange(callback: Callback<GravityResponse>): void
```

Subscribe to gravity sensor data once, {@code SensorId.GRAVITY}.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-sensor-function onceGravityChange(callback: Callback<GravityResponse>): void--><!--Device-sensor-function onceGravityChange(callback: Callback<GravityResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;GravityResponse&gt; | Yes | callback gravity data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |


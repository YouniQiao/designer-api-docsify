# offProximityChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## offProximityChange

```TypeScript
function offProximityChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<ProximityResponse>): void
```

Unsubscribe to proximity sensor data, {@code SensorId.PROXIMITY}.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-sensor-function offProximityChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<ProximityResponse>): void--><!--Device-sensor-function offProximityChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<ProximityResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensorInfoParam | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No | Parameters of sensor on the device. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ProximityResponse&gt; | No | callback proximity data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |


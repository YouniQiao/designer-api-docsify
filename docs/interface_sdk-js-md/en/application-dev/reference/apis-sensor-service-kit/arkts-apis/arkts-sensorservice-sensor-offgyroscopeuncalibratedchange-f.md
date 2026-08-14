# offGyroscopeUncalibratedChange

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## offGyroscopeUncalibratedChange

```TypeScript
function offGyroscopeUncalibratedChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<GyroscopeUncalibratedResponse>): void
```

Unsubscribe to uncalibrated gyroscope sensor data, {@code SensorId.GYROSCOPE_UNCALIBRATED}.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GYROSCOPE

<!--Device-sensor-function offGyroscopeUncalibratedChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<GyroscopeUncalibratedResponse>): void--><!--Device-sensor-function offGyroscopeUncalibratedChange(sensorInfoParam?: SensorInfoParam, callback?: Callback<GyroscopeUncalibratedResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensorInfoParam | [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | No | Parameters of sensor on the device. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[GyroscopeUncalibratedResponse](arkts-sensorservice-sensor-gyroscopeuncalibratedresponse-i.md)&gt; | No | callback uncalibrated gyroscope data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |


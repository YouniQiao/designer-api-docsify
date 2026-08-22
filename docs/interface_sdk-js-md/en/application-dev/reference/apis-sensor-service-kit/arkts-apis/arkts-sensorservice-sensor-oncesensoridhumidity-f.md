# once_SensorId.HUMIDITY

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## once_SensorId.HUMIDITY

```TypeScript
function once(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>): void
```

Obtains data of the humidity sensor once.

**Since:** 9

<!--Device-sensor-function once(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>): void--><!--Device-sensor-function once(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorId.HUMIDITY | Yes | Sensor type. The value is fixed at **SensorId.HUMIDITY**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HumidityResponse](arkts-sensorservice-sensor-humidityresponse-i.md)&gt; | Yes | Callback used to report the sensor data, which is a **HumidityResponse** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br> 2. Incorrect parameter types; 3. Parameter verification failed. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |


# on_SensorId.FUSION_PRESSURE

## Modules to Import

```TypeScript
import { sensor } from 'sensor';
```

## on_SensorId.FUSION_PRESSURE

```TypeScript
function on(type: SensorId.FUSION_PRESSURE, callback: Callback<FusionPressureResponse>,
    options?: Options): void
```

Subscribes to the fused pressure sensor data.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Deprecated since:** -1

<!--Device-sensor-function on(type: SensorId.FUSION_PRESSURE, callback: Callback<FusionPressureResponse>,    options?: Options): void--><!--Device-sensor-function on(type: SensorId.FUSION_PRESSURE, callback: Callback<FusionPressureResponse>,    options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | SensorId.FUSION_PRESSURE | Yes | Sensor type. The value is fixed at SensorId.FUSION_PRESSURE. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FusionPressureResponse](arkts-sensorservice-sensor-fusionpressureresponse-i.md)&gt; | Yes | Callback used to report the sensor data, which is a **FusionPressureResponse** object. |
| options | Options | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br> 2. Incorrect parameter types; 3. Parameter verification failed. |
| [14500101](../errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; <br> 2. Sensor service ipc exception;3. Sensor data channel exception. |


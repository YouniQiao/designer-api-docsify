# onWearDetectionChange

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## onWearDetectionChange

```TypeScript
function onWearDetectionChange(callback: Callback<WearDetectionResponse>, options?: Options): void
```

Subscribe to wear detection sensor data, {@code SensorId.WEAR_DETECTION}.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-sensor-function onWearDetectionChange(callback: Callback<WearDetectionResponse>, options?: Options): void--><!--Device-sensor-function onWearDetectionChange(callback: Callback<WearDetectionResponse>, options?: Options): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[WearDetectionResponse](arkts-sensorservice-sensor-weardetectionresponse-i.md)&gt; | Yes | callback wear detection data. |
| options | Options | No | Optional parameters specifying the interval at which sensor data is reported, &lt;br&gt; {@code Options}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [14500101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-sensor-service-kit/errorcode-sensor.md#14500101-service-exception) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |


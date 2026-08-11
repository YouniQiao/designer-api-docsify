# offDistanceMeasure (System API)

## Modules to Import

```TypeScript
import { spatialAwareness } from 'kits/@kit.MultimodalAwarenessKit';
```

## offDistanceMeasure

```TypeScript
function offDistanceMeasure(configParams: DistanceMeasurementConfigParams,
    callback?: Callback<DistanceMeasurementResponse>): void
```

Unsubscribe from distance measurement result data.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_SENSING_WITH_ULTRASOUND

**Model restriction:** This API can be used only in the stage model.

<!--Device-spatialAwareness-function offDistanceMeasure(configParams: DistanceMeasurementConfigParams,    callback?: Callback<DistanceMeasurementResponse>): void--><!--Device-spatialAwareness-function offDistanceMeasure(configParams: DistanceMeasurementConfigParams,    callback?: Callback<DistanceMeasurementResponse>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.DistanceMeasurement

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| configParams | [DistanceMeasurementConfigParams](arkts-multimodalawareness-spatialawareness-distancemeasurementconfigparams-i-sys.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DistanceMeasurementResponse&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35100004](../../apis-multimodalawareness-kit/errorcode-spatialAwareness.md#35100004-invalid-parameter) |
| [35100003](../../apis-multimodalawareness-kit/errorcode-spatialAwareness.md#35100003-unsubscription-failed) |
| [35100001](../../apis-multimodalawareness-kit/errorcode-spatialAwareness.md#35100001-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { spatialAwareness } from '@kit.MultimodalAwarenessKit';
   console.info('call offDistanceMeasure before');
   let configParams: spatialAwareness.DistanceMeasurementConfigParams = {
      deviceList: ["123456"],
      techType: 2,
      reportMode: 0,
      reportFrequency: 340
   };
   console.info('call offDistanceMeasure start');
   try {
      spatialAwareness.offDistanceMeasure(configParams, (data:spatialAwareness.DistanceMeasurementResponse) => {
         console.info('result = ${data.distance}');
      });
   } catch (err) {
      console.error('call offDistanceMeasure failed, errCode = ' + err.code);
   }
```

# onIndoorOrOutdoorIdentify (System API)

## Modules to Import

```TypeScript
import { spatialAwareness } from '@kit.MultimodalAwarenessKit';
```

## onIndoorOrOutdoorIdentify

```TypeScript
function onIndoorOrOutdoorIdentify(configParams: DistanceMeasurementConfigParams,
    callback: Callback<DoorPositionResponse>): void
```

Subscribe to the results of indoorand outdoor identification.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_SENSING_WITH_ULTRASOUND

**Model restriction:** This API can be used only in the stage model.

<!--Device-spatialAwareness-function onIndoorOrOutdoorIdentify(configParams: DistanceMeasurementConfigParams,    callback: Callback<DoorPositionResponse>): void--><!--Device-spatialAwareness-function onIndoorOrOutdoorIdentify(configParams: DistanceMeasurementConfigParams,    callback: Callback<DoorPositionResponse>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.DistanceMeasurement

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| configParams | [DistanceMeasurementConfigParams](arkts-multimodalawareness-spatialawareness-distancemeasurementconfigparams-i-sys.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DoorPositionResponse](arkts-multimodalawareness-spatialawareness-doorpositionresponse-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35100004](../../apis-multimodalawareness-kit/errorcode-spatialAwareness.md#35100004-invalid-parameter) |
| [35100002](../../apis-multimodalawareness-kit/errorcode-spatialAwareness.md#35100002-subscription-failed) |
| [35100001](../../apis-multimodalawareness-kit/errorcode-spatialAwareness.md#35100001-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { spatialAwareness } from '@kit.MultimodalAwarenessKit';
   console.info('call onIndoorOrOutdoorIdentify before');
   let configParams: spatialAwareness.DistanceMeasurementConfigParams = {
      deviceList: ["123456"],
      techType: 2,
      reportMode: 0,
      reportFrequency: 340
   };
   console.info('call onIndoorOrOutdoorIdentify start');
   try {
      spatialAwareness.onIndoorOrOutdoorIdentify(configParams, (data:spatialAwareness.DoorPositionResponse) => {
         console.info('result = ${data.position}');
      });
   } catch (err) {
      console.error('call onIndoorOrOutdoorIdentify failed, errCode = ' + err.code);
   }
```

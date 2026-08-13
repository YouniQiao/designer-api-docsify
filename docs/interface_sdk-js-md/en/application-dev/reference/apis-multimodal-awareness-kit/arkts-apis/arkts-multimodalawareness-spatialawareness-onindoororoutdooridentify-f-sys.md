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

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_SENSING_WITH_ULTRASOUND

**Model restriction:** This API can be used only in the stage model.

<!--Device-spatialAwareness-function onIndoorOrOutdoorIdentify(configParams: DistanceMeasurementConfigParams,    callback: Callback<DoorPositionResponse>): void--><!--Device-spatialAwareness-function onIndoorOrOutdoorIdentify(configParams: DistanceMeasurementConfigParams,    callback: Callback<DoorPositionResponse>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.DistanceMeasurement

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| configParams | [DistanceMeasurementConfigParams](arkts-multimodalawareness-spatialawareness-distancemeasurementconfigparams-i-sys.md) | Yes | Configuration parameters for identification inside and &lt;br&gt; outside the door. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DoorPositionResponse](arkts-multimodalawareness-spatialawareness-doorpositionresponse-i-sys.md)&gt; | Yes | Callback for identification inside and outside the door. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Function can not work correctly due to &lt;br&gt; limited device capabilities. |
| [35100004](../../apis-multimodalawareness-kit/errorcode-spatialAwareness.md#35100004-invalid-parameter) | Parameter invalid. |
| [35100002](../../apis-multimodalawareness-kit/errorcode-spatialAwareness.md#35100002-subscription-failed) | Subscription failed. |
| [35100001](../../apis-multimodalawareness-kit/errorcode-spatialAwareness.md#35100001-service-exception) | Service exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

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


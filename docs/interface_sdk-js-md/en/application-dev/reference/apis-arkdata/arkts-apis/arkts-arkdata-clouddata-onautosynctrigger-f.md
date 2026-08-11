# onAutoSyncTrigger

## Modules to Import

```TypeScript
import { cloudData } from 'kits/@kit.ArkData';
```

## onAutoSyncTrigger

```TypeScript
function onAutoSyncTrigger(observer: Callback<AutoSyncTriggerInfo>): void
```

Describes the triggering method for automatic device-cloud synchronization subscription.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-cloudData-function onAutoSyncTrigger(observer: Callback<AutoSyncTriggerInfo>): void--><!--Device-cloudData-function onAutoSyncTrigger(observer: Callback<AutoSyncTriggerInfo>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AutoSyncTriggerInfo&gt; | Yes | Callback for automatic synchronization trigger interception. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |


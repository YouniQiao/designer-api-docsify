# offAutoSyncTrigger

## Modules to Import

```TypeScript
import { cloudData } from '@kit.ArkData';
```

## offAutoSyncTrigger

```TypeScript
function offAutoSyncTrigger(observer?: Callback<AutoSyncTriggerInfo>): void
```

Describes unsubscribing from the device-cloud automatic synchronization trigger mode.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AutoSyncTriggerInfo](arkts-arkdata-clouddata-autosynctriggerinfo-i.md)&gt; | No | Callback for automatic synchronization trigger interception. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

**Examples**

```TypeScript
function autoSyncTriggerObserver(info: cloudData.AutoSyncTriggerInfo) {
  console.info(`Auto sync triggered, mode: ${info.mode}`);
}

// Subscribe to an observer.
cloudData.onAutoSyncTrigger(autoSyncTriggerObserver);

// Unsubscribe from a specified observer.
cloudData.offAutoSyncTrigger(autoSyncTriggerObserver);

// Unsubscribe from all observers.
cloudData.offAutoSyncTrigger();
```

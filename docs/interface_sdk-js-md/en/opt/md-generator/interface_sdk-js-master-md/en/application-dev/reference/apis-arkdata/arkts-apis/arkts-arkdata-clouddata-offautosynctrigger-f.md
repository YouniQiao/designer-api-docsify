# offAutoSyncTrigger

## Modules to Import

```TypeScript
```

## offAutoSyncTrigger

```TypeScript
function offAutoSyncTrigger(observer?: Callback<AutoSyncTriggerInfo>): void
```

Describes unsubscribing from the device-cloud automatic synchronization trigger mode.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-cloudData-function offAutoSyncTrigger(observer?: Callback<AutoSyncTriggerInfo>): void--><!--Device-cloudData-function offAutoSyncTrigger(observer?: Callback<AutoSyncTriggerInfo>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AutoSyncTriggerInfo](arkts-arkdata-clouddata-autosynctriggerinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

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

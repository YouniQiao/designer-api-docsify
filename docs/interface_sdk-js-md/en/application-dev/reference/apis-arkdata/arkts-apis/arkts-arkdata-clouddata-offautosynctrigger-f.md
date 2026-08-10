# offAutoSyncTrigger

## Modules to Import

```TypeScript
import { cloudData } from 'kits/@kit.ArkData';
```

## offAutoSyncTrigger

```TypeScript
function offAutoSyncTrigger(observer?: Callback<AutoSyncTriggerInfo>): void
```

取消订阅自动同步触发事件通知。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-cloudData-function offAutoSyncTrigger(observer?: Callback<AutoSyncTriggerInfo>): void--><!--Device-cloudData-function offAutoSyncTrigger(observer?: Callback<AutoSyncTriggerInfo>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AutoSyncTriggerInfo&gt; | No | 回调函数。 若传入observer，则取消指定回调函数的订阅；若不传入observer，则取消所有已注册的订阅。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |

## Examples

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


# onApplicationStateChange (System API)

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## onApplicationStateChange

```TypeScript
function onApplicationStateChange(observer: ApplicationStateObserver, filter: AppStateFilter): int
```

Register application state observer with filter.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver, filter: AppStateFilter): int--><!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver, filter: AppStateFilter): int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | ApplicationStateObserver | Yes | The application state observer. |
| filter | [AppStateFilter](arkts-ability-appmanager-appstatefilter-i-sys.md) | Yes | Filter configuration for targeted monitoring. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the number code of the observer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |


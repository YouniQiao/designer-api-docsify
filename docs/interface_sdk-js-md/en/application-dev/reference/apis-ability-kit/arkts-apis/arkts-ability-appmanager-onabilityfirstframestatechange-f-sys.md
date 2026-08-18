# onAbilityFirstFrameStateChange (System API)

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { appManager } from '@kit.AbilityKit';
```

## onAbilityFirstFrameStateChange

```TypeScript
function onAbilityFirstFrameStateChange(observer: AbilityFirstFrameStateObserver, bundleName?: string): void
```

Register ability first frame state observe.

**Since:** 23

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function onAbilityFirstFrameStateChange(observer: AbilityFirstFrameStateObserver, bundleName?: string): void--><!--Device-appManager-function onAbilityFirstFrameStateChange(observer: AbilityFirstFrameStateObserver, bundleName?: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | AbilityFirstFrameStateObserver | Yes | The ability first frame state observer. |
| bundleName | string | No | The target bundle name. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |


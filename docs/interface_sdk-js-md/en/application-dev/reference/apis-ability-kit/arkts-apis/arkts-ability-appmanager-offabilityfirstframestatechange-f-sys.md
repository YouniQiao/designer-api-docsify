# offAbilityFirstFrameStateChange (System API)

## offAbilityFirstFrameStateChange

```TypeScript
function offAbilityFirstFrameStateChange(observer?: AbilityFirstFrameStateObserver): void
```

Unregister ability first frame state observer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function offAbilityFirstFrameStateChange(observer?: AbilityFirstFrameStateObserver): void--><!--Device-appManager-function offAbilityFirstFrameStateChange(observer?: AbilityFirstFrameStateObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | The ability first frame state observer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |


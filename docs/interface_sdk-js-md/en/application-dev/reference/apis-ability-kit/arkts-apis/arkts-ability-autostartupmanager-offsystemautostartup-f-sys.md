# offSystemAutoStartup (System API)

## Modules to Import

```TypeScript
import { autoStartupManager } from 'autoStartupManager';
```

## offSystemAutoStartup

```TypeScript
function offSystemAutoStartup(callback?: AutoStartupCallback): void
```

Unregister listener that watches for all applications auto startup state.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_APP_BOOT

**Model restriction:** This API can be used only in the stage model.

<!--Device-autoStartupManager-function offSystemAutoStartup(callback?: AutoStartupCallback): void--><!--Device-autoStartupManager-function offSystemAutoStartup(callback?: AutoStartupCallback): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AutoStartupCallback](arkts-ability-autostartupcallback-i-sys.md) | No | Auto startup callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Connect to system server failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied, interface caller does not have permission "ohos.permission.MANAGE_APP_BOOT". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |


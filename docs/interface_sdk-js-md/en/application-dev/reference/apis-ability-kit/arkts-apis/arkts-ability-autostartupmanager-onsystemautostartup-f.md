# onSystemAutoStartup

## onSystemAutoStartup

```TypeScript
function onSystemAutoStartup(callback: AutoStartupCallback): void
```

Register the listener that watches for all applications auto startup state.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.MANAGE_APP_BOOT

**Model restriction:** This API can be used only in the stage model.

<!--Device-autoStartupManager-function onSystemAutoStartup(callback: AutoStartupCallback): void--><!--Device-autoStartupManager-function onSystemAutoStartup(callback: AutoStartupCallback): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Auto startup callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied, interface caller does not have permission "ohos.permission.MANAGE\_\_\_ESCAPED\_UNDERSCORE\_\_\_APP\_\_\_ESCAPED\_UNDERSCORE\_\_\_BOOT". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Connect to system server failed. |


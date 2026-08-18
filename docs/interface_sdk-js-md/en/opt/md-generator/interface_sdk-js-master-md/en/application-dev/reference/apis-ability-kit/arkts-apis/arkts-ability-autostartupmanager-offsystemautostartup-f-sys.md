# offSystemAutoStartup (System API)

## Modules to Import

```TypeScript
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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AutoStartupCallback](arkts-ability-autostartupcallback-i-sys.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

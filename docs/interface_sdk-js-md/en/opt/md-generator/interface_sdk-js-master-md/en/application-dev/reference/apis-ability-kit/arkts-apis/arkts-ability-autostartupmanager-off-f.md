# off

## Modules to Import

```TypeScript
import { autoStartupManager } from 'kits/@kit.AbilityKit';
```

## off('systemAutoStartup')

```TypeScript
function off(type: 'systemAutoStartup', callback?: AutoStartupCallback): void
```

Unregisters the callback used to listen for auto-startup status changes of an application component.Starting from API version 18, this API can be properly called on 2-in-1 devices and wearables. If it is called on other device types, error code 16000050 is returned.For versions earlier than API version 18, this API can be properly called only on 2-in-1 devices. If it is called on other device types, error code 16000050 is returned.

**Since:** 11

**Required permissions:** ohos.permission.MANAGE_APP_BOOT

**Model restriction:** This API can be used only in the stage model.

<!--Device-autoStartupManager-function off(type: 'systemAutoStartup', callback?: AutoStartupCallback): void--><!--Device-autoStartupManager-function off(type: 'systemAutoStartup', callback?: AutoStartupCallback): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'systemAutoStartup' | Yes |
| callback | [AutoStartupCallback](arkts-ability-autostartupcallback-i-sys.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

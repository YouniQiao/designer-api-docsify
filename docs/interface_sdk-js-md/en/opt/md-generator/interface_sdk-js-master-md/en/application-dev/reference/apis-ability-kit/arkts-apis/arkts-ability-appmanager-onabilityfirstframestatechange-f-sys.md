# onAbilityFirstFrameStateChange (System API)

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## onAbilityFirstFrameStateChange

```TypeScript
function onAbilityFirstFrameStateChange(observer: AbilityFirstFrameStateObserver, bundleName?: string): void
```

Register ability first frame state observe.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function onAbilityFirstFrameStateChange(observer: AbilityFirstFrameStateObserver, bundleName?: string): void--><!--Device-appManager-function onAbilityFirstFrameStateChange(observer: AbilityFirstFrameStateObserver, bundleName?: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [AbilityFirstFrameStateObserver](arkts-ability-appmanager-abilityfirstframestateobserver-t-sys.md) | Yes |
| bundleName | string | No |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

# on_abilityFirstFrameState (System API)

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## on_abilityFirstFrameState

```TypeScript
function on(type: 'abilityFirstFrameState', observer: AbilityFirstFrameStateObserver, bundleName?: string): void
```

Registers an observer to listen for the complete of the first frame rendering of a given ability.

**Since:** 12

**Deprecated since:** -1

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function on(type: 'abilityFirstFrameState', observer: AbilityFirstFrameStateObserver, bundleName?: string): void--><!--Device-appManager-function on(type: 'abilityFirstFrameState', observer: AbilityFirstFrameStateObserver, bundleName?: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'abilityFirstFrameState' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [AbilityFirstFrameStateObserver](arkts-ability-appmanager-abilityfirstframestateobserver-t-sys.md) | Yes |
| bundleName | string | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityFirstFrameStateObserverForAll: appManager.AbilityFirstFrameStateObserver = {
  onAbilityFirstFrameDrawn(abilityStateData: appManager.AbilityFirstFrameStateData) {
    console.info("abilityFirstFrame: ", JSON.stringify(abilityStateData));
  }
};

try {
  appManager.on('abilityFirstFrameState', abilityFirstFrameStateObserverForAll);
} catch (e) {
  let code = (e as BusinessError).code;
  let message = (e as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```

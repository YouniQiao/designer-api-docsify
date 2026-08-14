# on_abilityFirstFrameState (System API)

## Modules to Import

```TypeScript
import { appManager } from 'appManager';
```

## on_abilityFirstFrameState

```TypeScript
function on(type: 'abilityFirstFrameState', observer: AbilityFirstFrameStateObserver, bundleName?: string): void
```

Registers an observer to listen for the complete of the first frame rendering of a given ability.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function on(type: 'abilityFirstFrameState', observer: AbilityFirstFrameStateObserver, bundleName?: string): void--><!--Device-appManager-function on(type: 'abilityFirstFrameState', observer: AbilityFirstFrameStateObserver, bundleName?: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'abilityFirstFrameState' | Yes | Event type. It is fixed at **'abilityFirstFrameState'**. |
| observer | AbilityFirstFrameStateObserver | Yes | Observer used to listen for the complete of the first frame rendering of the ability. |
| bundleName | string | No | Bundle name of the ability to be listened for. If this parameter is left blank, the event is listened for all applications. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

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


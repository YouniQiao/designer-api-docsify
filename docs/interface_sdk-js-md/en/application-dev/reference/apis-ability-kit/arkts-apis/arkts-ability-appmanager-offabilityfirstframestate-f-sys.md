# off_abilityFirstFrameState (System API)

## Modules to Import

```TypeScript
import { appManager } from 'appManager';
```

## off_abilityFirstFrameState

```TypeScript
function off(type: 'abilityFirstFrameState', observer?: AbilityFirstFrameStateObserver): void
```

Deregisters the observer used to listen for the complete of the first frame rendering of a given ability.

**Since:** 12

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function off(type: 'abilityFirstFrameState', observer?: AbilityFirstFrameStateObserver): void--><!--Device-appManager-function off(type: 'abilityFirstFrameState', observer?: AbilityFirstFrameStateObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'abilityFirstFrameState' | Yes | Event type. It is fixed at **'abilityFirstFrameState'**. |
| observer | AbilityFirstFrameStateObserver | No | Callback used for deregistration. If this parameter is left blank , all subscriptions to the specified event are canceled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

**Examples**

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

try {
  appManager.off('abilityFirstFrameState', abilityFirstFrameStateObserverForAll);
} catch (e) {
  let code = (e as BusinessError).code;
  let message = (e as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```


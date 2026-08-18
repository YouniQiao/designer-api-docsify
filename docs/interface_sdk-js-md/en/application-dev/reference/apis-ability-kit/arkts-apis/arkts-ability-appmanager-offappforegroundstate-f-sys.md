# off_appForegroundState (System API)

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { appManager } from '@kit.AbilityKit';
```

## off_appForegroundState

```TypeScript
function off(type: 'appForegroundState', observer?: AppForegroundStateObserver): void
```

Unregisters the observer used to listen for application start or exit events.

**Since:** 11

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function off(type: 'appForegroundState', observer?: AppForegroundStateObserver): void--><!--Device-appManager-function off(type: 'appForegroundState', observer?: AppForegroundStateObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'appForegroundState' | Yes | Event type. It is fixed at **'appForegroundState'**. |
| observer | AppForegroundStateObserver | No | Observer used to listen for application start or exit events. |

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

let observer_: appManager.AppForegroundStateObserver | undefined;
// 1. Register an observer to listen for application start or exit events.
let observer: appManager.AppForegroundStateObserver = {
  onAppStateChanged(appStateData: appManager.AppStateData) {
    console.info(`[appManager] onAppStateChanged: ${JSON.stringify(appStateData)}`);
  },
};

try {
  appManager.on('appForegroundState', observer);
  // Save the observer object.
  observer_ = observer;
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}

// 2. Deregister the observer.
try {
  appManager.off('appForegroundState',  observer_);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```


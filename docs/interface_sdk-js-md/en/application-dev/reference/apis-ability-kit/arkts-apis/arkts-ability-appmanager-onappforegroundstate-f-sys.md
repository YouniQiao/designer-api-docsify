# on_appForegroundState (System API)

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## on('appForegroundState')

```TypeScript
function on(type: 'appForegroundState', observer: AppForegroundStateObserver): void
```

Registers an observer to listen for application start or exit events. The observer can be used by a system application to observe the start or event events of all applications.

**Since:** 11

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function on(type: 'appForegroundState', observer: AppForegroundStateObserver): void--><!--Device-appManager-function on(type: 'appForegroundState', observer: AppForegroundStateObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'appForegroundState' | Yes | Event type. It is fixed at **'appForegroundState'**. |
| observer | AppForegroundStateObserver | Yes | Observer used to listen for application start or exit events. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

**Examples**

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observer: appManager.AppForegroundStateObserver = {
  onAppStateChanged(appStateData) {
    console.info(`[appManager] onAppStateChanged: ${JSON.stringify(appStateData)}`);
  },
};

try {
  appManager.on('appForegroundState', observer);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```


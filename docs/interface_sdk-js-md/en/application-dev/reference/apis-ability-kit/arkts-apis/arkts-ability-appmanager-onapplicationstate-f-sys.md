# on_applicationState (System API)

## Modules to Import

```TypeScript
import { appManager } from 'appManager';
```

## on_applicationState

```TypeScript
function on(type: 'applicationState', observer: ApplicationStateObserver, filter: AppStateFilter): int
```

Registers an application state observer, which allows you to filter for specific application lifecycle changes by setting filter criteria.

**Since:** 21

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function on(type: 'applicationState', observer: ApplicationStateObserver, filter: AppStateFilter): int--><!--Device-appManager-function on(type: 'applicationState', observer: ApplicationStateObserver, filter: AppStateFilter): int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'applicationState' | Yes | Type of the API to call. It is fixed at **'applicationState'**. |
| observer | ApplicationStateObserver | Yes | Application state observer, which is used to listen for application lifecycle changes. |
| filter | [AppStateFilter](arkts-ability-appmanager-appstatefilter-i-sys.md) | Yes | Filter for application lifecycle changes. |

**Return value:**

| Type | Description |
| --- | --- |
| int | ID of the observer registered. You can pass this ID to [off]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

**Examples**

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let applicationStateObserver: appManager.ApplicationStateObserver = {
  onForegroundApplicationChanged(appStateData: appManager.AppStateData) {
    console.info(`[appManager] onForegroundApplicationChanged: ${JSON.stringify(appStateData)}`);
  },
  onAbilityStateChanged(abilityStateData: appManager.AbilityStateData) {
    console.info(`[appManager] onAbilityStateChanged: ${JSON.stringify(abilityStateData)}`);
  },
  onProcessCreated(processData: appManager.ProcessData) {
    console.info(`[appManager] onProcessCreated: ${JSON.stringify(processData)}`);
  },
  onProcessDied(processData: appManager.ProcessData) {
    console.info(`[appManager] onProcessDied: ${JSON.stringify(processData)}`);
  },
  onProcessStateChanged(processData: appManager.ProcessData) {
    console.info(`[appManager] onProcessStateChanged: ${JSON.stringify(processData)}`);
  },
  onAppStarted(appStateData: appManager.AppStateData) {
    console.info(`[appManager] onAppStarted: ${JSON.stringify(appStateData)}`);
  },
  onAppStopped(appStateData: appManager.AppStateData) {
    console.info(`[appManager] onAppStopped: ${JSON.stringify(appStateData)}`);
  }
};

/* This example uses the filter to listen for the following application callbacks:
 * 1. onAbilityStateChanged, a callback function used to listen for ability components in the creating state.
 * 2. onProcessCreated, a callback function used to listen for processes in the created state.
 */
let appStateFilter: appManager.AppStateFilter = {
    bundleTypes: appManager.FilterBundleType.APP,
    appStateTypes: appManager.FilterAppStateType.CREATE | appManager.FilterAppStateType.FOREGROUND,
    processStateTypes: appManager.FilterProcessStateType.CREATE,
    abilityStateTypes: appManager.FilterAbilityStateType.CREATE,
    callbacks: appManager.FilterCallback.ON_ABILITY_STATE_CHANGED | appManager.FilterCallback.ON_PROCESS_CREATED
};

try {
  const observerId = appManager.on('applicationState', applicationStateObserver, appStateFilter);
  console.info(`[appManager] observerCode: ${observerId}`);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```


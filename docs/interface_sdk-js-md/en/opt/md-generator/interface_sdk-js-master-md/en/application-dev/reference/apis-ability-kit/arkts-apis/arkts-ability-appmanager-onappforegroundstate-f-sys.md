# on_appForegroundState (System API)

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## on_appForegroundState

```TypeScript
function on(type: 'appForegroundState', observer: AppForegroundStateObserver): void
```

Registers an observer to listen for application start or exit events. The observer can be used by a system application to observe the start or event events of all applications.

**Since:** 11

**Deprecated since:** -1

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function on(type: 'appForegroundState', observer: AppForegroundStateObserver): void--><!--Device-appManager-function on(type: 'appForegroundState', observer: AppForegroundStateObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'appForegroundState' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [AppForegroundStateObserver](../../apis-na/arkts-apis/arkts-na-appforegroundstateobserver-i-sys.md) | Yes |

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

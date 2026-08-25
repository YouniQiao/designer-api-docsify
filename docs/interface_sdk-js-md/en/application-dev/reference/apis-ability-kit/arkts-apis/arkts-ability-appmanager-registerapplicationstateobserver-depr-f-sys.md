# registerApplicationStateObserver (System API)

## Modules to Import

```TypeScript
```

## registerApplicationStateObserver

```TypeScript
function registerApplicationStateObserver(observer: ApplicationStateObserver): number
```

Register application state observer.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Deprecated since:** 9

**Substitutes:** [on](arkts-ability-appmanager-on-f.md#onapplicationstate)

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [ApplicationStateObserver](arkts-ability-applicationstateobserver-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
import appManager from '@ohos.application.appManager';

const observerCode = appManager.registerApplicationStateObserver({
  onForegroundApplicationChanged(appStateData) {
    console.info(`onForegroundApplicationChanged, appStateData: ${appStateData}.`);
  },
  onAbilityStateChanged(abilityStateData) {
    console.info(`onAbilityStateChanged, abilityStateData: ${abilityStateData}.`);
  },
  onProcessCreated(processData) {
    console.info(`onProcessCreated, processData: ${processData}.`);
  },
  onProcessDied(processData) {
    console.info(`onProcessDied, processData: ${processData}.`);
  },
  onProcessStateChanged(processData) {
    console.info(`onProcessStateChanged, processData: ${processData}.`);
  },
  onAppStarted(appStateData) {
    console.info(`onAppStarted, appStateData: ${JSON.stringify(appStateData)}`);
  },
  onAppStopped(appStateData) {
    console.info(`onAppStopped, appStateData: ${JSON.stringify(appStateData)}`);
  }
});
console.info(`observerCode: ${observerCode}.`);
```

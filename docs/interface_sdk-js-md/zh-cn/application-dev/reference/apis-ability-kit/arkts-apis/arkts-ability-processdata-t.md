# ProcessData

```TypeScript
export type ProcessData = _ProcessData.default
```

进程数据信息。

**起始版本：** 14

<!--Device-unnamed-export type ProcessData = _ProcessData.default--><!--Device-unnamed-export type ProcessData = _ProcessData.default-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**属性类型：** _ProcessData.default

**示例**

ArkTS-Dyn示例：

```TypeScript
import { appManager } from '@kit.AbilityKit';

let applicationStateObserver: appManager.ApplicationStateObserver = {
  onForegroundApplicationChanged(appStateData) {
    console.info(`onForegroundApplicationChanged, appStateData: ${JSON.stringify(appStateData)}.`);
  },
  onAbilityStateChanged(abilityStateData) {
    console.info(`onAbilityStateChanged, abilityStateData: ${JSON.stringify(abilityStateData)}.`);
  },
  onProcessCreated(processData) {
    console.info(`onProcessCreated, processData: ${JSON.stringify(processData)}.`);
  },
  onProcessDied(processData) {
    console.info(`onProcessDied, processData: ${JSON.stringify(processData)}.`);
  },
  onProcessStateChanged(processData) {
    console.info(`onProcessStateChanged, processData: ${JSON.stringify(processData)}.`);
  },
  onAppStarted(appStateData) {
    console.info(`onAppStarted, appStateData: ${JSON.stringify(appStateData)}.`);
  },
  onAppStopped(appStateData) {
    console.info(`onAppStopped, appStateData: ${JSON.stringify(appStateData)}.`);
  }
};
let observerCode = appManager.on('applicationState', applicationStateObserver);
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { appManager } from '@kit.AbilityKit';

class ApplicationStateObserverCustom implements appManager.ApplicationStateObserver {
  onForegroundApplicationChanged(appStateData: appManager.AppStateData) {
    console.info(`onForegroundApplicationChanged, appStateData: ${JSON.stringify(appStateData)}.`);
  }

  onAbilityStateChanged(abilityStateData: appManager.AbilityStateData) {
    console.info(`onAbilityStateChanged, abilityStateData: ${JSON.stringify(abilityStateData)}.`);
  }

  onProcessCreated(processData: appManager.ProcessData) {
    console.info(`onProcessCreated, processData: ${JSON.stringify(processData)}.`);
  }

  onProcessDied(processData: appManager.ProcessData) {
    console.info(`onProcessDied, processData: ${JSON.stringify(processData)}.`);
  }

  onProcessStateChanged(processData: appManager.ProcessData) {
    console.info(`onProcessStateChanged, processData: ${JSON.stringify(processData)}.`);
  }

  onAppStarted(appStateData: appManager.AppStateData) {
    console.info(`onAppStarted, appStateData: ${JSON.stringify(appStateData)}.`);
  }

  onAppStopped(appStateData: appManager.AppStateData) {
    console.info(`onAppStopped, appStateData: ${JSON.stringify(appStateData)}.`);
  }
}

let applicationStateObserver = new ApplicationStateObserverCustom();
let observerCode = appManager.onApplicationStateChange(applicationStateObserver);
```


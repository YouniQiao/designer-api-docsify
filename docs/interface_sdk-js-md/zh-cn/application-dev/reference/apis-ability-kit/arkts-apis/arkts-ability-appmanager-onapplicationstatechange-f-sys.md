# onApplicationStateChange（系统接口）

## 导入模块

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## onApplicationStateChange

```TypeScript
function onApplicationStateChange(observer: ApplicationStateObserver, filter: AppStateFilter): int
```

注册应用程序的状态监听器，并通过设置过滤条件来筛选所需监听的应用生命周期变化事件。

**起始版本：** 23

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver, filter: AppStateFilter): int--><!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver, filter: AppStateFilter): int-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| observer | ApplicationStateObserver | 是 | 应用状态监听器，用于监听应用的生命周期变化。 |
| filter | [AppStateFilter](arkts-ability-appmanager-appstatefilter-i-sys.md) | 是 | 应用生命周期变化事件的过滤器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 已注册监听器ID。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system application. |
| [16000050](../errorcode-ability.md#16000050-内部错误) | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module. |

**示例**

ArkTS-Sta示例：

```TypeScript
'use static'
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

class CustomApplicationStateObserver implements appManager.ApplicationStateObserver {
  public appStateData?: appManager.AppStateData;
  public abilityStateData?: appManager.AbilityStateData;
  public processData?: appManager.ProcessData;

  onForegroundApplicationChanged(appStateData: appManager.AppStateData): void {
    console.info(`[appManager] onForegroundApplicationChanged: ${JSON.stringify(appStateData)}`);
  }

  onAbilityStateChanged(abilityStateData: appManager.AbilityStateData): void {
    console.info(`[appManager] onAbilityStateChanged: ${JSON.stringify(abilityStateData)}`);
  }

  onProcessCreated(processData: appManager.ProcessData): void {
    console.info(`[appManager] onProcessCreated: ${JSON.stringify(processData)}`);
  }

  onProcessDied(processData: appManager.ProcessData): void {
    console.info(`[appManager] onProcessDied: ${JSON.stringify(processData)}`);
  }

  onProcessStateChanged(processData: appManager.ProcessData) {
    console.info(`[appManager] onProcessStateChanged: ${JSON.stringify(processData)}`);
  }

  onAppStarted(appStateData: appManager.AppStateData) {
    console.info(`[appManager] onAppStarted: ${JSON.stringify(appStateData)}`);
  }

  onAppStopped(appStateData: appManager.AppStateData) {
    console.info(`[appManager] onAppStopped: ${JSON.stringify(appStateData)}`);
  }
}

try {
  let applicationStateObserver = new CustomApplicationStateObserver();
  const observerId = appManager.onApplicationStateChange(applicationStateObserver);
  console.info(`[appManager] observerCode: ${observerId}`);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

class CustomApplicationStateObserver implements appManager.ApplicationStateObserver {
  public appStateData?: appManager.AppStateData;
  public abilityStateData?: appManager.AbilityStateData;
  public processData?: appManager.ProcessData;

  onForegroundApplicationChanged(appStateData: appManager.AppStateData): void {
    console.info(`[appManager] onForegroundApplicationChanged: ${JSON.stringify(appStateData)}`);
  }

  onAbilityStateChanged(abilityStateData: appManager.AbilityStateData): void {
    console.info(`[appManager] onAbilityStateChanged: ${JSON.stringify(abilityStateData)}`);
  }

  onProcessCreated(processData: appManager.ProcessData): void {
    console.info(`[appManager] onProcessCreated: ${JSON.stringify(processData)}`);
  }

  onProcessDied(processData: appManager.ProcessData): void {
    console.info(`[appManager] onProcessDied: ${JSON.stringify(processData)}`);
  }

  onProcessStateChanged(processData: appManager.ProcessData) {
    console.info(`[appManager] onProcessStateChanged: ${JSON.stringify(processData)}`);
  }

  onAppStarted(appStateData: appManager.AppStateData) {
    console.info(`[appManager] onAppStarted: ${JSON.stringify(appStateData)}`);
  }

  onAppStopped(appStateData: appManager.AppStateData) {
    console.info(`[appManager] onAppStopped:  ${JSON.stringify(appStateData)}`);
  }
}

try {
  let bundleNameList = ['bundleName1', 'bundleName2'];
  let applicationStateObserver = new CustomApplicationStateObserver();
  const observerId = appManager.onApplicationStateChange(applicationStateObserver, bundleNameList);
  console.info(`[appManager] observerCode: ${observerId}`);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```

